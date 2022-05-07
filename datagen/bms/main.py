import logging
import time
from kaa_client import KaaClient
from bms_gateway import BMSGateway

# Change application version
application_version = ''
# If you revoked the token, update this value with new one
token = 'room-1'
 
mqtt_host = 'mqtt.cloud.kaaiot.com'
mqtt_port = 1883
 
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
kaa_client = KaaClient(host=mqtt_host,
                        port=mqtt_port,
                        application_version=application_version,
                        token=token)
bms_gateway = BMSGateway(kaa_client)

# Command handlers
kaa_client.add_command_handler("sensor_toggle", bms_gateway.sensor_toggle)
kaa_client.add_configuration_status_handler(bms_gateway.configuration_handler)
logging.info(
    f"""
        Connect to kaa using:
        Host: [{mqtt_host}]
        Port: [{mqtt_port}]
        Application version name: [{application_version}]
        Token: [{token}]
    """
)
kaa_client.connect()

logging.info(f"Send device metadata [{bms_gateway.get_device_metadata()}]")
kaa_client.publish_metadata(bms_gateway.get_device_metadata())
while True:
    logging.info("Send BMS data")
    data_sample = bms_gateway.get_data_sample()
    logging.info(f"{data_sample}")
    kaa_client.publish_data_collection(data_sample)
    time.sleep(5)