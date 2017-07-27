
class Car(Track):
	"""creates the car object"""

	# Initalize a car
		# trackNumber = odd numbers represents tracks going vertically, even numbers represent tracks going horizontally
		# initPos = initial position of car on the track
		# initV = initial velocity of the car on the track
		# initAccel = initial acceleration of the car on the track

	def __init__(self, trackNumber, initPos, initV, initAccel):
		self.getPVA = [initPos initV initAccel]


	# returns the track number that the car is on
	def getTrackNo(self):
		return trackNumber

	# returns a list containing the current position, velocity, and acceleration of the car
	def getPVA(self):
		return self.getPVA

	# returns only the positions of the car (int)
	def getPos(self):
		return self.getPVA[1]

	# returns only the velocity of the car
	def getV(self):
		return self.getPVA[2]

	# returns only the acceleration of the car
	def getAccel(self):
		return self.getPVA[3]


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
#                      Update whereTrackues                  #
##############################################################


	# updates the position and velocity of the car based on current PVA
	# only to be used with the class Car - use other update functions to move car on track
	def updatePV(self):

		# Update postion
		newPos = self.getPos() + self.getV()*timeStep + 0.5*self.getAccel()*timeStep^2

		# wrap around the track if car is about to run off of the track

		if self.getTrackNo % 2 = 0: # even track, tracks runs horizontally
			trackLength = getWidth()
		else:
			trackLength = getHeight()

		if newPos <= trackLength:
			self.getPVA[1] = newPos
		else: 
			self.getPVA[1] = newPos - trackLength

		# Update Velocity
		self.getPVA[2] = self.getV() + self.getAccel()*timeStep

		print self.getPVA


	# move the car with constant velocity
	def moveConstantV()
		self.getPVA[3] = 0
		self.updatePV()

	# move the car with constant acceleration
	def moveConstantAccel():
		self.updatePV()

	# slow the car down !!!!!!!!!!!!!!!!
	def brake():
		self.getPVA[3] = -3 # random acceleration whereTrackue - figure this out
		self.updatePV()







		
