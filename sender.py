import paho.mqtt.client as mqtt
import sys

def main(argv):
   client = mqtt.Client()
   client.connect("test.mosquitto.org", 1883)
   #client.subscribe("tupytest/msgs")
   client.publish("tupytest/msgs", argv[1])

if __name__ == "__main__":
   main(sys.argv)