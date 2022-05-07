import random
import math
import datetime
import uuid
import time
import logging
import json
import paho.mqtt.client as mqtt
from kaa_client import KaaClient, CommandsDto, ConfigurationStatusResponseDto
from paho.mqtt.client import MQTTMessage

class Vehicle(object):
    def __init__(self, client: KaaClient):
        self.kaa_client = client
        self.time = time.time()
        self.config = {
            "maxSpeed": 185,
            "maxRange": 555,
            "maintenanceInterval": 15000,
            "climateSetpoint": 21
        }

        self.mileage = random.randint(0, 200)
        self.routes = json.load(open('./routes.json'))
        self.route_point = -1

        self.engine = 1
        self.trunk = 1
        self.windows = 1
        self.lock = 1
        self.lights = 0
        self.beep = 0
        self.climate = 1

        self.statuses = ['engine', 'trunk', 'windows', 'lock', 'lights', 'beep', 'climate']

        self.range = self.config['maxRange']
        self.metadata = {
          'name': "Vehicle 1",
          'lon': -0.0395317,
          'lat': 51.5025671,
          'engine': "gasoline",
          'model': "Boxster",
          'brand': "Porsche",
          'year': "2019",
          'maxSpeed': 265,
          'maxRange': 447,
          'power': 256,
          'Address': "Dock Hill Ave, Rotherhithe, London SE16 6AX, United Kingdom"
        }

    def get_device_metadata(self):
        self.metadata["lastMaintenance"] = str(datetime.datetime.now())
        self.metadata["serial"] = str(uuid.uuid4())
        return self.metadata
    
    """
    Generates tiers data
    """
    def get_tiers_data(self):
        if self.engine == 0:
            return {}
        else:
            front_tires = random.uniform(2.35, 2.4)
            rear_tires = random.uniform(2.2, 2.3)
            
            return {
                'tiers': {
                    'front_left': front_tires,
                    'front_right': front_tires,
                    'back_left': rear_tires,
                    'back_right': rear_tires
                }
            }
    
    """
    Generates hill assist data
    """
    def get_hill_assist_data(self):
        if self.engine == 0:
            return {}
        else:
            return {
                'gyro_x': random.randint(0, 20),
                'gyro_y': random.randint(0, 15),
                'gyro_z': random.randint(0, 5),
            }
    
    def get_climate_data(self):
        if self.engine == 0:
            return {}
        else:
            now = datetime.datetime.now()
            return {
                'climate_temperature': (self.config['climateSetpoint'] - 3) + 3 * math.cos(now.minute + now.second/60.0)
            }
    
    """
    Generates engine data
    """
    def get_engine_data(self):
        if self.engine == 0:
            return {}
        else: 
            self.mileage += random.randint(10, 40)
            self.range -= random.randint(1, 5)

            if self.range < 0:
                self.range = self.config['maxRange']
                self.kaa_client.publish_data_collection({
                    'log': {
                        'message': 'Max range exceeded. Vehicle filled up',
                        'location': 'UK, London'
                    }
                })

            maintenance_in = self.config['maintenanceInterval'] - self.mileage

            return {
                'speed': random.randint(40, 110),
                'rpm': random.randint(600, 2000),
                'mileage': self.mileage,
                'range': self.range,
                'maintenance_in': 0 if maintenance_in < 0 else maintenance_in,
                'engine_temperature': random.randint(62, 95)
            }

    """
    Generates location data
    """
    def get_location_data(self):
        if self.engine == 0:
            return {}
        else:
            next_point = [self.metadata['lat'], self.metadata['lon']]

            try:
                self.route_point += 1
                next_point = self.routes[self.route_point]
            except:
                self.route_point = 0
                next_point = self.routes[self.route_point]

            return {
                'location': {
                    'lat': next_point[0],
                    'lon': next_point[1]
                }
            }
    
    """
    Generates telemetry data sample.
    """
    def get_data_sample(self):
        data = {}

        for name in self.statuses:
            data[f"{name}_status"] = getattr(self, name)

        data.update(self.get_tiers_data())
        data.update(self.get_engine_data())
        data.update(self.get_hill_assist_data())
        data.update(self.get_location_data())
        data.update(self.get_climate_data())

        return data
    
    """
    Logs command as telemetry
    """
    def log_command(self, key: str, value: int):
        messages = {
            'engine': {0: 'Engine off', 1: 'Engine on'},
            'trunk': {0: 'Trunk closed', 1: 'Trunk opened'},
            'windows': {0: 'Windows closed', 1: 'Windows opened'},
            'lock': {0: 'Car locked', 1: 'Car opened'},
            'beep': {0: 'Horn sound off', 1: 'Horn on'},
            'climate': {0: 'AC off', 1: 'AC on'}
        }
        if key in messages:
            self.kaa_client.publish_data_collection({
                'log': {
                    'message': messages[key][value],
                    'location': 'UK, London'
                }
            })

    """
    command name: remote_toggle
    example of payloads:
    Can be one or combination of keys:
    {
        "engine": 1,
        "trunk": 1,
        "windows": 1,
        "lock":  1,
        "lights": 0,
        "beep": 0,
        "climate": 1
    }
    """
    def sensor_toggle(self, client: mqtt.Client, userdata, message: MQTTMessage):
        command_payload = str(message.payload.decode('utf-8'))
        logging.info(f"Received command: [{message.topic}] []")
        response_topic = KaaClient.get_command_response_topic(
            message, "remote_toggle")
        commands = CommandsDto(command_payload).get_command_responses()
        for command in commands:
            try:
                for key in command.payload.keys():
                    payload_value = int(command.payload[key])
                    setattr(self, key, payload_value)
                    command.status_code = 200
                    command.payload[key] = "status changed"
                    self.log_command(key, payload_value)
            except Exception as error:
                logging.error(
                    f"Invalid command payload [{error}] [{command.to_dict()}]")
        client.publish(
            response_topic, self.kaa_client.compose_commands_result(commands))

    """
    Handle values `maxSpeed`, `maxRange`, `maintenanceInterval`, `climateSetpoint`  published from configuration.
    """
    def configuration_handler(self, client: mqtt.Client, userdata, message):
        configuration_payload = str(message.payload.decode('utf-8'))
        logging.info("Received configuration")
        config = ConfigurationStatusResponseDto(
            configuration_payload).to_dict()["config"]
        if configuration_payload:
            for key in config.keys():
                self.config[key] = config[key]
