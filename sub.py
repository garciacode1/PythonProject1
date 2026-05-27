import json

import paho.mqtt.client as paho
from paho import mqtt
import time
from Caesar import *




client = paho.Client()
client.username_pw_set(username='smooth', password='')



def publish(client, encrypted):
        time.sleep(1)
        data_to_send = {"GROUP": "Smooth", "MESSAGE:": encrypted}
        msg = json.dumps(data_to_send)
        result = client.publish('chat', msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Sent `{msg}` to topic 'chat'")
        else:
            print(f"Failed to send message to topic 'chat'")

def subscribe(client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe('chat')
    client.on_message = on_message
    return client.on_message


def run():
    client.connect('10.25.35.225', 1883, 60)
    while True:

        client.loop_start()
        message = input("Enter message to publish: ")
        encrypted = caesar_cypher(message)
        publish(client, encrypted)
        message_received = subscribe(client)
        print(message_received)
        if message_received["GROUP"] == "Smooth":
            decrypt_cypher(message_received['MESSAGE'])

if __name__ == '__main__':
    run()