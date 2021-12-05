import time
from utils.argparser import get_parser
import RPi.GPIO as GPIO

##Testing GPIO
args = get_parser()
servo_pin1 = args["servo_pin1"]
servo_pin2 = args["servo_pin2"]
servo_pin3 = args["servo_pin3"]
servo_pin4 = args["servo_pin4"]


GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo_pin1, GPIO.OUT)
servo1 = GPIO.PWM(servo_pin1, 50)
GPIO.setup(servo_pin2, GPIO.OUT)
servo2 = GPIO.PWM(servo_pin2, 50)
GPIO.setup(servo_pin3, GPIO.OUT)
servo3 = GPIO.PWM(servo_pin3, 50)
GPIO.setup(servo_pin4, GPIO.OUT)
servo4 = GPIO.PWM(servo_pin4, 50)


print('Connecting to servo1')
servo1.start(0)
servo2.start(0)
servo3.start(0)
servo4.start(0)


duty = 2

time_sleep = args["time_sleep"]


while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    servo2.ChangeDutyCycle(duty)
    servo3.ChangeDutyCycle(duty)
    servo4.ChangeDutyCycle(duty)
    time.sleep(time_sleep)
    duty += 1

print("Reset position")
servo1.ChangeDutyCycle(2)
servo2.ChangeDutyCycle(2)
servo3.ChangeDutyCycle(2)
servo4.ChangeDutyCycle(2)
time.sleep(2)

servo1.stop()
servo2.stop()
servo3.stop()
servo4.stop()

GPIO.cleanup()
print("End of process")