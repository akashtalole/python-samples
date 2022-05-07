import paho.mqtt.client as mqtt
import json
import logging
from typing import List
from paho.mqtt.client import MQTTMessage
import random

class CommandResponseDto(object):
    def __init__(self, command_id: int, status_code=None, payload=None):
        self.command_id = command_id
        self.status_code = status_code
        self.payload = payload

    def to_dict(self) -> dict:
        return {
            "id": self.command_id,
            "statusCode": self.status_code,
            "payload": self.payload
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

class ConfigurationStatusResponseDto(object):
  def __init__(self, payload):
    self.payload = json.loads(payload)

  def to_dict(self):
    return {
      "configId": self.payload["configId"],
      "statusCode": self.payload["statusCode"],
      "reasonPhrase": self.payload["reasonPhrase"],
      "config": self.payload["config"]
    }

  def to_json(self):
    return json.dumps(self.to_dict())


class CommandsDto(object):
    def __init__(self, payload=None):
        self.payload = json.loads(payload)
        
    def get_command_responses(self) -> List[CommandResponseDto]:
        return [CommandResponseDto(command["id"], payload=command["payload"]) for command in self.payload]

"""
Kaa MQTT client that simplifies device communication with kaa platform.
Check our tutorials about how to connect different devices:
https://docs.kaaiot.io/KAA/docs/current/Tutorials/device-integration/hardware-guides/
"""
class KaaClient(object):
    def __init__(self, host, port, application_version, token, client_id="fleet_sim"):
        self.host = host
        self.port = port
        self.token = token
        self.application_version = application_version
        self.client = mqtt.Client(client_id=client_id)
        self.client.on_message = self.on_message

    """
    Adds command handler by specified command type.
    For more information about command protocol see rfc document:
    https://github.com/kaaproject/kaa-rfcs/blob/master/0011/README.md

    Also check our tutorial about command execution:
    https://docs.kaaiot.io/KAA/docs/current/Tutorials/getting-started/sending-commands-to-device/
    """
    def add_command_handler(self, name, handler):
        self.client.message_callback_add(self._topic_command(name), handler)

    """
    Returns command result topic name.
    For more information about command protocol see rfcs document:
    https://github.com/kaaproject/kaa-rfcs/blob/master/0011/README.md#result-resource#command-resource
    """
    @staticmethod
    def get_command_response_topic(message: MQTTMessage, command_name):
        return f"{message.topic}".replace(f"command/{command_name}/status", f"result/{command_name}")

    """
    Returns command status topic name.
    For more information about command protocol see rfcs document:
    https://github.com/kaaproject/kaa-rfcs/blob/master/0011/README.md
    """
    def _topic_command(self, name):
        return f"kp1/{self.application_version}/cex/{self.token}/command/{name}/status"

    """
    Returns configuration status topic name.
    For more information about configuration management protocol see rfc document:
    https://github.com/kaaproject/kaa-rfcs/blob/master/0007/README.md
    """
    def _topic_configuration_status(self):
      return f"kp1/{self.application_version}/cmx/{self.token}/config/json/status"

    """
    Sends metadata from device.
    For more information check endpoint metadata protocol rfc:
    https://github.com/kaaproject/kaa-rfcs/blob/master/0010/README.md

    Metadata covered in getting started guides:
    https://docs.kaaiot.io/KAA/docs/current/Tutorials/getting-started/
    """
    def publish_metadata(self, payload: dict) -> None:
        result = self.client.publish(topic=self.topic_metadata(), payload=json.dumps(payload))
        self._check_send_result(result)

    """
    Sends metadata from device.
    For more information check data collection protocol rfc:
    https://github.com/kaaproject/kaa-rfcs/blob/master/0002/README.md

    Data collection covered in data collection tutorial:
    https://docs.kaaiot.io/KAA/docs/current/Tutorials/getting-started/collecting-data-from-a-device/
    """
    def publish_data_collection(self, payload: dict) -> None:
        result = self.client.publish(topic=self._topic_data_collection(), payload=json.dumps(payload))
        self._check_send_result(result)

    """
    Returns update metadata topic name.
    """
    def topic_metadata(self):
        return f"kp1/{self.application_version}/epmx/{self.token}/update/keys/{random.randint(1,99)}"

    """
    Returns send time series data name.
    """
    def _topic_data_collection(self):
        return f"kp1/{self.application_version}/dcx/{self.token}/json/{random.randint(1,99)}"

    """
    Adds callback to execute when new configuration is sent to the device.
    For more information about configuration management protocol see rfc document:
    https://github.com/kaaproject/kaa-rfcs/blob/master/0007/README.md
    """
    def add_configuration_status_handler(self, handler) -> None:
      self.client.message_callback_add(self._topic_configuration_status(), handler)

    def connect(self):
        self.client.connect(self.host, self.port, 60)
        self.client.on_message = self.on_message
        self.client.loop_start()

    def _check_send_result(self, result):
        if result.rc != 0:
            logging.error("Unable to send data to platform try to reconnect")
            self.connect()

    @staticmethod
    def compose_commands_result(commands: List[CommandResponseDto]):
        command_results = [command.to_dict() for command in commands]
        return json.dumps(command_results)

    @staticmethod
    def on_message(client, userdata, message: MQTTMessage):
        logging.info(f"Message received: topic [{message.topic}] body [{str(message.payload.decode('utf-8'))}]")
