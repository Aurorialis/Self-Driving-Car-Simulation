
from random import choice

from gui import GUI
from track import Track
from car import Car
from math import floor, sqrt

import time

#############################################################
# 			  Create Cars and Track                        #
#############################################################

# INPUTS THAT CAN BE CHANGED
v_term = 10 # terminal velocity
t_panic = 4 # time for which intersection is going to happen too soon, and emergency brakes must be used

rows = 4
cols = 4
width = 640
height = 480
timeStep = 0.1
carLength = 10
carWidth = 6

# create the track
track = Track(rows, cols, width, height, timeStep)


#############################################################
# initialize all of the cars and set them to some initial position 
# (at the beginning of the track with zero velocity)

allCars = []

# initialize the vertical cars
for i in range(cols):
	oddCounter = (i*2)+1
	currentCar = Car(oddCounter, 0, 1, 0.5, carLength, carWidth, track, timeStep) # each vertical car is on an odd numbered track
	allCars += [currentCar]

# initialize the horizontal cars
for i in range(rows):
	evenCounter = i*2
	currentCar = Car(evenCounter, 0, 2, 0.5, carLength, carWidth, track, timeStep) # each horizontal car is on an even numbered track
	allCars += [currentCar]


##############################################################
#        Location and Time Calculations for Car              #
##############################################################

	# Determines the next upcoming intersection
	def nearestIntersect(car):

		intersections = track.getIntersections()
		nearestIntersect = (-1,-1)

		if car.getTrackNo() % 2 == 0: # horizontal track
			# get exact row pixel number
			rowNum = car.getTrackNo()/2
			pixel = rowNum * track.getRowSpacing() # row number of the track
			currentMin = track.getWidth()

			trackType = 'horizontal'

		else: # vertical track
			# get exact col pixel number
			colNum = floor(car.getTrackNo()/2)
			pixel = colNum * track.getColSpacing() # column number of the track
			currentMin = track.getHeight()

			trackType = 'vertical'

		# loop through list of list of intersections, and find next upcoming intersection			
		for i in intersections:
			if trackType == 'horizontal':
				whereTrack = i[1] # row value of the horizontal track
				whereOnTrack = i[0] # location of vertical intersection with the track
				spacing = track.getColSpacing()
				lastLane = spacing * track.getCols()

			else:
				whereTrack = i[0] # col value of the vertical track
				whereOnTrack = i[1] # location of horizontal intersection with the track
				spacing = track.getRowSpacing()
				lastLane = spacing * track.getRows()

			# eliminate intersections on a different row/column
			if whereTrack != pixel:
				continue

			# find the nearest intersection
			else:
				# check if next intersection is wrapped around on the other side of the track
				if car.getPos() >= lastLane:
					newMin = whereOnTrack
					if newMin < currentMin:
						currentMin = newMin
						nearestIntersect = i 
					else:
						continue

				# eliminate all intersections that are behind the car
				elif whereOnTrack <= car.getPos() and car.getPos() < lastLane :
					continue

				# next intersection does not wrap around to the other side
				else:
					newMin = whereOnTrack - car.getPos() 
					if newMin < currentMin:
						currentMin = newMin
						nearestIntersect = i 
					else:
						continue

		return nearestIntersect


	# Get the time in which the car will start crossing the intersection, and will leave the intersection
	# returns a list of size two
	# the first item is when the leading edge of the car enters the intersection
	# the second item is when the lagging edge of the car leaves the intersection
	def intersectionTimes(car):

		v = car.PVA[1]
		a = car.PVA[2]

		# get relevant location of next intersection (single value instead of a coordinate)
		# depends on whether car is on a horizontal or vertical track
		if car.getTrackNo() % 2 == 0: 
			# horizontal track
			nextIntersect = nearestIntersect(car)[0]
		else:
			# vertical track
			nextIntersect = nearestIntersect(car)[1]

		# if the next intersection wraps around to the other side of the track, make sure to 
		# add the position of the next intersection to the remaining distance on the track
		# before the car wraps around
		if nextIntersect < car.PVA[0]:
			if car.getTrackNo() % 2 == 0: 
				# horizontal track
				d = nextIntersect + track.getWidth()
			else:
				# vertical trac
				d = nextIntersect + track.getHeight()

		# the normal case: intersection is in front of the car on the track (no wrapping around)
		else:
			d = nextIntersect - car.PVA[0]

		# calculate intersections times based on kinematics
		t_enter = -v/a + sqrt( (v**2/a**2) + 2/a * (d + 0.5*(carLength + carWidth)))
		t_exit = -v/a + sqrt( (v**2/a**2) + 2/a * (d + (carLength + 0.5*carWidth)))

		intersectionTimes = [t_enter, t_exit]
		return intersectionTimes


