import json

import paho.mqtt.client as paho
from cryptography.fernet import Fernet


BROKER = "10.25.35.225"
PORT = 1883
TOPIC = "chat"

KEY = b'otAovNOfb4LcxWr-uTPTz2zTmETc7iaNO2GnHd43qC8='

f = Fernet(KEY)

client = paho.Client()
client.username_pw_set(username="smooth", password="")


def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        encrypted_message = payload["Message"].encode()
        decrypted = f.decrypt(encrypted_message).decode()
        print(f"\nReceived: {decrypted}")
    except Exception as e:
        print(f"Error decrypting message: {e}")


def publish(message):
    try:
        encrypted = f.encrypt(message.encode()).decode()
        payload = {
            "Group": "Smooth",
            "Message": encrypted
        }
        msg = json.dumps(payload)
        result = client.publish(TOPIC, msg)
        status = result[0]
        if status == 0:
            print(f"Sent encrypted message")
        else:
            print("Failed to send message")

    except Exception as e:
        print(f"Publish error: {e}")


def run():
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.subscribe(TOPIC)
    client.loop_start()

    while True:
        message = input("Enter message: ")
        if message.lower() == "exit":
            break
        publish(message)

    client.loop_stop()
    client.disconnect()


if __name__ == "__main__":
    run()