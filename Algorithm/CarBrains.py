class CarBrains(Car):
	"""determines how each car should behave at each time step"""

	def __init__(self):


		# initialize all of the cars and set them to some initial position

		allCars = []

		# initialize the vertical cars
		for i in range(self.getCols()+1):
			allCars += Car(i, 0, 0, 5) # I need i to be entirely odd :/

		for i in range(self.getRows()):
			allCars += Car(i, 0, 0,5) # I need i to be entirely even :/