############################################################
# run the simulation
isRunning = True

# Initialize GUI
g = GUI(4,4,width,height)
g.tk.update()
time.sleep(5)

##############################################################
#                     Run Algorithm                          #
##############################################################

while isRunning == True:

	# Break loop on quit button
	if not g.notQuit:
		g.tk.destroy()
		break

	# if it hasn't started, then update gui and wait for start flag
	if not g.startFlag:
		g.tk.update_idletasks()
		g.tk.update()
		time.sleep(0.02)
		continue

	# Create dictionary that maps each car to its PVA, nearest intersection coordinate, and intersection times

	# initialize the car dictionary
	carInformation = {}
	carPVAs = []
	#print("Print car info")
	for car in allCars:
		info = [car.PVA, nearestIntersect(car), intersectionTimes(car)]
		carInformation[car] = info
		carPVAs += [info[0]]
	#print(carPVAs)

	##################
	### Update GUI ###
	##################
	g.animate(carPVAs)
	g.checkCollision()
	g.tk.update_idletasks()
	g.tk.update()
	time.sleep(0.05)

##############################################################
#                        Algorithm                           #
##############################################################

	# initialize a list of tuples of pairs of cars that might crash into each other
	# have the same next nearest intersect (but not checking intersection times yet)
	mightCrash = []
	# loop through all of the cars to figure out which cars have the same nearest intersections
	for car1 in allCars:
		for car2 in allCars:
			# get the nearest intersection of two cars
			mainIntersection = carInformation[car1][1]
			secondaryIntersection = carInformation[car2][1]
			# figure out cars that will crash into each other
			# not the same car, but have same nearest intersection
			if car1 != car2 and mainIntersection == secondaryIntersection:
				carsMightCrash = (car1, car2)
				# ignore any duplicates of the same car
				if (carsMightCrash not in mightCrash) or (reversed(carsMightCrash) not in mightCrash):
					mightCrash += [(car1, car2)] # add pair of cars to list of cars that will crash
				else:
					continue
			else:
				continue
	# return mightCrash


#################################################################
	# check if cars will intersect each other
	# and if they will then change speed of car in order to avoid collision
	for possibleCrashPair in mightCrash:
		# label the cars to make things easier
		car1 = possibleCrashPair[0]
		car2 = possibleCrashPair[1]

		# times when cars enter and exit the intersection
		car1_enter = carInformation[car1][2][0]
		car1_exit = carInformation[car1][2][1]
		car2_enter = carInformation[car2][2][0]
		car2_exit = carInformation[car2][2][1]

		# label velocities
		car1_v = carInformation[car1][1][1] 
		car2_v = carInformation[car2][1][1]


		# no collision is going to happen! yayyy!!!
		if car1_enter < car2_exit or car2_enter < car1_exit:
			# if either of the cars are moving at terminal velocity already
			# then just move the cars at a constant velocity
			if car1_v >= v_term or car2_v >= v_term:
				#print("Move at constant V")
				car1.moveConstantV()
				car2.moveConstantV()
			# otherwise speed up both cars
			else:
				#print("Speed up car")
				car1.speedUp()
				car2.speedUp()

