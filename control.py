import time
import RPi.GPIO as GPIO


class MovementControl():
    def __init__(self, servo):
        self.servo = servo
    def Anger(self):
        print("You look angry !")
    def Sadness(self):
        print("You look sad... ):")
    def Neutral(self):
        print("You look neutral.")
    def Happy(self):
        print("You look happy ! =)")
