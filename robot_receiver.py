from control_motors import MotorController
import json
import paho.mqtt.client as mqtt
import time

class Receiver:
   def __init__(self, mc):
      self.message_wait_time = 15
      self.last_rx_time = time.time() - 15

      self.client_name = "ec2-18-217-139-14.us-east-2.compute.amazonaws.com"
      self.client = mqtt.Client()
      self.client.connect(self.client_name, 1883)
      self.client.subscribe("tupyrobot/command")
      self.client.on_message = self.on_message

      self.mc = mc

   def on_message(self, client, userdata, message):
      print("Received message")
      msg = message.payload.decode("utf-8")
      print(msg)
      time_remaining = min(
         time.time() - (self.last_rx_time + self.message_wait_time),
         0
      )
      print(time_remaining, "seconds remaining")
      #if (self.last_rx_time + self.message_wait_time) <= time.time():
      if time_remaining >= 0:
         print("Executing message")
         self.last_rx_time = time.time()
         try:
            commands = json.loads(msg)
            # Only keep the first 4 commands.
            commands = commands[0:5]
            for cmd in commands:
               print("Command: ", cmd[0], "Execution time:", cmd[1])
               if "forward" in str(cmd[0]).lower():
                  self.mc.go_forward(cmd[1])
               elif "backward" in str(cmd[0]).lower():
                  self.mc.go_backward(cmd[1])
               elif "right" in str(cmd[0]).lower():
                  self.mc.turn_right(cmd[1])
               elif "left" in str(cmd[0]).lower():
                  self.mc.turn_left(cmd[1])
         except Exception as e:
            print("Error occurred attempting to parse message,", str(e))
         
   def start(self):
      self.client.loop_forever()

if __name__ == "__main__":
   m1_pins = {
      "forward": 6,
      "backward": 12,
      "pwm": 18
   }

   m2_pins = {
      "forward": 19,
      "backward": 16,
      "pwm": 17
   }

   mc = MotorController(m1_pins, m2_pins, 10)

   #mc.go_forward(1.5)

   receiver = Receiver(mc)
   receiver.client.loop_forever()
