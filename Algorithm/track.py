class Track:
	"""creates the tracks for all of the cars"""

    def __init__(self, rows, cols, width, height, timeStep):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height


        # returns the number of horizontal lanes on the track
        def getRows():
        	return self.rows

        # returns the number of vertical lanes on the track
        def getCols():
        	return self.cols

        # returns the width of the track in pixels
		def getWidth():
			return self.width

		# returns the height of the track in pixels
		def getHeight():
			return self.height

		# returns the number of pixels between each row
     	def getRowSpacing(self):
		    rowSpacing = (height-self.getRows())/(rows+1)
		    return rowSpacing
		    
		# returns the number of pixels between each column
		def getColSpacing(self):
			colSpacing = (width-self.getCols())/(cols+1)
			return colSpacing

		# returns a list of tuples, with the x and y coordinate of each intersection contained in the tuple
    	def getIntersections(self)
	    	intersections = []

	    	for i in range(self.rows):
	    		for j in range(self.cols):

	    			# account fot the width of each lane
	    			# determine the coordinate of each intersection
	    			x_intersect = (j+1)*self.colSpacing + i
	    			y_intersect = (i+1)*self.rowSpacing + j

	    			intersection = (x_intersect, y_intersect)
	    			intersections + intersection
	    			
			return intersections


    			
