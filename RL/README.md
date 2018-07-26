#########################################
### Self-Driving-Car (SDC) Simulation ###
#########################################

This simulation is intended to illustrate how self-driving-cars can improve the efficiency of intersections.

The simulation is setup like a city street grid, with one-way one-lane streets. All cars are autonomous, except for
a single user controlled car. User car can be malicious and try create an accident, but with the autonomous cars 
communicating with one another, knowing their own positon and others', all collisions will be avoided.

Dependencies
------------
- Tkinter
- numpy


Development details
-------------------
- Crossword Indexing
- Cars are modelled as points, with intersections as circles
    - Intersection radius effectively dictates size of the cars, or the collision area
- Car position defined in 1D
    - Since restricted to linear motion, always know the x (or y) for the car, so only care about the degree of freedom
- GUI Interfacing
    - At every timestep, takes in the POSITION of all cars
    - Initialize GUI with:
        > g = GUI(NUM_ROWS,NUM_COLS,WINDOW_WIDTH,WINDOW_HEIGHT, INT_R=INT_R, CAR_R=CAR_R)
    - Wrap algorithm in while loop that updates Tkinter GUI
    ```
        while True:
            if g.notQuit:
                if g.startFlag:
                    carPos = generateMoves(carPos)
                    g.animate(carPos)
                    g.checkCollision()

                g.tk.update_idletasks()
                g.tk.update()
                time.sleep(0.02)
            else:
                g.tk.destroy()
                break
    ```
- Coordinates in (x,y) with (0,0) as top-left, and x going right, y going down




