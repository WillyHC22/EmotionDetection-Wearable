import time
import RPi.GPIO as GPIO

## WITHOUT THREADING

class MovementControl():
    
    def __init__(self, args):
        self.args = args

        self.pin1 = args["servo_pin1"]
        self.pin2 = args["servo_pin2"]
        self.pin3 = args["servo_pin3"]
        self.pin4 = args["servo_pin4"]

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.pin1, GPIO.OUT)
        self.servo1 = GPIO.PWM(self.pin1, 50)
        GPIO.setup(self.pin2, GPIO.OUT)
        self.servo2 = GPIO.PWM(self.pin2, 50)
        GPIO.setup(self.pin3, GPIO.OUT)
        self.servo3 = GPIO.PWM(self.pin3, 50)
        GPIO.setup(self.pin4, GPIO.OUT)
        self.servo4 = GPIO.PWM(self.pin4, 50)


    def start_servo(self):
        init_duty = self.args["init_duty"] ## set to 0 by default

        self.servo1.start(init_duty)
        self.servo2.start(init_duty)
        self.servo3.start(init_duty)
        self.servo4.start(init_duty)


    def stop_servo(self):
        self.servo1.stop()
        self.servo2.stop()
        self.servo3.stop()
        self.servo4.stop()

        GPIO.cleanup()


    def rotation(self, angle, speed):
        duty = (1./18.)*angle + 2.
        self.servo1.ChangeDutyCycle(duty)
        self.servo2.ChangeDutyCycle(duty)
        self.servo3.ChangeDutyCycle(duty)
        self.servo4.ChangeDutyCycle(duty)
        if speed == "slow":
            time.sleep(0.05)
        elif speed == "medium":
            time.sleep(0.02)
        elif speed == "fast": 
            time.sleep(0.01)


    def Sadness(self):
        self.start_servo()
        print("You look sad... ):")
        # The -120 should depend on positioning. 
        for angle in range(120):
            self.rotation(angle, "slow")
        self.stop_servo()
        

    def Happy(self):
        self.start_servo()
        print("You look happy ! =)")
        for angle in range(120):
            self.rotation(angle, "medium")
        self.stop_servo()


    def Anger(self):
        self.start_servo()
        print("You look angry !")
        # TO-DO : Add trembling
        for angle in range(40):
            self.rotation(angle, "fast")
        self.stop_servo()
