
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

	def __init__(self, trackNumber, initPos, initV, initAccel, carLength, carWidth):
		self.carWidth = carWidth # length of the car
		self.carLength = carLength # width of the car
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
#                      Update Track                          #
##############################################################


	# updates the position and velocity of the car based on current PVA
	# only to be used with the class Car - use other update functions to move car on track
	def updatePV(self):

		# Update postion using kinematics
		newPos = self.getPos() + self.getV()*timeStep + 0.5*self.getAccel()*timeStep^2

		# make sure that the car does not start moving backwards
		if newPos < self.getPos():
			newPos = self.getPos()
		else:
			continue

		# wrap around the track if car is about to run off of the track

		if self.getTrackNo % 2 = 0: # even track, tracks runs horizontally
			trackLength = getWidth()
		else: # odd track, track runs vertically
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

	# # move the car with constant acceleration
	# def moveConstantAccel():
	# 	self.updatePV()

	def speedUp():
		self.setAccel(3)
		self.updatePV()
		# # if car is already speeding up, increase acceleration
		# if self.PVA[2] > 0:
		# 	self.PVA[2] += 0.1*(self.PVA[2])
		# # if car is not accelerating yet, begin accelerating
		# else:
		# 	self.PVA[2] = 3
		# # update position and velocity based on braking
		# self.updatePV()

	def lightSpeed():
		self.setAccel(maxAccel)
		self.updatePV()

	# slow the car down
	def brake():
		self.setAccel(-3)
		# # if car is already braking, increase braking amount
		# if self.PVA[2] < 0:
		# 	self.PVA[2] += 0.1*(self.PVA[2])
		# # if car is not braking yet, begin braking
		# else:
		# 	self.PVA[2] = -3
		# # update position and velocity based on braking
		# self.updatePV()

	# brake as quickly as possible
	def hardBrake():
		self.setAccel(maxBrake)
		self.updatePV()







		
