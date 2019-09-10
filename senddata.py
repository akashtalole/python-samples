#!/usr/bin/env python

import paho.mqtt.client as paho
import random
import time, json

mqttc = paho.Mosquitto()
mqttc.username_pw_set('username', 'password')
mqttc.connect("mqtt.com", 1883)

mqttc.loop_start()

while True:
    try:
        value = "%.1f" % random.uniform(10,50)
        lat = "%.1f" % random.uniform(10,50)
        lon = "%.1f" % random.uniform(10,50)
        elev = "%.1f" % random.uniform(10,50)
        #temperature = random.randint(0,100)    #random no generator
        ds = ['temp', 'humidity']#, 'battery', 'pressure', 'heartbeats', 'humid', 'test1']
        ds1 = ['temp', 'humidity']
        ds_name = random.choice(ds)
        ds_name1 = random.choice(ds1)
        topic = 'telemetry/8daa3270000b49039975b2684408982e/' + ds_name
        topic2 = 'telemetry/8daa3270000b49039975b2684408982e/' + ds_name1
        topic3 = 'telemetry/5acbe5a0b5c5460d8d6de4d3d4722a8f/battery'
        topic4 = 'telemetry/d13bf91190154eb392b8fb68a24a457f/' + ds_name
        #topic = 'telemetry/43054a2418ac421790ae425d2b84aee5/' + ds_name
        payload = json.dumps({"context":{"elevation": elev,"latitude": lat,"longitude": lon},"datastream_name": ds_name,"value": value})
        payload1 = json.dumps({"context":{"elevation": elev,"latitude": lat,"longitude": lon},"datastream_name": ds_name1,"value": value})
        payload2 = json.dumps({"context":{"elevation": elev,"latitude": lat,"longitude": lon},"datastream_name": 'battery',"value": value})
        rc, mid = mqttc.publish(topic, payload, qos=0, retain=False)
        rc, mid = mqttc.publish(topic2, payload1, qos=0, retain=False)
        rc, mid = mqttc.publish(topic3, payload2, qos=0, retain=False)
        rc, mid = mqttc.publish(topic4, payload, qos=0, retain=False)
        if rc != 0:
            print rc
        time.sleep(2)

    except KeyboardInterrupt:
            break

mqttc.loop_stop()
mqttc.disconnect()
