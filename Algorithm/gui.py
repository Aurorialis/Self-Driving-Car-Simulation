##################
## gui.pu
##      Simple animation to display self-driving car simulation
##
##      Austin Chun
##################


from tkinter import *
import time
import random

class GUI():

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
        self.start = Button(self.tk, text="Start", command=self.startCall)
        self.start.pack()
        self.pause = Button(self.tk, text="Pause", command=self.pauseCall)
        self.pause.pack()
        self.q = Button(self.tk, text="Quit", command=self.quitCall)
        self.q.pack()

        # Create gridlines
        rowSpacing = height/(rows+1)
        colSpacing = width/(cols+1)
        for row in range(1,rows+1):
            self.w.create_line(0, row*rowSpacing, width, row*rowSpacing)
        for col in range(1,cols+1):
            self.w.create_line(col*colSpacing, 0, col*colSpacing, height)

        # Initialize cars
        carWidth = 10
        carHeight = 15
        self.carWidth = carWidth
        self.carHeight = carHeight

        self.cars = []
        for i in range(cols):
            # carDict["car"+str(i)] = w.create_rectangle(
            self.cars.append(self.w.create_rectangle(
                                (i+1)*colSpacing-carWidth/2, 0,
                                (i+1)*colSpacing+carWidth/2, carHeight,
                                fill='blue'))
        for i in range(rows):
            # carDict["car"+ str(i+cols)] = w.create_rectangle(
            self.cars.append(self.w.create_rectangle(
                                0, (i+1)*rowSpacing+carWidth/2,
                                carHeight, (i+1)*rowSpacing-carWidth/2,
                                fill='red'))

    
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


    def move(self):
        if self.notQuit:
            if self.startFlag:
                inc = 2
            else:
                inc = 0

            for col in range(self.cols):
                if(self.w.coords(self.cars[col])[1] >= self.height):
                    self.w.move(self.cars[col], 0, -(self.height+self.carHeight))
                # print(self.w.coords(self.cars[col])[3])
                self.w.move(self.cars[col], 0, inc)
            for row in range(self.rows):
                if(self.w.coords(self.cars[self.cols+row])[0] >= self.width):
                    self.w.move(self.cars[self.cols+row], -(self.width+self.carHeight), 0)
                self.w.move(self.cars[self.cols+row], inc, 0)
            self.tk.update()




g = GUI(3,3,600,400)
g.tk.update()

# print(g.startFlag)
# while not g.startFlag:
    # print('.',end='')
    
while True:
    # time.sleep(0.01)
    if g.notQuit:
        g.move()
        time.sleep(0.01)
    else:
        g.tk.destroy()
        break
print("Closed GUI")
g.tk.mainloop()