#############################################################################
		# COLLISION IS GOING TO HAPPEN 
		# BEGIN ACTUAL PART OF ALGORITHM!!!

		else:

			# determine which car will reach intersection faster


			####################################################
			# if car1 will reach the intersection before car 2
			if car1_enter < car2_enter:

				# if car1 is not moving at terminal velocity
				if car1_v < v_term:

					if car1_enter <= t_panic:
						# panic mode
						#print("Car1 light Speed, Car2 hard brake")
						car1.lightSpeed()
						car2.hardBrake()
					else:
						# accelerate car1 and let car2 move at constant velocity
						car1.speedUp()
						car2.moveConstantV()

				# if car1 is moving at terminal velocity
				else:

					if car1_enter <= t_panic:
						# panic mode
						car1.moveConstantV()
						car2.hardBrake()
					else:
						# continue to move car1 at constant velocity and brake car2
						car1.moveConstantV()
						car2.brake()

			#####################################################
			# if car2 will reach the intersection before car1
			elif car2_enter < car1_enter:

				# if car2 is not moving at terminal velocity
				if car2_v < v_term:

					if car2_enter <= t_panic:
						# panic mode
						car2.lightSpeed()
						car1.hardBrake()
					else:
						# accelerate car2 and let car1 move at constant velocity
						car2.speedUp()
						car1.moveConstantV()

				# if car2 is moving at terminal velocity
				else:

					if car2_enter <= t_panic:
						car2.moveConstantV()
						car1.hardBrake()
					else:
						# continue to move car1 at constant velocity and brake car2
						car2.moveConstantV()
						car1.brake()

			#####################################################
			# if the cars will reach the intersection at the exact same time
			else:

				# determine which car is moving faster

				# if car1 is moving faster
				if car2_v < car1_v:

					# if car1 is not moving at terminal velocity
					if car1_v < v_term:

						if car1_enter <= t_panic:
							# panic mode
							car1.lightSpeed()
							car2.hardBrake()

						else:
							# speed up car1
							# slow down car2
							car1.speedUp()
							car2.brake()

					# if car1 is moving at terminal velocity
					else: 

						if car1_enter <= t_panic:
							# panic mode
							car1.moveConstantV()
							car2.hardBrake()

						else:
							# move car1 at constant velocity
							# slow down car2
							car1.moveConstantV()
							car2.brake()

				####################################################

				# if car2 is moving faster
				elif car1_v < car2_v:

					# if car2 is not moving at terminal velocity
					if car2_v < v_term:

						if car2_enter <= t_panic:
							# panic mode
							car2.lightSpeed()
							car1.hardBrake()

						else:
							# speed up car2
							# slow down car1
							car2.speedUp()
							car1.brake()

					# if car2 is moving at terminal velocity
					else: 

						if car2_enter <= t_panic:
							# panic mode
							car2.moveConstantV()
							car1.hardBrake()

						else:
							# move car2 at constant velocity
							# slow down car1
							car2.moveConstantV()
							car1.brake()

				####################################################

				# car1 and car2 are moving at the same velocity
				else:
					# randomly select a car to speed up and a car to slow down
					carSlow = choice([car1,car2])

					for car in [car1,car2]:
						if car == carSlow:
							continue
						else:
							carFast = car

					# if they are not moving at terminal velocity
					if car1_v < v_term:

						if car1_enter <= t_panic:
							# panic mode
							carSlow.hardBrake()
							carFast.lightSpeed()

						else:
							# slow down car to be slowed, and speed up the other one
							carSlow.brake()
							carFast.speedUp()

					# if they are moving at terminal velocity
					else:

						if car1_enter <= t_panic:
							# panic mode
							carSlow.hardBrake()
							carFast.moveConstantV()

						else:
							# slow down car to be slowed
							carSlow.brake()
							carFast.moveConstantV()


	##############################################
	# accelerate the cars that aren't about to intersect with anyone
	# (aren't in the "mightCrash" list)

	crashAlgCar =[] # car that goes through the crash-avoidance algorithm above
	for carPair in mightCrash:
		crashAlgCar += [carPair[0], carPair[1]]

	lonelyCars = [] # car that doesn't need to go through crash-avoidance algorithm b/c isn't going to crash 
	for car in allCars:
		# if the car might crash, then it already went through the correct algorithm
		if car in crashAlgCar:
			continue
		# if the car doesn't have to worry about crashing, add it to the list
		else:
			lonelyCars += [car]

	# loop through all of the lonely cars and speed them up
	for lonelyCar in lonelyCars:
		# if not moving at terminal velocity, speed up
		if lonelyCar.getV() < v_term:
			lonelyCar.speedUp()
		elif lonelyCar.getV() > v_term:
			lonelyCar.brake()
		# if moving at terminal velocity, just keep moving with same velocity
		else:
			lonelyCar.moveConstantV()









