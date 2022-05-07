import logging
from kaa_client import KaaClient
from air_station import AirStation
import time
import json

# Change application version
application_version = ''
# If you revoked the token, update this value with new one
token = 'air-station-1'
 
mqtt_host = 'mqtt.cloud.kaaiot.com'
mqtt_port = 1883

publish_interval = 60

metadata = {
  "name": "Newcastle Cradlewell Roadside - UKA00528",
  "lon": -1.595362,
  "lat": 54.986405,
  "location": "Newcastle upon Tyne"
}
 
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

kaa_client = KaaClient(mqtt_host, mqtt_port, application_version, token)
air_station = AirStation(kaa_client, metadata)

logging.info(
    f"""
        Connect to kaa using:
        Host: [{mqtt_host}]
        Port: [{mqtt_port}]
        Application version name: [{application_version}]
        Token: [{token}]
    """
)

# Start mqtt connection
kaa_client.connect()

logging.info(f"Send device metadata [{air_station.get_device_metadata()}]")
kaa_client.publish_metadata(air_station.get_device_metadata())

while True:
    logging.info("Send Air pollution data")
    data_sample = air_station.get_data_sample()
    logging.info(f"{json.dumps(data_sample)}")
    kaa_client.publish_data_collection(data_sample)
    kaa_client.publish_metadata(air_station.get_latest_metadata())
    time.sleep(publish_interval)