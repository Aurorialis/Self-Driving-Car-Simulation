# alg.py
#   The core decision algorithm to control cars
#   
#   Austin Chun
#   July 24 2018
#   

import numpy as np


class Alg():


    def __init__(self, rows, cols, width, height, CAR_R):
        self.ROWS = rows        # num rows (or horz cars)
        self.COLS = cols        # num cols (or vert cars)
        self.WIDTH = width      # width of window (meters)
        self.HEIGHT = height    # height of window (meters)
        self.CAR_R = CAR_R      # Size of car (meters) (nominal 5 m)

        self.numCars = self.ROWS + self.COLS # one car per lane

        self.action = np.zeros(self.numCars)

    def act(self, state):
        # self.action.fill(np.random.randint(-1,3))
        self.action = np.random.randint(-1,3,(6))
        return self.action