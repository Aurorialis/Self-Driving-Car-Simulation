"""

    car.py

    Define the Car class, which has attributes such as:

        position, velocity, acceleration etc

"""

# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=R0902


class Car():



    def __init__(self, px=0, py=0):
        """ Constructor """

        # Position (m)
        self.px = px
        self.py = py
        # Velocity (m/s)
        self.vx = 0
        self.vy = 0
        # Acceleration (m/s^2)
        self.ax = 0
        self.ay = 0


        # Constants
        self.MAX_VEL = 27 # 60 mph = 26.8 m/s
        self.MAX_ACCEL = 2.7 # 0-60mph in 10s => avg 27m/s / 10s = 2.7 m/s^2

    def update(self, dt):
        """ Update the state of the car based on dt"""

        # Pos
        self.px += self.vx*dt
        self.py += self.vy*dt
        # Velocity
        self.vx += self.ax*dt
        self.vy += self.ay*dt

        # Bounds on velocity
        if self.vx > self.MAX_VEL:
            self.vx = self.MAX_VEL
            self.ax = 0
        if self.vy > self.MAX_VEL:
            self.vy = self.MAX_VEL
            self.ay = 0

    def set_accel(self, ax, ay):
        """ Set the acceleration """
        self.ax = ax
        self.ay = ay

        # Bounds
        if abs(self.ax) > self.MAX_ACCEL:
            self.ax = self.MAX_ACCEL
        if abs(self.ay) > self.MAX_ACCEL:
            self.ay = self.MAX_ACCEL
