import random
import datetime
import uuid
import time
import logging
import paho.mqtt.client as mqtt
from kaa_client import KaaClient, CommandsDto, ConfigurationStatusResponseDto
from paho.mqtt.client import MQTTMessage

class ElectricMeter(object):
    def __init__(self, client: KaaClient):
        self.kaa_client = client
        self.lines = ["l1", "l2", "l3"]
        self.time = time.time()
        self.l1 = 1
        self.l2 = 1
        self.l3 = 1
        self.consumed_power = random.randint(991, 110000)
        self.config = {
          "overdriveThreshold": 240,
          "powerThreshold": None
        }
        self.simulateOverdrive = False

    def toggle(self, status: bool) -> None:
        self.l1 = status
        self.l2 = status
        self.l3 = status

    @staticmethod
    def get_device_metadata():
        return {
            "model": "Qubino Smart Meter 3-Phase",
            "lon": "-0.0395317",
            "lat": "51.5025671",
            "lastMaintenance": f"{datetime.datetime.now()}",
            "type": "electric meter",
            "serial": f"{uuid.uuid4()}",
            "Address": "Dock Hill Ave, Rotherhithe, London SE16 6AX, United Kingdom"
        }

    def _is_overdrive(self, voltage_total: int) -> bool:
      return bool(self.config["overdriveThreshold"] and voltage_total > self.config["overdriveThreshold"] * 3)

    def get_voltage(self):
      if self.simulateOverdrive is True:
        return random.randint(251, 300)
      else:
        return random.randint(215, 230)

    def get_current(self, line):
      if getattr(self, line):
        return random.randint(8, 10) * getattr(self, line)
      else:
        return 0

    @staticmethod
    def get_power(voltage, current):
        return voltage*current

    @staticmethod
    def get_current_reactive(current_active):
        return current_active / (random.randint(1, 10))

    def get_consumed_power(self, total_power):
        time_delta = (time.time() - self.time) / 3600
        self.consumed_power = self.consumed_power + time_delta * total_power
        return self.consumed_power

    def get_power_status(self):
      if self.l1 and self.l2 and self.l3:
        return 1
      return 0

    """
    Generates telemetry data sample.
    """
    def get_data_sample(self):
        data = {}
        for line in self.lines:
            data[f"voltage_{line}"] = self.get_voltage()
        voltage_total = sum([data[f"voltage_{line}"] for line in self.lines])
        if self._is_overdrive(voltage_total):
            for line in self.lines:
              setattr(self, line, 0)
              data[f"status_{line}"] = 0
        for line in self.lines:
            data[f"current_{line}_active"] = self.get_current(line)
            data[f"current_{line}_reactive"] = self.get_current_reactive(data[f"current_{line}_active"])
            data[f"current_{line}_total"] = data[f"current_{line}_active"] + data[f"current_{line}_reactive"]
            data[f"power_{line}_active"] = self.get_power(data[f"voltage_{line}"], data[f"current_{line}_active"])
            data[f"power_{line}_reactive"] = self.get_power(data[f"voltage_{line}"], data[f"current_{line}_reactive"])
            data[f"power_{line}_total"] = self.get_power(data[f"voltage_{line}"], data[f"current_{line}_total"])
            data[f"status_{line}"] = getattr(self, line)
        
        data["current_total"] = sum([data[f"current_{line}_total"] for line in self.lines])
        data["power_total"] = sum([data[f"power_{line}_total"] for line in self.lines])
        data["power_active"] = sum([data[f"power_{line}_active"] for line in self.lines])
        data["power_reactive"] = sum([data[f"power_{line}_reactive"] for line in self.lines])
        data["consumed_power"] = self.get_consumed_power(data["power_total"])
        data["power_status"] = self.get_power_status()
        data["voltage_total"] = voltage_total

        return data

    """
    command type: electric_meter_toggle
    example of payloads:
    Turn off all lines
    {
      "l1": 0,
      "l2": 0,
      "l3": 0
    }
    Turn on the Line 1
    {
      "l1": 1
    }
    """
    def electric_meter_handler(self, client: mqtt.Client, userdata, message: MQTTMessage):
        command_payload = str(message.payload.decode('utf-8'))
        logging.info(f"Received command: [{message.topic}] []")
        response_topic = KaaClient.get_command_response_topic(message, "electric_meter_toggle")
        commands = CommandsDto(command_payload).get_command_responses()
        for command in commands:
            try:
                for key in command.payload.keys():
                    setattr(self, key, int(command.payload[key]))
                    command.status_code = 200
                    command.payload[key] = "status changed"
            except Exception as error:
                logging.error(f"Invalid command payload [{error}] [{command.to_dict()}]")
        client.publish(response_topic, self.kaa_client.compose_commands_result(commands))


    """
    Command to simulate overdrive
    Send command type `electric_meter_overdrive` to turn on the overdrive.
    Send payload { "off": true } to switch to normal mode.
    """
    def electric_meter_overdrive_handler(self, client: mqtt.Client, userdata, message: MQTTMessage):
        command_payload = str(message.payload.decode('utf-8'))
        logging.info(f"Received command: [{message.topic}] []")
        response_topic = KaaClient.get_command_response_topic(message, "electric_meter_overdrive")
        commands = CommandsDto(command_payload).get_command_responses()
        last_command = commands[-1].to_dict()
        for command in commands:
          command.status_code = 200
          command.reasonPhrase = "Ok"
        if last_command and "off" in last_command["payload"]:
          self.simulateOverdrive = False
        else:
          self.simulateOverdrive = True
        client.publish(response_topic, self.kaa_client.compose_commands_result(commands))

    """
    Handle value `overdriveThreshold` published from configuration.
    When avarage voltage is less then threshold value simulator will turn off all the lines
    """
    def configuration_handler(self, client: mqtt.Client, userdata, message):
      configuration_payload = str(message.payload.decode('utf-8'))
      logging.info("Received configuration")
      if configuration_payload:
        self.config = ConfigurationStatusResponseDto(configuration_payload).to_dict()["config"]
      