"""
    env.py

    Implement the environment (real-world values)

"""
# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=R0902

from time import time
from car import Car

class Env():

    def __init__(self, width, height):

        # Environment window dimensions (in meters)
        self.width = width
        self.height = height


        self.cars = [] # List of car objects
        self.cars += Car(0, 0)
        self.cars += Car(5, 5)

        self.cur_t = time()
        self.prev_t = time()

    def 


    def update(self):
        """ Update the simulation"""

        self.prev_t = self.cur_t
        self.cur_t = time()
        dt = self.cur_t - self.prev_t

        for car in self.cars:
            car.update(dt)

