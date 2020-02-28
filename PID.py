# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 22:52:06 2020

@author: iainr
"""

# import necessary packages
import time
from threading import Thread

class PID:
    def __init__(self, kP=1, kI=0, kD=0):
        # initialize gains
        self.kP = kP
        self.kI = kI
        self.kD = kD
        # initialize the current and previous time
        self.prevTime = self.currTime
		# initialize the previous error
        self.prevError = 0
		# initialize the term result variables
        self.cP = 0
        self.cI = 0
        self.cD = 0
        
    def start(self):
		# start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self
        
    def update(self, error, sleep=0.2):
		# pause for a bit
        time.sleep(sleep)
		# grab the current time and calculate delta time
        self.currTime = time.time()
        deltaTime = self.currTime - self.prevTime
		# delta error
        deltaError = error - self.prevError
		# proportional term
        self.cP = error
		# integral term
        self.cI += error * deltaTime
		# derivative term and prevent divide by zero
        self.cD = (deltaError / deltaTime) if deltaTime > 0 else 0
		# save previous time and error for the next update
        self.prevtime = self.currTime
        self.prevError = error
		# sum the terms and return
        return sum([
            self.kP * self.cP,
            self.kI * self.cI,
            self.kD * self.cD])