class CarBrains(Car):
	"""determines how each car should behave at each time step"""

	def __init__(self):


 		#############################################################
 		# 			       		Create Cars                         #
 		#############################################################

		# initialize all of the cars and set them to some initial position 
		# (at the beginning of the track with zero velocity)

		allCars = []

		# initialize the vertical cars
		for i in range(self.getCols()+1):
			oddCounter = (i*2)-1
			currentCar = Car(oddCounter, 0, 0, 5) # each vertical car is on an odd numbered track
			allCars.append(currentCar)

		# initialize the horizontal cars
		for i in range(self.getRows()):
			evenCounter = i*2
			currentCar += Car(evenCounter, 0, 0,5) # each horizontal car is on an even numbered track
			allCars.append(currentCar)

		# make a map, such that each car maps to its current positions
		# then loop through all of the cars, and determine its next nearest intersection
		# in the map, also map each car to its nearest intersection 
		####### determine if there are any intersecions that any cars share with one another !!!!!
		# for each car that shares an intersection, obtain their pva
		# whichever car is moving more slowly, speed up the car, 
		# and whichever car is moving more quickly should continue to move at the same speed
		# if any car is not going to intersect with any other cars, then speed up
		# what happens if the cars are moving at the same speed???? it can't be random...ahhhhhh!!!

	#	for firstCarNearestInt = (all cars' nearest intersections):
	#		for secCarNearestInt = (all cars' nearest intersections):
	#			while firstCarNearestInt == secCarNearestInt:









