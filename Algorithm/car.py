# maximum acceleration of a car (both speeding up and braking)
normalAccel = 100
normalBrake = -100
maxAccel = 2000
maxBrake = -2000

class Car():
	"""creates the car object"""

	# Initalize a car
		# trackNumber = odd numbers represents tracks going vertically, even numbers represent tracks going horizontally
		# initPos = initial position of car on the track
		# initV = initial velocity of the car on the track
		# initAccel = initial acceleration of the car on the track



	def __init__(self, trackNumber, initPos, initV, initAccel, carLength, carWidth, track, timeStep, v_term):
		self.carWidth = carWidth # length of the car
		self.carLength = carLength # width of the car
		self.PVA = [initPos, initV, initAccel]
		self.trackNumber = trackNumber
		self.track = track
		self.timeStep = timeStep
		self.v_term = v_term

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
		newPos = self.getPos() + self.getV()*self.timeStep + 0.5*self.getAccel()*self.timeStep**2

		# make sure that the car does not start moving backwards
		if newPos < self.getPos():
			newPos = self.getPos()
		else:
			pass

		# wrap around the track if car is about to run off of the track

		if self.getTrackNo() % 2 == 0: # even track, tracks runs horizontally
			trackLength = self.track.getWidth()
		else: # odd track, track runs vertically
			trackLength = self.track.getHeight()

		if newPos <= trackLength:
			self.PVA[0] = newPos
		else: 
			self.PVA[0] = newPos - trackLength

		# Update Velocity
		newV = self.getV() + self.getAccel()*self.timeStep

		# make sure car does not start moving backwards
		if newV < 0:
			newV = 0
		elif newV > self.v_term:
			newV = self.v_term
		else:
			newV = newV

		self.PVA[1] = newV


	# move the car with constant velocity - not zero so that we don't divide by 0
	def moveConstantV(self):
		#print("constant V - car, %d" %self.trackNumber)
		self.setAccel(0.000001)
		self.updatePV()

	# # move the car with constant acceleration
	# def moveConstantAccel():
	# 	self.updatePV()

	def speedUp(self):
		#print("speed up - car, %d" %self.trackNumber)
		self.setAccel(normalAccel)
		self.updatePV()
		# # if car is already speeding up, increase acceleration
		# if self.PVA[2] > 0:
		# 	self.PVA[2] += 0.1*(self.PVA[2])
		# # if car is not accelerating yet, begin accelerating
		# else:
		# 	self.PVA[2] = 3
		# # update position and velocity based on braking
		# self.updatePV()

	def lightSpeed(self):
		#print("LIGHT SPEED - car, %d" %self.trackNumber)
		self.setAccel(maxAccel)
		self.updatePV()

	# slow the car down
	def brake(self):
		#print("brake - car, %d" %self.trackNumber)
		self.setAccel(normalBrake)
		# # if car is already braking, increase braking amount
		# if self.PVA[2] < 0:
		# 	self.PVA[2] += 0.1*(self.PVA[2])
		# # if car is not braking yet, begin braking
		# else:
		# 	self.PVA[2] = -3
		# # update position and velocity based on braking
		# self.updatePV()

	# brake as quickly as possible
	def hardBrake(self):
		#print("HARD BRAKE- car, %d" %self.trackNumber)
		self.setAccel(maxBrake)
		self.updatePV()







		
