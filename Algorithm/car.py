
class car(track):
	"""creates the car object"""

	# Initalize a car
		# trackNumber = (int) track number between 1-9 inclusive
		# initPos = initial position of car on the track
		# initV = initial velocity of the car on the track
		# initAccel = initial acceleration of the car on the track
	def __init__(self, trackNumber, initPos, initV, initAccel):
		self.getTrackNo = trackNumber 
		self.getPos = initPos 
		self.getV = initV 
		self.getAccel = initAccel 

##############################################################
#                      Update Values                         #
##############################################################

	# Update the position of the car
	def move():
		newPos = self.getPos + self.getV*timeStep

		# wrap around the track if car is about to run off of the track
		if newPos <= trackLength
			self.getPos = newPos

		else 
			self.getPos = newPos - trackLength

	# Update the velocity of the car
	def accelerate():
		self.getV += self.getAccel*timeStep

	# Update the acceleration of the car
	def jerk(self, jerk):
		self.getAccel += jerk





		
