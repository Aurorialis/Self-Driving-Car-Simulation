
class Car(Track):
	"""creates the car object"""

	# Initalize a car
		# trackNumber = odd numbers represents tracks going vertically, even numbers represent tracks going horizontally
		# initPos = initial position of car on the track
		# initV = initial velocity of the car on the track
		# initAccel = initial acceleration of the car on the track

	def __init__(self, trackNumber, initPos, initV, initAccel):
		self.getPVA = [initPos initV initAccel]


	def getTrackNo(self):
		return trackNumber

	def getPos(self):
		return self.getPVA[1]

	def getV(self):
		return self.getPVA[2]

	def getAccel(self):
		return self.getPVA[3]


##############################################################
#                        Location                           #
##############################################################

	def nearestIntersect(self):

		intersections = self.getIntersections()

		if self.getTrackNo() % 2 = 0: # horizontal track
			# get exact row pixel number
			rowNum = self.getTrackNo()/2
			rowPixel = rowNum * self.getRowSpacing()

			#sameRow for sameRow in intersections if sameRow[0].startswith('rowPixel')

		else: # vertical track
			# get exact col pixel number
			colNum = floor(self.getTrackNo()/2)
			colPixel = colNum * self.getColSpacing()




##############################################################
#                      Update Values                         #
##############################################################


	# updates the position and velocity of the car based on current PVA
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

	# slow the car down
	def brake():
		self.getPVA[3] = -3 # random acceleration value - figure this out
		self.updatePV()







		
