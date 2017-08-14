class Track():
    """creates the tracks for all of the cars"""

    # makes sure pixel resolution is high

    def __init__(self, rows, cols, width, height, timeStep):
        self.rows = rows # number of horizontal lanes
        self.cols = cols # number of vertical lanes
        self.width = width # pixels wides
        self.height = height # pixels high

        #######################################################

    # returns the number of horizontal lanes on the track
    def getRows(self):
        return self.rows

    # returns the number of vertical lanes on the track
    def getCols(self):
        return self.cols

    # returns the width of the track in pixels
    def getWidth(self):
        return self.width

    # returns the height of the track in pixels
    def getHeight(self):
        return self.height

    # returns the number of pixels between each row
    def getRowSpacing(self):
        rowSpacing = (self.height-self.rows)/(self.rows+1)
        return rowSpacing
        
    # returns the number of pixels between each column
    def getColSpacing(self):
        colSpacing = (self.width-self.cols)/(self.cols+1)
        return colSpacing

    # returns a list of tuples, with the x and y coordinate of each intersection contained in the tuple
    def getIntersections(self):
        intersections = []

        for i in range(self.rows):
            for j in range(self.cols):

                # account fot the width of each lane
                # determine the coordinate of each intersection
                x_intersect = (j+1)*self.getColSpacing() + i
                y_intersect = (i+1)*self.getRowSpacing() + j

                intersection = [(x_intersect, y_intersect)]
                intersections += intersection

        return intersections


            
