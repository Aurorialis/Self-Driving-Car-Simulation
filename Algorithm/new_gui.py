##################
## gui.py
##      Simple animation to display self-driving car simulation
##      Uses points as cars, and circles for intersections
##
##      Austin Chun
##################


from tkinter import *
import time
import random


class GUI():

    INTERSECTION_RADIUS = 5
    CAR_RADIUS = 2

    # rows: # of horizontal lanes
    # cols: # of vertical lanes
    # width: of window in pixels
    # height: of window in pixels
    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height


        self.numCars = rows + cols # one car per lane

        # Flags for tkinter buttons
        self.startFlag = False
        self.notQuit = True

        # Initialize window
        self.tk = Tk()
        self.w = Canvas(self.tk, width=width, height=height)
        self.tk.title("Self Driving Car Simulation")
        self.w.pack()
        # Buttons
        self.start = Button(self.tk, text="Start", command=self.startCall)
        self.start.pack()
        self.pause = Button(self.tk, text="Pause", command=self.pauseCall)
        self.pause.pack()
        self.quit = Button(self.tk, text="Quit", command=self.quitCall)
        self.quit.pack()

        # Create gridlines
        rowSpacing = height/(rows+1)
        colSpacing = width/(cols+1)
        self.rowSpacing = rowSpacing
        self.colSpacing = colSpacing

        self.intPos = []
        self.intersectionHandles = [] # indexes for objects in tkinter
        for row in range(1,rows+1):
            for col in range(1,cols+1):
                self.intPos += [col*colSpacing, row*rowSpacing]

                self.intersectionHandles += [self.w.create_oval(
                    col*colSpacing - self.INTERSECTION_RADIUS, row*rowSpacing - self.INTERSECTION_RADIUS,
                    col*colSpacing + self.INTERSECTION_RADIUS, row*rowSpacing + self.INTERSECTION_RADIUS,
                    outline='grey',dash=(2,2),fill='white')]

        # Crossword ordering
        for row in range(1,rows+1):
            self.w.create_line(0, row*rowSpacing, width, row*rowSpacing)
        for col in range(1,cols+1):
            self.w.create_line(col*colSpacing, 0, col*colSpacing, height)


        # Dictionary for car objects (in reality, just indexes as objects in self.w)
        # Crossword ordering
        self.cars = {}
        # Dictionary of car positions in 1D (since restricted to linear motion
        self.carPos = {}
        for i in range(cols):
            # Start at top edge
            self.carPos[i] = 0
            # create_oval(x0, y0, x1, y1) as top-left and bottom-right corners
            self.cars[i] = self.w.create_oval((i+1)*colSpacing-self.CAR_RADIUS, -self.CAR_RADIUS,
                                              (i+1)*colSpacing+self.CAR_RADIUS, +self.CAR_RADIUS,
                                              fill='blue')

        for i in range(rows):
            # Start on left edge
            self.carPos[i+cols] = 0
            self.cars[i+cols] = self.w.create_oval(-self.CAR_RADIUS, (i+1)*rowSpacing-self.CAR_RADIUS,
                                                   +self.CAR_RADIUS, (i+1)*rowSpacing+self.CAR_RADIUS,
                                                   fill='blue')

        # White background
        self.w.configure(background='white')
        # Show GUI
        self.tk.update()

    def startCall(self):
        if not self.startFlag:
            self.startFlag = True
    def pauseCall(self):
        if self.startFlag:
            self.startFlag = False
    def quitCall(self):
        print("Quit")
        self.notQuit = False
        # self.tk.destroy()

    def animate(self, carPositions):
        # if self.startFlag:
        for i in range(self.numCars):
            self.moveCar(i, carPositions[i])

    def moveCar(self, carNum, pos): # Note: 1D position, determine direction from carNum
        if carNum < self.cols:
            self.w.move(self.cars[carNum], 0, (pos - self.carPos[carNum]))
            self.carPos[carNum] += pos - self.carPos[carNum]
        elif carNum < self.cols + self.rows:
            self.w.move(self.cars[carNum], (pos - self.carPos[carNum]), 0)
            self.carPos[carNum] += pos - self.carPos[carNum]
        else:
            print("ERROR: Invalid Car index, %d" %carNum)


    def checkCollision(self):
        collisionExists = False

        # Loop through intersections indexes
        for inter in range( self.rows*self.cols ):
            # Set fill to default
            self.w.itemconfig(self.intersectionHandles[inter], fill='white')
            # Check col car
            colCar = inter % self.cols # index of the column car
            colCarPos = self.carPos[colCar] # position of column car
            interRow = (inter // self.cols) + 1

            if( abs(colCarPos - interRow*self.rowSpacing) < self.INTERSECTION_RADIUS ):
                # Check row car
                rowCar = (inter // self.cols) + self.cols
                rowCarPos = self.carPos[rowCar]
                interCol = (inter % self.cols) + 1 # what column is this intersection


                if( abs(rowCarPos - interCol*self.colSpacing) < self.INTERSECTION_RADIUS):
                    # Set color to red!
                    self.w.itemconfig(self.intersectionHandles[inter], fill='red')
                    collisionExists = True

        if(collisionExists):
            time.sleep(0.02)
                    # print("")
                    # print("Inter: ",inter)
                    # print("Row car: ", rowCar)
                    # print("Row car pos: ", rowCarPos, "Row int: ", interRow*self.rowSpacing)
                    # print("Col car: ", colCar)
                    # print("Col car pos: ", colCarPos, "Col int: ", interCol*self.colSpacing)

                    # time.sleep(1)


###############
# Test Script #
###############


# NUM_ROWS = 5
# NUM_COLS = 8
# NUM_CARS = NUM_ROWS + NUM_COLS
# WINDOW_WIDTH = 600
# WINDOW_HEIGHT = 300

# carPos = [0]*NUM_CARS


# def generateMoves(carPos):

#     for i in range(NUM_CARS):
#         carPos[i] += (random.randint(1,4)+ i%2)
#         # print(carPos[i][0])
#         if(i < NUM_COLS):
#             carPos[i] = carPos[i] % WINDOW_HEIGHT
#         else:
#             carPos[i] = carPos[i] % WINDOW_WIDTH
#     # print(carPos)
#     return carPos



# g = GUI(NUM_ROWS,NUM_COLS,WINDOW_WIDTH,WINDOW_HEIGHT)
# while True:
#     if g.notQuit:
#         if g.startFlag:
#             carPos = generateMoves(carPos)
#             g.animate(carPos)
#             g.checkCollision()

#         g.tk.update_idletasks()
#         g.tk.update()
#         time.sleep(0.02)
#     else:
#         g.tk.destroy()
#         break
# print("Closed GUI")

# g.tk.mainloop()
