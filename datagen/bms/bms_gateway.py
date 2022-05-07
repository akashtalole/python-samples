import random
import math
import datetime
import uuid
import time
import logging
import paho.mqtt.client as mqtt
from kaa_client import KaaClient, CommandsDto, ConfigurationStatusResponseDto
from paho.mqtt.client import MQTTMessage

class BMSGateway(object):
    def __init__(self, client: KaaClient):
        self.metadata = {
          "name": "Room 1",
          "lon": "-0.0395317",
          "lat": "51.5025671",
          "Address": "Dock Hill Ave, Rotherhithe, London SE16 6AX, United Kingdom"
        }
        self.kaa_client = client
        self.devices = ["ac", "cleaner", "humidifier"]
        self.time = time.time()
        self.ac = 1
        self.ac_fan_speed = 1
        self.cleaner = 1
        self.humidifier = 1
        self.ac_mode = 1
        self.air_ionization = 1
        self.config = {
            "temperatureSetpoint": 24,
            "humiditySetpoint": 60
        }

    def get_device_metadata(self):
        self.metadata["lastMaintenance"] = str(datetime.datetime.now())
        self.metadata["serial"] = str(uuid.uuid4())
        return self.metadata

    def get_ac_data(self):
        if self.ac == 0:
            return {}
        else:
            now = datetime.datetime.now()
            return {
                'temperature': abs(self.config['temperatureSetpoint'] * math.sin(now.minute + now.second/60.0)),
                'temperature_setpoint': self.config['temperatureSetpoint'],
                'ac_fan_speed': self.ac_fan_speed,
                'ac_mode': self.ac_mode
            }
    
    def get_humidifier_data(self):
        if self.humidifier == 0:
            return {}
        else:
            return {
                "humidity": random.randint(self.config['humiditySetpoint'] - 20, self.config['humiditySetpoint']),
                "humidity_setpoint": self.config['humiditySetpoint']
            }

    """
    Generates telemetry data for air cleaner device
    """
    def get_cleaner_data(self):
        if self.cleaner == 0:
            return {}
        else:
            return {
                "filter_condition": 10,
                "air_pollution": random.randint(2, 151),
                "status_ionization": self.air_ionization
            }

    """
    Generates telemetry data sample.
    """
    def get_data_sample(self):
        data = {}
        for device in self.devices:
            data[f"status_{device}"] = getattr(self, device)
        now = datetime.datetime.now()
        
        data.update(self.get_ac_data())
        data.update(self.get_humidifier_data())
        data.update(self.get_cleaner_data())
        data['pressure'] = 800 + abs(200 * math.cos(now.minute + now.second/60.0) + now.hour)
        
        return data

    """
    command name: sensor_toggle
    example of payloads:
    Turn off all sensors
    {
      "ac": 0,
      "humidifier": 0,
      "cleaner": 0
    }
    Turn on the AC
    {
      "ac": 1
    }
    """
    def sensor_toggle(self, client: mqtt.Client, userdata, message: MQTTMessage):
        command_payload = str(message.payload.decode('utf-8'))
        logging.info(f"Received command: [{message.topic}] []")
        response_topic = KaaClient.get_command_response_topic(
            message, "sensor_toggle")
        commands = CommandsDto(command_payload).get_command_responses()
        for command in commands:
            try:
                for key in command.payload.keys():
                    setattr(self, key, int(command.payload[key]))
                    command.status_code = 200
                    command.payload[key] = "status changed"
            except Exception as error:
                logging.error(
                    f"Invalid command payload [{error}] [{command.to_dict()}]")
        client.publish(
            response_topic, self.kaa_client.compose_commands_result(commands))

    """
    Handle values `temperatureSetpoint` and `humiditySetpoint` published from configuration.
    Simulator will update temperature and humidity telemetry data according to appropriate set point
    """
    def configuration_handler(self, client: mqtt.Client, userdata, message):
        configuration_payload = str(message.payload.decode('utf-8'))
        logging.info("Received configuration")
        config = ConfigurationStatusResponseDto(
            configuration_payload).to_dict()["config"]
        if configuration_payload:
            for key in config.keys():
                self.config[key] = config[key]
