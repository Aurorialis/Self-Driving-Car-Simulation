# main.py
#   Piece together the different pieces for the simulation
#   
#   
#   Austin Chun
#   July 24 2018

from gui import GUI
from env import Env
from alg import Alg

import numpy as np
import time

def main():
    NUM_ROWS = 3
    NUM_COLS = 3
    NUM_CARS = NUM_ROWS + NUM_COLS
    WINDOW_WIDTH = 50          # meters
    WINDOW_HEIGHT = 50         # meters
    CAR_R = 2.5                 # meters (typical car is 5 m long, so radius is 2.5 m)

    # Initialzie Environment
    env = Env(NUM_ROWS, NUM_COLS, WINDOW_WIDTH, WINDOW_HEIGHT, CAR_R)

    # Initialize GUI
    g = GUI(NUM_ROWS,NUM_COLS,WINDOW_WIDTH,WINDOW_HEIGHT, CAR_R)

    # Initialize decision algorithm
    alg = Alg(NUM_ROWS, NUM_COLS, WINDOW_WIDTH, WINDOW_HEIGHT, CAR_R)

    curTime = 0

    while g.notQuit:
        if(g.startFlag):



            # Use algorithm to determine actions (based on current state)
            action = alg.act( env.getState() )

            # Take a step in the simulation
            env.step(action)

            # if(env.collisionCheck()):
            env.collisionCheck()
            g.highlightCollision(env.collisions)


            # Update gui with car positions
            state = env.getState()
            # print(state[0,:])


            g.animate( env.getCarPoses() )


            # print("Cur time:",round(curTime,3))
            curTime += 0.02

            if(curTime % 1.0 < 0.02):
                print("CurTime %.3f" %curTime)
                print("  Car 0: %.2f, %.2f" %(state[0,0], state[0,1]))

            time.sleep(0.02)


        g.update()

    g.exit()

    print("Exited")

if __name__ == '__main__':
    main()