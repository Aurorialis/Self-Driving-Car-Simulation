class Track:
	"""creates the tracks for all of the cars"""

    def __init__(self, rows, cols, width, height, timeStep):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height


        def getRows():
        	return self.rows

        def getCols():
        	return self.cols

		def getWidth():
			return self.width

		def getHeight():
			return self.height

     	def getRowSpacing(self):
		    rowSpacing = height/(rows+1)
		    return rowSpacing
		    

		def getColSpacing(self):
			colSpacing = width/(cols+1)
			return colSpacing

    	def getIntersections(self)
	    	intersections = []
	    	for i in range(self.rows):
	    		for j in range(self.cols):
	    			x_intersect = (j+1)*self.colSpacing
	    			y_intersect = (i+1)*self.rowSpacing
	    			intersection = (x_intersect, y_intersect)
	    			intersections + intersection
			return intersections


    			
