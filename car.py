import jsonParser

class Car:

	def __init__(self, tripPath = None, wantedAtt = None):
		self.long = (0,0)
		self.lat = (0,0)
		self.speed = (0,0)
		self.tripCounter = 0
		if(tripPath == None and wantedAtt == None):
			self.json = jsonParser.JsonParser()
			self.trip = self.json.getResources(self.json.getPath())
		else:
			self.json.setPath(tripPath)
			self.json.setWantedAttributes(wantedAtt)
			self.trip = self.json.getResources()

	def getTrip(self):
		return self.trip

	def setTrip(self, path, wantedAtt):
		#=self.json.getWantedAttributes()
		self.tripCounter = 0
		self.long = (0,0)
		self.lat = (0,0)
		self.speed = (0,0)
		self.json.setPath(path)
		self.json.setWantedAttributes(wantedAtt)
		self.trip = self.json.getResources(path)

	def getJson(self):
		return self.json

	def next(self):
		tempName = self.trip[self.tripCounter]['name']
		tempVal = self.trip[self.tripCounter]['value']
		if "vehicle_speed" == tempName:
			self.speed = (self.speed[1],tempVal)
		elif "longitdue" == tempName:
			self.long = (self.long[1],tempVal)
		elif "latitude" == tempName:
			self.lat = (self.lat[1],tempVal)
		elif tempVal == "end_of_script":
			return False

		self.tripCounter += 1
		return True
