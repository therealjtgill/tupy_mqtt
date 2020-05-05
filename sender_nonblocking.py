import paho.mqtt.client as mqtt
import sys

def divisble_by_nine_question_mark(num):
   return ((num % 9) == 0)

def on_message(client, userdata, message):
   print("sender received a message", message.payload)

def main(argv):
   client = mqtt.Client()
   client.connect("test.mosquitto.org", 1883)
   client.subscribe("tupytest/from_receiver")
   client.on_message = on_message
   client.loop_start()

   stuff_we_care_about = []
   # Let's find the first 5000 numbers after 1000000 that are evenly
   # divisble by nine in an extremly inefficient way so that we can
   # can demonstrate loop_start() and loop_stop()
   counter = 1000000
   while len(stuff_we_care_about) < 5000:
      if divisble_by_nine_question_mark(counter):
         stuff_we_care_about.append(counter)
         payload = "jgill found a divvyniner! " + str(counter)
         client.publish("tupytest/from_sender", payload.encode())
      counter += 1

   client.loop_stop()

if __name__ == "__main__":
   main(sys.argv)