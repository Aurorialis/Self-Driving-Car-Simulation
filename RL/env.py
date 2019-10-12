# env.py
#   Hold all invormation of the current environment (all car positoons and velocities)
#   
#   Austin Chun
#   July 24 2018


import numpy as np

class Env():


    def __init__(self, rows, cols, width, height, CAR_R, maxV):
        self.ROWS = rows        # num rows (or horz cars)
        self.COLS = cols        # num cols (or vert cars)
        self.WIDTH = width      # width of window (meters)
        self.HEIGHT = height    # height of window (meters)
        self.CAR_R = CAR_R      # Size of car (meters) (nominal 5 m)

        self.numCars = self.ROWS + self.COLS # one car per lane


        # Create gridlines
        self.ROW_D = self.HEIGHT/(self.ROWS+1)  # Row spacing dist (m)
        self.COL_D = self.WIDTH/(self.COLS+1)   # Col spacing dist (m)

        self.maxV = maxV

        self.dt = 0.02  # seconds (50 Hz)

        # Matrix of each cars position (column 0), velocity (column 1), acc (columm 2)
        # Continuous (float) values
        self.carPVA = np.zeros((self.numCars, 3))
        self.dist = np.zeros(self.numCars)

        # Store intersection coordinates
        # Intersections indexed crossword
        self.intCoords = np.zeros((self.ROWS*self.COLS, 2))
        for row in range(1,self.ROWS+1):
            for col in range(1,cols+1):
                self.intCoords[row+col,:] = row*self.ROW_D , col*self.COL_D


        # Collision Flags, corresponding to intersection
        # Check for any 1's in array for collisions
        self.collisions = np.zeros((self.COLS, self.ROWS))
        self.COLLISION = False # Flag to indicate collision

        # Store crossroads y coordinates (so vert cars just need to check this)
        self.yCrossCoords = np.zeros(self.ROWS)
        for row in range(self.ROWS):
            self.yCrossCoords[row] = (row+1)*self.ROW_D
        # Store crossroads x coord
        self.xCrossCoords = np.zeros(self.COLS)
        for col in range(self.COLS):
            self.xCrossCoords[col] = (col+1)*self.COL_D


    def step(self, acc):
        """
        @brief      step the environment forward one step
        
        @param      acc   A np vector of accelerations for each cat

        @return     reward, and done flag (collision flag)
        """
        # Load new Accelerations
        self.carPVA[:,2] = acc

        # Kinematics
        self.dist += self.carPVA[:,1]*self.dt

        self.carPVA[:,0] += self.carPVA[:,1]*self.dt
        self.carPVA[:,1] += self.carPVA[:,2]*self.dt


        for car in range(self.numCars):
            # Bound Position (within window)
            pos = self.carPVA[car,0]
            # Vert cars
            if(car < self.COLS):
                if(pos > self.HEIGHT):
                    self.carPVA[car,0] = pos % self.HEIGHT
            # Horz cars
            else:
                if(pos > self.WIDTH):
                    self.carPVA[car,0] = pos % self.WIDTH

            # Bound Velocity (0 to maxVelocity)
            vel = self.carPVA[car,1]
            if(vel > self.maxV):
                self.carPVA[car,1] = self.maxV
            elif(vel < 0):
                self.carPVA[car,1] = 0



        self._collisionCheck()

        return self._reward(), self.COLLISION

        # self.carPVA[0:self.COLS,0] = [x%self.HEIGHT for x in self.carPVA[0:self.COLS,0] if x>self.HEIGHT]
        # self.carPVA[self.COLS:self.COLS+self.ROWS,0] = \
        #                 [x%self.WIDTH for x in self.carPVA[self.COLS:self.COLS+self.ROWS,0] if x>self.WIDTH]



    def _reward(self):
        """
        Define reward system:
            +1 for every meter
            -1000 for every collision
        """
        return np.sum(self.dist) - 1000.0*np.count_nonzero(self.collisions)



    def _collisionCheck(self):
        """
        @brief      Checks for collisions 
              
        @return     Populates self.collisions with 1 where there is a collision, and returns bool if there was a collision
        """

        # Occupied intersections 
        occInts = np.zeros((self.ROWS,self.COLS)) # Count how many cars in each intersection
        COLLISION = False # Flag
        self.collisions.fill(0)

        for car in range(self.COLS):
            # get pos (just y, since x is fixed based on track num)
            carPos = self.carPVA[car][0] 
            # Check crossing intersections (just y coords)
            for yCoord in self.yCrossCoords:
                if (carPos > yCoord-self.CAR_R) and (carPos < yCoord+self.CAR_R):
                    row = int(yCoord/self.ROW_D - 1)
                    # increment occupant num for intersection
                    occInts[row,car] = 1

        for car in range(self.ROWS):
            # get pos (make sure car num indexing is correct, add offset from vertCars)
            carPos = self.carPVA[car+self.COLS][0] 
            # Check crossing intersections (just x coords)
            for xCoord in self.xCrossCoords:
                if (carPos > xCoord-self.CAR_R) and (carPos < xCoord+self.CAR_R):
                    col = int(xCoord/self.COL_D - 1)
                    # Raise Collision flag for that intersection
                    if(occInts[car,col] == 1):
                        # If just collided
                        if(not self.COLLISION):
                            print("COLLISON!!!")
                            self.COLLISION = True
                            COLLISION = True
                        # Set collisins
                        self.collisions[car,col] = 1
                        print(" Collision at: (%d,%d)" %(car,col))
        

        self.COLLISION = COLLISION # gets false if no collisions in

        return self.COLLISION

    def getP(self):
        return self.carPVA[:,0]
    def getPV(self):
        return self.carPVA[:,0:2]
    def getPVA(self):
        return self.carPVA


    def reset(self):
        """
        Reset the environment (the car PVA, and collision map)
        """
        self.carPVA.fill(0)
        self.collisions.fill(0)

