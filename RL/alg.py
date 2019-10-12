# alg.py
#   The core decision algorithm to control cars
#   
#   Austin Chun
#   July 24 2018
#   

import numpy as np


class Alg_perCar():


    def __init__(self, rows, cols, width, height, CAR_R, maxV):
        self.ROWS = rows        # num rows (or horz cars)
        self.COLS = cols        # num cols (or vert cars)
        self.WIDTH = width      # width of window (meters)
        self.HEIGHT = height    # height of window (meters)
        self.CAR_R = CAR_R      # Size of car (meters) (nominal 5 m)
        self.maxV = maxV

        self.numCars = self.ROWS + self.COLS # one car per lane

        self.state = np.zeros((self.numCars, 2), dtype=int) # Pos,Vel for each car

        self.action = np.zeros(self.numCars) # Acceleration commands (m/s^2)
        self.actionIndex = np.zeros(self.numCars, dtype=int) # Index of chosen actions

        self.numPosStates = 50
        self.numVelStates = 20
        self.numActions = 2 # accelerate, decelerate

        self.chooseActions = [3.0, -7.0]    # [maxAcc, maxDec]

        self.eps = 0.02 # 2% chance of doing random action

        # Create Q table (Learns the approp action for givens tate) (numCars x (numStates) X numActions)
        # Total num states = numCars * numPosStates * numVelStates
        self.qTable = np.zeros((self.numCars, self.numPosStates, self.numVelStates, self.numActions))

        self.dx = self.WIDTH / self.numPosStates # Resolution of position
        self.dv = self.maxV / self.numVelStates  # Resolution of velocity



    def _obs2state(self, obs):
        # round pos and vel values to states
        state = np.empty((self.numCars, 2), int)
        for car in range(self.numCars):
            state[car,0] = int(obs[car,0]//self.dx)
            state[car,1] = int(obs[car,1]//self.dv)

        return state


    def act(self, obs):

        # Converts observation (cts) to state (discrete)
        self.state = self._obs2state(obs)

        for car in range(self.numCars):
            
            # Randomly choose an action
            if np.random.uniform(0, 1) < self.eps:
                self.actionIndex[car] = int(np.random.randint(self.numActions)) # Randomly choose action index
                self.action[car] = self.chooseActions[self.actionIndex[car]] # Store actual action
                # self.action[car] = np.random.choice(self.chooseActions)
            else:
                pos, vel = self.state[car]  # pos (and vel respectively) is integer from 0 to self.numPosStates
                
                logits = self.qTable[car,pos,vel]

                logits_exp = np.exp(logits)
                probs = logits_exp / np.sum(logits_exp)
                
                self.actionIndex[car] = int(np.random.choice(self.numActions, p=probs)) # Sample action (index) with prob dist
                self.action[car] = self.chooseActions[self.actionIndex[car]] # Store actual action
                # self.action[car] = np.random.choice(self.chooseActions, p=probs)


        # # self.action.fill(np.random.randint(-1,3))
        self.action = np.random.randint(-1,3,(6))
        return self.action, self.actionIndex

    def updateQTable(self, obs, eta, reward, gamma):
        """ 
        Update the Q table using Bellman equation
        """
        state_ = self._obs2state(obs)

        for car in range(self.numCars):
            pos_, vel_ = state_[car] # New pos and vel from recent action
            pos, vel = self.state[car]  # Old pos and vel before step
            action = self.actionIndex[car]

            # Bellman Equation
            self.qTable[car,pos,vel,action] = self.qTable[car,pos,vel,action] + eta * \
                        (reward + gamma * np.max( self.qTable[car,pos_,vel_] - self.qTable[car,pos,vel,action]) )


class Alg_allCars():
    """
    This algorithm considers the all cars at one time to determine action.
    State space is numCars*numPoses*numVels (6 * 50 * 20 = 6000 states)
    Actions, each car either acc/dec => 2^6 = 64 possible decisions
    """

    def __init__(self, rows, cols, width, height, CAR_R, maxV):
        self.ROWS = rows        # num rows (or horz cars)
        self.COLS = cols        # num cols (or vert cars)
        self.WIDTH = width      # width of window (meters)
        self.HEIGHT = height    # height of window (meters)
        self.CAR_R = CAR_R      # Size of car (meters) (nominal 5 m)
        self.maxV = maxV

        self.numCars = self.ROWS + self.COLS # one car per lane

        self.state = np.zeros((self.numCars, 2), int) # Pos,Vel for each car

        self.action = np.zeros(self.numCars) # Acceleration commands (m/s^2)
        self.actionIndex = np.zeros(self.numCars) # Index of chosen actions

        self.numPosStates = 50
        self.numVelStates = 20
        self.numActions = 2 # accelerate, decelerate

        self.chooseActions = [3.0, -7.0]    # [maxAcc, maxDec]

        self.eps = 0.02 # 2% chance of doing random action

        # Create Q table (Learns the approp action for givens tate) (numCars x (numStates) X numActions)
        # Total num states = numCars * numPosStates * numVelStates
        self.qTable = np.zeros((self.numCars, self.numPosStates, self.numVelStates, self.numActions))

        self.dx = self.WIDTH / self.numPosStates # Resolution of position
        self.dv = self.maxV / self.numVelStates  # Resolution of velocity


    def _obs2state(self, obs):
        # round pos and vel values to states
        state = np.empty((self.numCars, 2), int)
        for car in range(self.numCars):
            state[car,0] = int(obs[car,0]//self.dx)
            state[car,1] = int(obs[car,1]//self.dv)

        return state
