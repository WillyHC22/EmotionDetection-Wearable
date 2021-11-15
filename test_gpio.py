import time
from utils.parser import get_parser
import RPi.GPIO as GPIO

##Testing GPIO
args = get_parser()
servo_pin = args["servo_pin"]
#servo_pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50)

print('Connecting to servo')
servo.start(0)

duty = 2

time_sleep = args["time_sleep"]


if args["stabilize"]:
    #Test stabilize
    while duty <= 12:
        servo.ChangeDutyCycle(duty)
        time.sleep(0.3)
        servo.ChangeDutyCycle(0)
        time.sleep(0.7)
        duty += 1
else:
    while duty <= 12:
        servo.ChangeDutyCycle(duty)
        time.sleep(time_sleep)
        duty += 1

print("Reset position")
servo.ChangeDutyCycle(2)
time.sleep(2)

servo.stop()
GPIO.cleanup()
print("End of process")