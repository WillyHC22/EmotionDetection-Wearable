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
