import paho.mqtt.client as mqtt
import sys
import time

def on_message(client, userdata, message):
   print("received a message!", str(message.payload))
   message = message.payload.decode("utf-8")
   number = int(message.split(" ")[-1])
   if (number % 5) == 0:
      payload = str(number) + " is also divisible by five"
      client.publish("tupytest/from_receiver", payload)

def main(argv):
   client = mqtt.Client()
   client.connect("test.mosquitto.org", 1883)
   client.subscribe("tupytest/from_sender")
   client.on_message = on_message

   client.loop_forever()

if __name__ == "__main__":
   main(sys.argv)