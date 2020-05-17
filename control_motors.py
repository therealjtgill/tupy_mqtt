import sys
import time
import RPi.GPIO as GPIO

class MotorController:
   def __init__(self, m1_pins, m2_pins, max_time=-1):
      self.max_time = max_time
      self.m1_pins = m1_pins
      self.m2_pins = m2_pins

      GPIO.setmode(GPIO.BCM)

      for _, pin in self.m1_pins.items():
         GPIO.setup(pin, GPIO.OUT)

      for _, pin in self.m2_pins.items():
         GPIO.setup(pin, GPIO.OUT)

      self.m1_pwm = GPIO.PWM(self.m1_pins["pwm"], 100)
      self.m2_pwm = GPIO.PWM(self.m2_pins["pwm"], 100)

      self.m1_pwm.start(0)
      self.m2_pwm.start(0)

   def pulse_pwm(self, duty_cycle=75):
      self.m1_pwm.ChangeDutyCycle(duty_cycle)
      self.m2_pwm.ChangeDutyCycle(duty_cycle)

   def go_forward(self, exec_time):
      exec_time = min(exec_time, self.max_time)
      sleep_time = 0.1
      num_loops = int(10*exec_time)
      print("num loops:", num_loops)
      GPIO.output(self.m1_pins["forward"], GPIO.LOW)
      GPIO.output(self.m1_pins["backward"], GPIO.HIGH)
      GPIO.output(self.m2_pins["forward"], GPIO.LOW)
      GPIO.output(self.m2_pins["backward"], GPIO.HIGH)
      for i in range(num_loops):
         self.pulse_pwm()
         time.sleep(0.1)
      self.pulse_pwm(0)

   def go_backward(self, exec_time):
      exec_time = min(exec_time, self.max_time)
      sleep_time = 0.1
      num_loops = int(10*exec_time)
      GPIO.output(self.m1_pins["forward"], GPIO.HIGH)
      GPIO.output(self.m1_pins["backward"], GPIO.LOW)
      GPIO.output(self.m2_pins["forward"], GPIO.HIGH)
      GPIO.output(self.m2_pins["backward"], GPIO.LOW)
      for i in range(num_loops):
         self.pulse_pwm()
         time.sleep(0.1)
      self.pulse_pwm(0)

   def turn_right(self, exec_time):
      exec_time = min(exec_time, self.max_time)
      sleep_time = 0.1
      num_loops = int(10*exec_time)
      GPIO.output(self.m1_pins["forward"], GPIO.HIGH)
      GPIO.output(self.m1_pins["backward"], GPIO.LOW)
      GPIO.output(self.m2_pins["forward"], GPIO.LOW)
      GPIO.output(self.m2_pins["backward"], GPIO.HIGH)
      for i in range(num_loops):
         self.pulse_pwm()
         time.sleep(0.1)
      self.pulse_pwm(0)

   def turn_left(self, exec_time):
      exec_time = min(exec_time, self.max_time)
      sleep_time = 0.1
      num_loops = int(10*exec_time)
      GPIO.output(self.m1_pins["forward"], GPIO.LOW)
      GPIO.output(self.m1_pins["backward"], GPIO.HIGH)
      GPIO.output(self.m2_pins["forward"], GPIO.HIGH)
      GPIO.output(self.m2_pins["backward"], GPIO.LOW)
      for i in range(num_loops):
         self.pulse_pwm()
         time.sleep(0.1)
      self.pulse_pwm(0)

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

   mc = MotorController(m1_pins, m2_pins)
   mc.go_forward(1.5)
   mc.go_backward(1.5)
   mc.turn_right(1.5)
   mc.turn_left(1.5)

   GPIO.cleanup()
