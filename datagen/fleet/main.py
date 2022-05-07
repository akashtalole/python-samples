import logging
import time
from kaa_client import KaaClient
from vehicle import Vehicle

# Change application version
application_version = ''
# If you revoked the token, update this value with new one
token = 'vehicle-1'
 
mqtt_host = 'mqtt.cloud.kaaiot.com'
mqtt_port = 1883
 
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

kaa_client = KaaClient(mqtt_host, mqtt_port, application_version, token)
vehicle = Vehicle(kaa_client)

# Command handler
kaa_client.add_command_handler("remote_toggle", vehicle.sensor_toggle)

# Configuration handler
kaa_client.add_configuration_status_handler(vehicle.configuration_handler)

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

logging.info(f"Send device metadata [{vehicle.get_device_metadata()}]")
kaa_client.publish_metadata(vehicle.get_device_metadata())

while True:
    logging.info("Send Vehicle data")
    data_sample = vehicle.get_data_sample()
    logging.info(f"{data_sample}")
    kaa_client.publish_data_collection(data_sample)
    time.sleep(1)
