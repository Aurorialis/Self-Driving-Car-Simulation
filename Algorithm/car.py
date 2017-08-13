
class Car(Track):
	"""creates the car object"""

	# Initalize a car
		# trackNumber = odd numbers represents tracks going vertically, even numbers represent tracks going horizontally
		# initPos = initial position of car on the track
		# initV = initial velocity of the car on the track
		# initAccel = initial acceleration of the car on the track

		# maximum acceleration of a car (both speeding up and braking)
		maxAccel = 10
		maxBrake = -10

	def __init__(self, trackNumber, initPos, initV, initAccel):
		self.PVA = [initPos initV initAccel]
		self.trackNumber = trackNumber

	# returns the track number that the car is on
	def getTrackNo(self):
		return self.trackNumber

	# returns only the positions of the car (int)
	def getPos(self):
		return self.PVA[0]

	# returns only the velocity of the car
	def getV(self):
		return self.PVA[1]

	# returns only the acceleration of the car
	def getAccel(self):
		return self.PVA[2]

	def setAccel(self, newAccel):
		self.PVA[2] = newAccel


##############################################################
#                        Location                           #
##############################################################

	# Determines the next upcoming intersection
	def nearestIntersect(self):

		intersections = self.getIntersections()

		if self.getTrackNo() % 2 == 0: # horizontal track
			# get exact row pixel number
			rowNum = self.getTrackNo()/2
			pixel = rowNum * self.getRowSpacing() # row number of the track
			currentMin = self.getWidth()

			trackType = horizontal

		else: # vertical track
			# get exact col pixel number
			colNum = floor(self.getTrackNo()/2)
			pixel = colNum * self.getColSpacing() # column number of the track
			currentMinn = self.getHeight()

			trackType = vertical

		# loop through list of list of intersections, and find next upcoming intersection			
		for i in intersections:
			if trackType == horizontal:
				whereTrack = i[2] # row value of the horizontal track
				whereOnTrack = i[1] # location of vertical intersection with the track
				spacing = self.getRowSpacing()
				lastLane = spacing * self.getRows()

			else:
				whereTrack = i[1] # col value of the vertical track
				whereOnTrack = i[2] # location of horizontal intersection with the track
				spacing = self.getColSpacing()
				lastLane = spacing * self.getCols()

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

##############################################################
#                      Update Track                          #
##############################################################


	# updates the position and velocity of the car based on current PVA
	# only to be used with the class Car - use other update functions to move car on track
	def updatePV(self):

		# Update postion
		newPos = self.getPos() + self.getV()*timeStep + 0.5*self.getAccel()*timeStep^2

		# make sure that the car does not start moving backwards
		if newPos < self.getPos():
			newPos = self.getPos()
		else:
			continue

		# wrap around the track if car is about to run off of the track

		if self.getTrackNo % 2 = 0: # even track, tracks runs horizontally
			trackLength = getWidth()
		else:
			trackLength = getHeight()

		if newPos <= trackLength:
			self.PVA[1] = newPos
		else: 
			self.PVA[1] = newPos - trackLength

		# Update Velocity
		newV = self.getV() + self.getAccel()*timeStep

		# make sure car does not start moving backwards
		if newV < 0:
			newV = 0
		else:
			continue

		self.PVA[2] = newV


	# move the car with constant velocity
	def moveConstantV()
		self.setAccel(0)
		self.updatePV()

	# move the car with constant acceleration
	def moveConstantAccel():
		self.updatePV()

	def speedUp():
		# if car is already speeding up, increase acceleration
		if self.PVA[2] > 0:
			self.PVA[2] += 0.1*(self.PVA[2])
		# if car is not accelerating yet, begin accelerating
		else:
			self.PVA[2] = 3
		# update position and velocity based on braking
		self.updatePV()

	def lightSpeed():
		self.PVA[2] = maxAccel
		self.updatePV()

	# slow the car down
	def brake():
		# if car is already braking, increase braking amount
		if self.PVA[2] < 0:
			self.PVA[2] += 0.1*(self.PVA[2])
		# if car is not braking yet, begin braking
		else:
			self.PVA[2] = -3
		# update position and velocity based on braking
		self.updatePV()

	# brake as quickly as possible
	def brakeHard():
		self.PVA[2] = maxBrake
		self.updatePV()







		
