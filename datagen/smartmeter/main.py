import logging
import time
from kaa_client import KaaClient
from electric_meter import ElectricMeter

# Change application version
application_version = ''
# If you revoked the token, update this value with new one
token = 'smart-meter-1'
 
mqtt_host = 'mqtt.cloud.kaaiot.com'
mqtt_port = 1883
 
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

kaa_client = KaaClient(mqtt_host, mqtt_port, application_version, token)
electric_meter = ElectricMeter(kaa_client)

# Command handlers
# Handle command to toggle device lines
kaa_client.add_command_handler("electric_meter_toggle", electric_meter.electric_meter_handler)
# Handle overdrive mode simulation command
kaa_client.add_command_handler("electric_meter_overdrive", electric_meter.electric_meter_overdrive_handler)

# Device configuration change handler
kaa_client.add_configuration_status_handler(electric_meter.configuration_handler)

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

logging.info(f"Send device metadata [{electric_meter.get_device_metadata()}]")
kaa_client.publish_metadata(electric_meter.get_device_metadata())

while True:
    logging.info("Send ElectricMeter data")
    data_sample = electric_meter.get_data_sample()
    logging.info(f"{data_sample}")
    kaa_client.publish_data_collection(data_sample)
    time.sleep(1)
