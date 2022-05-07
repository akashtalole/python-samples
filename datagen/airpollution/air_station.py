import random
import datetime
import uuid
import time
import datetime
from typing import Dict
from kaa_client import KaaClient

class AirStation(object):
    def __init__(self, client: KaaClient, metadata: dict):
        self.kaa_client = client
        self.time = time.time()
        self.metadata = metadata

    def get_device_metadata(self):
        self.metadata["lastMaintenance"] = str(datetime.datetime.now())
        self.metadata["serial"] = str(uuid.uuid4())
        return self.metadata

    def get_latest_metadata(self):
        return self.metadata

    def get_climate_data(self):
        """
        Generates data from temperature and humidity sensors
        """
        return {
            "humidity": random.randint(60, 90),
            "temperature": random.randint(-10, 40)
        }

    def get_pm_sensor_data(self) -> Dict[str, int]:
        """
        Generates data for PM(Particulate Matter) sensors
        """
        self.metadata["PM_2_sensor"] = random.randint(0, 800)
        self.metadata["PM_10_sensor"] = random.randint(0, 1200)

        return {
            "pm2": self.metadata["PM_2_sensor"],
            "pm10": self.metadata["PM_10_sensor"]
        }

    def get_gas_sensor(self) -> Dict[str, int]:
        """
        Generates data for Nitrogen Dioxide Sensor, Ozone, Sulphur Dioxide
        """
        self.metadata["n2"] = random.randint(0, 1000)
        self.metadata["o3"] = random.randint(0, 800)
        self.metadata["so2"] = random.randint(0, 1250)

        return {
            "n2": self.metadata["n2"],
            "o3": self.metadata["o3"],
            "so2": self.metadata["so2"]
        }

    def get_air_quality(self) -> Dict[str, int]:
        """
        Generates data for Air Quality Index 
        """
        self.metadata["airQuality"] = random.randint(1, 6)
        return {
            "aq": self.metadata["airQuality"]
        }

    """
    Generates telemetry data sample.
    """
    def get_data_sample(self):
        data = {}
        data.update(self.get_air_quality())
        data.update(self.get_gas_sensor())
        data.update(self.get_pm_sensor_data())
        data.update(self.get_climate_data())

        return data