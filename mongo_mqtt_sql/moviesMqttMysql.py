import sys
import paho.mqtt.client as mqtt
#import mysql.connector as mariadb
#from mysql.connector import Error

def on_connect(client, userdata, flags, rc):
        print("Connected to MQTT with result code "+str(rc))
        print("subscribing")
        client.subscribe(topic)

# def on_subscribe(client, userdata, mid, reason_code_list, properties):
#     # Since we subscribed only for a single channel, reason_code_list contains
#     # a single entry
#     if reason_code_list[0].is_failure:
#         print(f"Broker rejected you subscription: {reason_code_list[0]}")
#     else:
#         print(f"Broker granted the following QoS: {reason_code_list[0].value}")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
# def on_message(client, userdata, msg):
#     global connection
#     try:
#         decoded_message = msg.payload.decode("utf-8")
#         message=decoded_message.split(",")
#         title=message[0].split(":")[1]
#         year=(message[1].split(":")[1]).split("}")[0]
#         Sql = "insert into movies (title, year) values ( " +title + ", " + year +" );"  
#         print(msg)
#         try:
#                 cursor = connection.cursor()
#                 print(Sql)
#                 cursor.execute(Sql)           
#         except:
#                 print ("Error: unable to insert MYSQL")         
#     except:
#         print ("Error: unable to receive message from MQTT")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# client.on_subscribe = on_subscribe
topic="tst_fred_2"
client.connect('broker.mqttdashboard.com', 1883)  

# try:
#       connection = mariadb.connect(host="localhost", user="root", passwd="", db="usamovies",connect_timeout=1000,autocommit=True)
#       print("Connected to Mysql")
# except Error as e:
#     print("Error while connecting to MySQL Database", e) 

while True:
    client.loop()



print(message)