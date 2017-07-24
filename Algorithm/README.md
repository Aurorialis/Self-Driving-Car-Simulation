Self Driving Car Simulation
---------------------------

by Aurora Leeson and Austin Chun
July 2017


Dependencies
------------
Python (2.7 or 3.5?)


Interface with GUI
------------------
Full example:
    g = GUI(3,3,600,400)
    # Loop until quit 
    while True:
        ################
        # Do lots of calculations
        # Produce carPositions
        ################

        if g.notQuit: # Make sure the gui hasn't been quit
            g.move(carPositions) # Update car positions
            # carPositions = [(pos1, vel1, acc1), (pos2, vel2, acc2), ... ,(posN, velN, accN)]
            
            g.checkCollision()
            
            # Let GUI update
            g.tk.update_idletasks() 
            g.tk.update()
            time.sleep(0.02)
        
        else: # Close GUI gracefully
            g.tk.destroy()
            break


- Initialize GUI object, with corresponding parameters
> g = GUI(<rows>, <cols>, <width>, <height>)
rows, cols = number of horizontal/vertical roads
width, height = platform dimensions (in cm? in? whatever) (I'll convert those to pixels to make it look right)

- While loop call
> while True:
    - Main calculation loop
    - I imagine all of the calculations will be done here

- g.move(carPositions)
    -Updates the car positions for the GUI
    - carPositions should be an array of tuples (position, velocity, acceleration)
        - position defined 1D (only along axis of movement)
        - Let Upper-Left be (0,0), and Bottom-Right be (N,M) positive
            - Thus down/right movement is positive
