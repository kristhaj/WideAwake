import jsonParser


class Car:
    '''
	This class is meant to simulate a car as it is driving, by changing it's attributes/variables as it reads through a
	json object of testdata using its tripcounter.
	'''

    def __init__(self, tripPath=None, wantedAtt=None):
        '''
		Initialises with the default jsonParser values as the trip.
		:param tripPath: Uses jsonParsers default path to json object if not given.
		:param wantedAtt: Uses jsonParsers default trip attributes if not given.
		:return:
		'''
        self.long = (0, 0)
        self.lat = (0, 0)
        self.speed = (0, 0)
        self.timestamp = (0, 0)
        self.ABS = False
        self.tripCounter = 0
        if (tripPath == None and wantedAtt == None):
            self.json = jsonParser.JsonParser()
            self.trip = self.json.getResources(self.json.getPath())
        else:
            self.json.setPath(tripPath)
            self.json.setWantedAttributes(wantedAtt)
            self.trip = self.json.getResources()

    def getTrip(self):
        '''
		Returns a list of dicts containing a attribute given by name, value and timestamp.
		:return: List of ditcs.
		'''
        return self.trip

    def getJson(self):
        '''
		The jsonParser connected to the car's trip
		:return: jsonParser
		'''
        return self.json

    def setTrip(self, path, wantedAtt):
        '''
		Gives the car a new trip by reading in a json file through jsonParser, using the given path and wanted attributes
		:param path: Path to the json file.
		:param wantedAtt: Dictionary of all attributes from the json file choosing true/false for which attributes one wants.
				{"speed":True}
		:return: None
		'''
        # =self.json.getWantedAttributes()
        self.tripCounter = 0
        self.long = (0, 0)
        self.lat = (0, 0)
        self.speed = (0, 0)
        self.ABS = False
        self.timestamp = (0, 0)
        self.json.setPath(path)
        self.json.setWantedAttributes(wantedAtt)
        self.trip = self.json.getResources(path)

    def next(self):
        '''
		The driving simulator. When called it reads one line of data from its trip list and changes the cars attributes
		depending on the name of the value. If the value is "end_of_script" the trip is done and this function returns false.
		:return: false if the trip is over, or true if it is still going.
		'''
        tempName = self.trip[self.tripCounter]['name']
        tempVal = self.trip[self.tripCounter]['value']
        tempTime = self.trip[self.tripCounter]['timestamp']
        self.timestamp = (self.timestamp[1], tempTime)
        if 'ABS' == tempName:
            self.ABS = True
        else:
            self.ABS = False
        if "vehicle_speed" == tempName:
            self.speed = (self.speed[1], tempVal)
        elif "longitude" == tempName:
            self.long = (self.long[1], tempVal)
        elif "latitude" == tempName:
            self.lat = (self.lat[1], tempVal)
        elif tempName == "end_of_script":
            return False

        self.tripCounter += 1
        return True
