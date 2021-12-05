import time
import RPi.GPIO as GPIO


class TestMovementControl():

    def __init__(self):
        pass

    def AngerTest(self):
        print("You look angry !")
        time.sleep(2)

    def SadnessTest(self):
        print("You look sad...")
        time.sleep(2)

    def HappyTest(self):
        print("You look happy.")
        time.sleep(2)

class TestMovementControl_1():

    def __init__(self, args):
        self.args = args

        self.pin1 = args["servo_pin1"]

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.pin1, GPIO.OUT)
        self.servo1 = GPIO.PWM(self.pin1, 50)

    def start_servo(self):
        init_duty = self.args["init_duty"] ## set to 0 by default

        self.servo1.start(init_duty)
        print("Connecting succesful !")


    def stop_servo(self):
        self.servo1.stop()

        GPIO.cleanup()


    def rotation(self, angle, speed):
        duty = (1./18.)*angle + 2.
        self.servo1.ChangeDutyCycle(duty)
        if speed == "slow":
            time.sleep(0.1)
        elif speed == "medium":
            time.sleep(0.015)
        elif speed == "fast": 
            time.sleep(0.01)
    

    def tremble(self, angle, depth, interval, inverse=False):
        """Add trembling for anger; Interval should be higher than depth"""
        #Create index for trembling
        if angle % interval == 0:
            L = [i for i in range(depth+1)]
            indexes = L[1:depth] + L[::-1]
            if inverse:
                for index in indexes :
                    self.rotation(angle+index, "fast")
            else:
                for index in indexes :
                    self.rotation(angle-index, "fast")
            

    def Sadness(self):
        self.start_servo()
        print("You look sad... ):")

        # The -120 should depend on positioning. 

        for angle in range(120):
            self.rotation(angle, "slow")
        # L = [i for i in range(120)]
        # L = L[::-1]
        # for angle in L:
        #     self.rotation(angle, "slow")

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

        depth = self.args["depth"]
        interval = self.args["interval"]
        for angle in range(40):
            self.rotation(angle, "fast")
            #Add trembling
            self.tremble(angle, depth, interval)
        self.stop_servo()
