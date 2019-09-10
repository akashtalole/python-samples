import paho.mqtt.client as mqtt
from datetime import datetime
import json, uuid
from pymongo import MongoClient
from ast import literal_eval
from flask import Flask
from mongoalchemy.document import Document
from mongoalchemy.fields import *
#from flask_cqlalchemy import CQLAlchemy

class Data(Document):

        value = StringField(required=True, default='')
        context = DictField(AnythingField(), required=False, default={})
#        tstamp = StringField(required=True)
        tstamp = DateTimeField(required=True)
        device_id = StringField(DocumentField('Devices.device_id'), required=True, default='')
        datastream_name = StringField(required=True, default='')


def on_connect(client, userdata, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("#")

def on_message(client, userdata, msg):
        tstamp=datetime.now()#.isoformat()
#       print msg.payload
        try:
                message = json.loads(msg.payload)
        except ValueError:
                return
        if sorted(["context", "value", "datastream_name"]) != sorted(message.keys()):
                return
        device_id = msg.topic.split("/")[1]
        context = message["context"]
        value = message["value"]
        datastream_name = message["datastream_name"]
        if datastream_name == "" or value == "":
                return

        #print(str(receiveTime) + ": " + msg.topic + " " + message)
#       db.sync_db()
        #Datas.create(value=value, device_id=device_id, tstamp=tstamp, latitude=context["latitude"], longitude=context["longitude"], elevation=context["elevation"])
#       data.save()
        post={"tstamp":tstamp, "device_id":device_id, "value":value, "context":context, "datastream_name":datastream_name}
        #print post
        collection.insert(post)
        #session.save(Data(**post))



from mongoalchemy.session import Session
session = Session.connect('mqtt_data', host='mongodb://127.0.0.1:27017/mqtt_data')
#session.clear_collection(Data)
#print "Connected to DB"


# Set up client for MongoDB
mongoClient=MongoClient("127.0.0.1:27017")
db=mongoClient.mqtt_data
collection=db.Data
print "Connected to DB"

# Initialize the client that should connect to the Mosquitto broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("user1", "password")
client.connect("127.0.0.1", 1883, 60)

# Blocking loop to the Mosquitto broker
client.loop_forever()
