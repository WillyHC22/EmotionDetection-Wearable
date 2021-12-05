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

        self.nrep = args["repetition"]
        self.depth = args["depth"]
        self.interval = args["interval"]

        GPIO.cleanup()

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
            time.sleep(0.1)
        elif speed == "medium":
            time.sleep(0.015)
        elif speed == "fast": 
            time.sleep(0.01)
    

    def tremble(self, angle, depth, interval):
        """Add trembling for anger; Interval should be higher than depth"""
        #Create index for trembling
        if angle % interval == 0:
            L = [i for i in range(depth+1)]
            indexes = L[1:depth] + L[::-1]
            for index in indexes :
                self.rotation(angle-index, "fast")


    def Sadness(self):
        self.start_servo()
        print("You look sad... ):")

        #
        for _ in range(self.nrep):
            for angle in range(120):
                self.rotation(angle, "slow")

            L = [i for i in range(120)]
            L = L[::-1]
            for angle in L:
                self.rotation(angle, "slow")

        self.stop_servo()
        

    def Happy(self):
        self.start_servo()
        print("You look happy ! =)")

        for _ in range(self.nrep):
            for angle in range(120):
                self.rotation(angle, "medium")

            L = [i for i in range(120)]
            L = L[::-1]
            for angle in L:
                self.rotation(angle, "medium")

        self.stop_servo()


    def Anger(self):
        self.start_servo()
        print("You look angry !")

        for _ in range(self.nrep):

            for angle in range(40):
                self.rotation(angle, "fast")
                #Add trembling
                self.tremble(angle, self.depth, self.interval)

            L = [i for i in range(40)]
            L = L[::-1]
            for angle in L:
                self.rotation(angle, "fast")
                self.tremble(angle, self.depth, self.interval, reverse = True)

        self.stop_servo()

#==============================================================================================
#==============================================================================================
#==============================================================================================
# Testing with the moving function
#==============================================================================================
#==============================================================================================
#==============================================================================================

    def servo_moving(self, angle_max, speed, with_tremble = False):
        
        #nrep is the number of back and forth done by the servo
        for _ in range(self.nrep):
            for angle in range(angle_max):
                self.rotation(angle, speed)
                if with_tremble:
                    self.tremble(angle, self.depth, self.interval)

            reverse_angles = [i for i in range(120)]
            reverse_angles = reverse_angles[::-1]
            for angle in reverse_angles:
                self.rotation(angle, speed)
                if with_tremble:
                    self.tremble(angle, self.depth, self.interval, reverse = True)


    def Sadness_move(self):
        self.start_servo()
        print("You look sad... =(")

        self.servo_moving(120, "slow", with_tremble = False)

        self.stop_servo()
        

    def Happy_move(self):
        self.start_servo()
        print("You look happy ! =)")

        self.servo_moving(120, "medium", with_tremble = False)

        self.stop_servo()


    def Anger_move(self):
        self.start_servo()
        print("You look angry ! è_é")

        self.servo_moving(40, "fast", with_tremble = True)

        self.stop_servo()