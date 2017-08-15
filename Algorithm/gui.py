##################
## gui.py
##      Simple animation to display self-driving car simulation
##
##      Austin Chun
##################


from tkinter import *
import time
import random



class GUI():

    firstCarIndex = 7
    overlaps = []
    # Class constants
    CAR_LENGTH = 10
    CAR_WIDTH = 6


    # class guiCar():
    #     def __init__(self, ID, direction, initPosX, initPosY,):
    #         self.ID = ID
    #         self.direction = direction # 0 = Vertical, 1 = Horizontal
    #         # Upper left corner
    #         self.x = initPosX
    #         self.y = initPosY



    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height

        self.numCars = rows + cols

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


        for row in range(1,rows+1):
            self.w.create_line(0, row*rowSpacing, width, row*rowSpacing)
        for col in range(1,cols+1):
            self.w.create_line(col*colSpacing, 0, col*colSpacing, height)


        # Dictionary for car objects (in reality, just indexes as objects in self.w)
        self.cars = {}
        # Dictionary of car positions (center of body)
        self.carPos = {}
        for i in range(cols):
            self.carPos[i] = 0
            self.cars[i] = self.w.create_rectangle(
                                (i+1)*colSpacing-GUI.CAR_WIDTH/2, self.carPos[i]-GUI.CAR_LENGTH+GUI.CAR_WIDTH,
                                (i+1)*colSpacing+GUI.CAR_WIDTH/2, self.carPos[i]+GUI.CAR_WIDTH,
                                fill='blue')

        for i in range(rows):
            self.carPos[i+cols] = 0
            self.cars[i+cols] = self.w.create_rectangle(
                                self.carPos[i+cols]-GUI.CAR_LENGTH+GUI.CAR_WIDTH, (i+1)*rowSpacing-GUI.CAR_WIDTH/2,
                                self.carPos[i+cols]+GUI.CAR_WIDTH, (i+1)*rowSpacing+GUI.CAR_WIDTH/2,
                                fill='blue')

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


    # def move(self):
    #     if self.startFlag:
    #         inc = 2
    #     else:
    #         inc = 0

    #     for col in range(self.cols):
    #         if(self.w.coords(self.cars[col])[1] >= self.height):
    #             self.w.move(self.cars[col], 0, -(self.height+self.CAR_LENGTH))
    #             self.carPos[col] -= self.height+self.CAR_LENGTH
    #         self.w.move(self.cars[col], 0, inc)

    #         self.carPos[col] += inc


    #     for row in range(self.rows):
    #         if(self.w.coords(self.cars[row+self.cols])[0] >= self.width):
    #             self.w.move(self.cars[row+self.cols], -(self.width+self.CAR_LENGTH), 0)
    #             self.carPos[row+self.cols] -= (self.width+self.CAR_LENGTH)
    #         self.w.move(self.cars[row+self.cols], inc, 0)

    #         self.carPos[row+self.cols] += inc


    def animate(self, carPositions):
        # if self.startFlag:
        for i in range(self.numCars):
            self.moveCar(i, carPositions[i][0])

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
        # global firstCarIndex
        # global overlaps
        for col in range(self.cols):
            coords = self.w.coords(self.cars[col])
            ov = self.w.find_overlapping(coords[0], coords[1], 
                                               coords[2], coords[3])

            ov = [car for car in ov if car >= GUI.firstCarIndex]
            if(len(ov) > 1):
                for car in ov:
                    if car not in GUI.overlaps:
                        GUI.overlaps += ov

        for car in range(GUI.firstCarIndex, GUI.firstCarIndex+len(self.cars)):
            if car in GUI.overlaps:
                self.w.itemconfig(car, fill='red')
            else:
                self.w.itemconfig(car, fill='blue')
       
        # Reset collision list
        GUI.overlaps = []



###############
# Test Script #
###############

# NUM_CARS = 6
# WINDOW_WIDTH = 400
# WINDOW_HEIGHT = 300

# carPos = [[0],[0],[0],[0],[0],[0]]
# def generateMoves(carPos):

#     for i in range(NUM_CARS):
#         carPos[i][0] += (random.randint(1,4)+ i%2)
#         # print(carPos[i][0])
#         if(i < 3):
#             carPos[i][0] = carPos[i][0] % WINDOW_HEIGHT
#         else:
#             carPos[i][0] = carPos[i][0] % WINDOW_WIDTH
#         # print(carPos)
#     return carPos



# g = GUI(3,3,WINDOW_WIDTH,WINDOW_HEIGHT)
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
