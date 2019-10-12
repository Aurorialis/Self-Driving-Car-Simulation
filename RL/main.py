# main.py
#   Piece together the different pieces for the simulation
#   
#   
#   Austin Chun
#   July 24 2018

from gui import GUI
from env import Env
from alg import Alg_perCar, Alg_allCars

import numpy as np
import time

NUM_ROWS = 3    
NUM_COLS = 3
NUM_CARS = NUM_ROWS + NUM_COLS
WINDOW_WIDTH = 50          # meters
WINDOW_HEIGHT = 50         # meters
CAR_R = 2.5                # meters (typical car is 5 m long, so radius is 2.5 m)
maxV = 18                  # meters/sec (18m/s = 40 mph) 

# RL stuff
iter_max = 100 # max num epsidoes 
initial_lr = 1.0
min_lr = 0.003
gamma = 1.0
j_max = 1000 # max timesteps in an episode


# USER FLAGS
render = False


def test(env, alg):
    # Initialize GUI
    g = GUI(NUM_ROWS,NUM_COLS,WINDOW_WIDTH,WINDOW_HEIGHT, CAR_R)
    # Reset environment (all cars back to start)
    env.reset()

    curTime = 0
    # Loop until exit
    while g.notQuit:
        if(g.startFlag):

            # Use algorithm to determine actions (based on current state)
            obs = env.getPV()
            action = alg.act( obs )

            # Take a step in the simulation (internally checks collisions)
            env.step(action)

            # update GUI with car poses, and highlght collisions
            g.animate( env.getP(), env.collisions)

            # print("Cur time:",round(curTime,3))
            curTime += 0.02

            if(curTime % 1.0 < 0.02):
                print("CurTime %.3f" %curTime)
                state = env.getPV()
                print("  Car 0: %.2f, %.2f" %(state[0,0], state[0,1]))

            time.sleep(0.02)

        g.update()

    g.exit()


###################
### RL Training ###
###################

# Initialize Environment
env = Env(NUM_ROWS, NUM_COLS, WINDOW_WIDTH, WINDOW_HEIGHT, CAR_R, maxV)
# Initialize decision algorithm
alg = Alg_perCar(NUM_ROWS, NUM_COLS, WINDOW_WIDTH, WINDOW_HEIGHT, CAR_R, maxV)
# alg = Alg_allCars(NUM_ROWS, NUM_COLS, WINDOW_WIDTH, WINDOW_HEIGHT, CAR_R, maxV)

if(render):
    # Initialize GUI
    g = GUI(NUM_ROWS,NUM_COLS,WINDOW_WIDTH,WINDOW_HEIGHT, CAR_R)

print("------ Q Learning -------")
# Run episodes many times
for i in range(iter_max):
    env.reset() # Reset environment
    total_reward = 0
    # eta: learning rate is decreased at each step
    eta = max(min_lr, initial_lr * (0.85 ** (i//100)))

    # Loop through timesteps of an episode
    for j in range(j_max):
        obs = env.getPV() # Take observation

        action, indexes = alg.act( obs ) # Calculate action based on observation
                                         # Internally, either random choice, or uses q_table

        reward, done = env.step( action ) # Take the step (return reward, and done flag)

        total_reward += reward # Keep track of reward

        newObs = env.getPV()
        alg.updateQTable(newObs, eta, reward, gamma)







print("Exited")
