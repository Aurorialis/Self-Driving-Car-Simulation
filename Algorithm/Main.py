
#############################################################
# 			  Create Cars and Track                        #
#############################################################

# INPUTS THAT CAN BE CHANGED
rows = 4
cols = 4
width = 800
height = 800
timeStep = 0.1

# create the track
track = Track(rows, cols, width, height, timeStep)


#############################################################
# initialize all of the cars and set them to some initial position 
# (at the beginning of the track with zero velocity)

allCars = []

# initialize the vertical cars
for i in range(cols):
	oddCounter = (i*2)+1
	currentCar = Car(oddCounter, 0, 0, 5) # each vertical car is on an odd numbered track
	allCars += currentCar

# initialize the horizontal cars
for i in range(rows):
	evenCounter = i*2
	currentCar += Car(evenCounter, 0, 0,5) # each horizontal car is on an even numbered track
	allCars += currentCar


############################################################
# run the simulation
isRunning = True

##############################################################
#                     Run Algorithm                          #
##############################################################

while isRunning == True:

	# Create dictionary that maps each car to its PVA and nearest intersection coordinate

	# initialize the car dictionary
	carInformation = {}

	for car in allCars:
		info = [car.PVA(), car.nearestIntersect()]
		carInformation[car] = info

##############################################################
#                        Algorithm                           #
##############################################################

	# initialize a list of cars that might crash into each other
	# have the same next nearest intersect
	mightCrash = []
	# loop through all of the cars to figure out which cars have the same nearest intersections
	for car1 in allCars:
		for car2 in allCars:
			# get the nearest intersection of two cars
			mainIntersection = carInformation[car1](1)
			secondaryIntersection = carInformation[car2](1)
			# figure out cars that will crash into each other
			# not the same car, but have same nearest intersection
			if car1 != car2 && mainIntersection == secondaryIntersection:
				carsMightCrash = (car1, car2)
				# ignore any duplicates of the same car
				if carsMightCrash not in mightCrash | reverse(carsMightCrash) not in mightCrash:
					mightCrash += (car1, car2) # add pair of cars to list of cars that will crash
				else:
					continue
			else:
				continue

	# check if cars will intersect each others			



# earliest and latest time that can arrive at intersection?

	#-yes- make a map, such that each car maps to its current positions
	#-yes- then loop through all of the cars, and determine its next nearest intersection
	#-yes- in the map, also map each car to its nearest intersection 
	#-yes- determine if there are any intersecions that any cars share with one another !!!!!
	# for each car that shares an intersection, obtain their pva
	# whichever car is moving more slowly, speed up the car, 
	# and whichever car is moving more quickly should continue to move at the same speed
	# if any car is not going to intersect with any other cars, then speed up
	# what happens if the cars are moving at the same speed???? it can't be random...ahhhhhh!!!

#	for firstCarNearestInt = (all cars' nearest intersections):
#		for secCarNearestInt = (all cars' nearest intersections):
#			while firstCarNearestInt == secCarNearestInt:









