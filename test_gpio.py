import time
import RPi.GPIO as GPIO

##Testing GPIO

servo_pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50)

print('Connecting to servo')
servo.start(0)

duty = 2

while duty <= 12:
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    duty += 1

    ##Test stabilize
    # servo.ChangeDutyCycle(duty)
    # time.sleep(0.3)
    # servo.ChangeDutyCycle(0)
    # time.sleep(0.7)
    # duty += 1

print("Reset position")
servo.ChangeDutyCycle(2)
time.sleep(2)

servo.stop()
GPIO.cleanup()
print("End of process")