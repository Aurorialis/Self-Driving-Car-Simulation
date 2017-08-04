class CarBrains(Car):
	"""determines how each car should behave at each time step"""

	def __init__(self):


 		#############################################################
 		# 			       		Create Cars                         #
 		#############################################################

		# initialize all of the cars and set them to some initial position 
		# (at the beginning of the track with zero velocity)

		# make all of the cars strings??
		allCars = []

		# initialize the vertical cars
		for i in range(self.getCols()+1):
			oddCounter = (i*2)-1
			currentCar = Car(oddCounter, 0, 0, 5) # each vertical car is on an odd numbered track
			allCars += currentCar

		# initialize the horizontal cars
		for i in range(self.getRows()):
			evenCounter = i*2
			currentCar += Car(evenCounter, 0, 0,5) # each horizontal car is on an even numbered track
			allCars += currentCar

		##############################################################################
		# while running simulation:

			# Create dictionary that maps each car to its PVA and nearest intersection coordinate

			# initialize the car dictionary
			carInformation = {}

			for i in allCars:
				car = allCars(i) 
				info = [car.getPVA(), car.nearestIntersect()]
				carInformation += {car : info}

			##############################################################
			#                        Algorithm                           #
			##############################################################

			# initialize a list of cars that will crash into each other
			willCrash = []
			# loop through all of the cars to figure out which cars have the same nearest intersections
			for mainLoop in allCars:
				for secondaryLoop in allCars:
					# get the nearest intersection of two cars
					mainIntersection = carInformation[mainLoop](2)
					secondaryIntersection = carInformation[secondaryLoop](2)
					# figure out cars that will crash into each other
					# not the same car, but have sam nearest intersection
					if mainLoop != secondaryLoop && mainIntersection == secondaryIntersection:
						carsWillCrash = (mainLoop, secondaryLoop)
						# ignore any duplicates of the same car
						if carsWillCrash not in willCrash | reverse(carsWillCrash) not in willCrash:
							willCrash += (mainLoop, secondaryLoop) # add pair of cars to list of cars that will crash
						else:
							continue
					else:
						continue			

			


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









