#py -m pip install paho-mqtt
#py -m pip install pymongo
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from pymongo import MongoClient
import time
import json


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect('broker.mqttdashboard.com', 1883)

clientMongo=MongoClient(username='admin',password='admin',authSource='admin')
print("MongoDB Connection Successful")
mydb = clientMongo["usamovies"]
colmovies = mydb["movies"]




for mensagem in colmovies.find({},{"_id":0,"title":1, "year":1}):
    print(json.dumps(mensagem))
    client.publish("tst_fred_2",json.dumps(mensagem))
    time.sleep(0.5)    

clientMongo.close()