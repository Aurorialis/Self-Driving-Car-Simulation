class track:
	"""creates the track for a single car"""

	# Define the duration of a single timestep
	timeStep = 0.001

	def __init__(self, trackNumber, trackLength):
		self.trackNumber = trackNumber
		self.trackLength = trackLength
