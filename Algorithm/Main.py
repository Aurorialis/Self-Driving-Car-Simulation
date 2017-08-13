
#############################################################
# 			  Create Cars and Track                        #
#############################################################

# INPUTS THAT CAN BE CHANGED
rows = 4
cols = 4
width = 1200
height = 1200
timeStep = 0.1
carLength = 10
carHeight = 6

# create the track
track = Track(rows, cols, width, height, timeStep)


#############################################################
# initialize all of the cars and set them to some initial position 
# (at the beginning of the track with zero velocity)

allCars = []

# initialize the vertical cars
for i in range(cols):
	oddCounter = (i*2)+1
	currentCar = Car(oddCounter, 0, 0, 5, carLength, carWidth) # each vertical car is on an odd numbered track
	allCars += currentCar

# initialize the horizontal cars
for i in range(rows):
	evenCounter = i*2
	currentCar += Car(evenCounter, 0, 0, 5, carLength, carWidth) # each horizontal car is on an even numbered track
	allCars += currentCar


##############################################################
#        Location and Time Calculations for Car              #
##############################################################

	# Determines the next upcoming intersection
	def nearestIntersect(self):

		intersections = track.getIntersections()

		if self.getTrackNo() % 2 == 0: # horizontal track
			# get exact row pixel number
			rowNum = self.getTrackNo()/2
			pixel = rowNum * track.getRowSpacing() # row number of the track
			currentMin = track.getWidth()

			trackType = horizontal

		else: # vertical track
			# get exact col pixel number
			colNum = floor(self.getTrackNo()/2)
			pixel = colNum * track.getColSpacing() # column number of the track
			currentMinn = track.getHeight()

			trackType = vertical

		# loop through list of list of intersections, and find next upcoming intersection			
		for i in intersections:
			if trackType == horizontal:
				whereTrack = i[2] # row value of the horizontal track
				whereOnTrack = i[1] # location of vertical intersection with the track
				spacing = track.getRowSpacing()
				lastLane = spacing * track.getRows()

			else:
				whereTrack = i[1] # col value of the vertical track
				whereOnTrack = i[2] # location of horizontal intersection with the track
				spacing = track.getColSpacing()
				lastLane = spacing * track.getCols()

			# eliminate intersections on a different row/column
			if whereTrack != pixel:
				continue

			# find the nearest intersection
			else:
				# check if next intersection is wrapped around on the other side of the track
				if self.getPos() >= lastLane:
					newMin = whereOnTrack
						if newMin < currentMin:
							currentMin = newMin
							nearestIntersect = i 
						else:
							continue

				# eliminate all intersections that are behind the car
				else if whereTrack <= self.getPos() && self.getPos() < lastLane :
						continue

				# next intersection does not wrap around to the other side
				else:
						newMin = whereTrack - self.getPos() 
						if newMin < currentMin:
							currentMin = newMin
							nearestIntersect = i 
						else:
							continue

		return nearestIntersect

################################################################
	# Get the time in which the car will start crossing the intersection, and will leave the intersection
	# returns a list of size two
	# the first item is when the leading edge of the car enters the intersection
	# the second item is when the lagging edge of the car leaves the intersection
	def intersectionTimes(self):

		v = PVA[1]
		a = PVA[2]

		# get relevant location of next intersection (single value instead of a coordinate)
		# depends on whether car is on a horizontal or vertical track
		if self.getTrackNo % 2 == 0: 
			# horizontal track
			nextIntersect = self.nearestIntersect()[1]
		else:
			# vertical track
			nextIntersect = self.nearestIntersect()[2]

		# if the next intersection wraps around to the other side of the track, make sure to 
		# add the position of the next intersection to the remaining distance on the track
		# before the car wraps around
		if nextIntersect < PVA[0]:
			if self.getTrackNo % 2 == 0: 
				# horizontal track
				d = nextIntersect + track.getWidth()
			else:
				# vertical trac
				d = nextIntersect + track.getHeight()

		# the normal case: intersection is in front of the car on the track (no wrapping around)
		else:
			d = nextIntersect - PVA[0]

		# calculate intersections times based on kinematics
		t_enter = -v/a + sqrt( (v^2/a^2) + 2/a * (d + 0.5*(carLength + carWidth)))
		t_exit = -v/a + sqrt( (v^2/a^2) + 2/a * (d + (carLength + carWidth)))

		intersectionTimes = [t_enter, t_exit]
		return intersectionTimes


############################################################
# run the simulation
isRunning = True

##############################################################
#                     Run Algorithm                          #
##############################################################

while isRunning == True:

	# Create dictionary that maps each car to its PVA, nearest intersection coordinate, and intersection times

	# initialize the car dictionary
	carInformation = {}

	for car in allCars:
		info = [car.PVA(), car.nearestIntersect(), car.intersectionTimes()]
		carInformation[car] = info

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
			if car1 != car2 && mainIntersection == secondaryIntersection:
				carsMightCrash = (car1, car2)
				# ignore any duplicates of the same car
				if carsMightCrash not in mightCrash | reverse(carsMightCrash) not in mightCrash:
					mightCrash += (car1, car2) # add pair of cars to list of cars that will crash
				else:
					continue
			else:
				continue
	return mightCrash


#################################################################
	# check if cars will intersect each other
	# and if they will then change speed of car in order to avoid collision
	for possibleCrashPair in mightCrash:
		# label the cars to make things easier
		car1 = possibleCrashPair[1]
		car2 = possibleCrashPair[2]

		# times when cars enter and exit the intersection
		car1_enter = carInformation[car1][2][0]
		car1_exit = carInformation[car1][2][1]
		car2_enter = carInformation[car2][2][0]
		car2_exit = carInformation[car2][2][1]

		if car1_enter < car2_exit | car2_enter < car1_exit:
			# no collision is going to happen!!!! yayyy!!!!!!




			

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









