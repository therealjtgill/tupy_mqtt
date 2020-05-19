import paho.mqtt.client as mqtt
import sys

def main(argv):
   client = mqtt.Client()
   #client.connect("172.31.43.249", 1883)
   client.connect("ec2-18-217-139-14.us-east-2.compute.amazonaws.com", 1883)
   client.publish("tupytest/msgs", argv[1])
   client.publish("tupyrobot/command", argv[1])

if __name__ == "__main__":
   main(sys.argv)
