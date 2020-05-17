import sys
import time
import RPi.GPIO as GPIO

class MotorController:
   def __init__(self, m1_pins, m2_pins, max_time=-1):
      self.max_time = max_time
      self.m1_pins = m1_pins
      self.m2_pins = m2_pins

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
      exec_time = max(exec_time, self.max_time)
      sleep_time = 0.1
      num_loops = int(exec_time/sleep_time)
      GPIO.output(self.m1_pins["forward"], GPIO.LOW)
      GPIO.output(self.m1_pins["backward"], GPIO.HIGH)
      GPIO.output(self.m2_pins["forward"], GPIO.LOW)
      GPIO.output(self.m2_pins["backward"], GPIO.HIGH)
      for i in range(num_loops):
         self.pulse_pwm()
         time.sleep(0.1)

   def go_backward(self, exec_time):
      exec_time = max(exec_time, self.max_time)
      sleep_time = 0.1
      num_loops = int(exec_time/sleep_time)
      GPIO.output(self.m1_pins["forward"], GPIO.HIGH)
      GPIO.output(self.m1_pins["backward"], GPIO.LOW)
      GPIO.output(self.m2_pins["forward"], GPIO.HIGH)
      GPIO.output(self.m2_pins["backward"], GPIO.LOW)
      for i in range(num_loops):
         self.pulse_pwm()
         time.sleep(0.1)

   def turn_right(self, exec_time):
      exec_time = max(exec_time, self.max_time)
      sleep_time = 0.1
      num_loops = int(exec_time/sleep_time)
      GPIO.output(self.m1_pins["forward"], GPIO.HIGH)
      GPIO.output(self.m1_pins["backward"], GPIO.LOW)
      GPIO.output(self.m2_pins["forward"], GPIO.LOW)
      GPIO.output(self.m2_pins["backward"], GPIO.HIGH)
      for i in range(num_loops):
         self.pulse_pwm()
         time.sleep(0.1)

   def turn_left(self, exec_time):
      exec_time = max(exec_time, self.max_time)
      sleep_time = 0.1
      num_loops = int(exec_time/sleep_time)
      GPIO.output(self.m1_pins["forward"], GPIO.LOW)
      GPIO.output(self.m1_pins["backward"], GPIO.HIGH)
      GPIO.output(self.m2_pins["forward"], GPIO.HIGH)
      GPIO.output(self.m2_pins["backward"], GPIO.LOW)
      for i in range(num_loops):
         self.pulse_pwm()
         time.sleep(0.1)

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

m1_forward  = 6
m1_backward = 12
m1_pwm_pin  = 18

m2_forward  = 19
m2_backward = 16
m2_pwm_pin  = 17

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m1_forward, GPIO.OUT)
GPIO.setup(m1_backward, GPIO.OUT)
GPIO.setup(m1_pwm_pin, GPIO.OUT)

GPIO.setup(m2_forward, GPIO.OUT)
GPIO.setup(m2_backward, GPIO.OUT)
GPIO.setup(m2_pwm_pin, GPIO.OUT)

m1_pi_pwm = GPIO.PWM(m1_pwm_pin, 100)
m1_pi_pwm.start(0)

m2_pi_pwm = GPIO.PWM(m2_pwm_pin, 100)
m2_pi_pwm.start(0)

print("moving the motors yaaaasss")

time.sleep(0.1)

#for _ in range(50):
#   GPIO.output(m1_forward, GPIO.LOW)
#   GPIO.output(m1_backward, GPIO.HIGH)
#   GPIO.output(m2_forward, GPIO.LOW)
#   GPIO.output(m2_backward, GPIO.HIGH)
#   m1_pi_pwm.ChangeDutyCycle(75)
#   m2_pi_pwm.ChangeDutyCycle(75)
#   time.sleep(0.1)
#print("Changing directions")
#for _ in range(50):
#   GPIO.output(m1_forward, GPIO.HIGH)
#   GPIO.output(m1_backward, GPIO.LOW)
#   GPIO.output(m2_forward, GPIO.HIGH)
#   GPIO.output(m2_backward, GPIO.LOW)
#   m1_pi_pwm.ChangeDutyCycle(75)
#   m2_pi_pwm.ChangeDutyCycle(75)
#   time.sleep(0.1)

mc = MotorController(m1_pins, m2_pins)
mc.go_forward(1.5)
mc.go_backward(1.5)
mc.turn_right(1.5)
mc.turn_left(1.5)

GPIO.cleanup()
