import jsonParser

class Car:

	json = jsonParser.JsonParser()
	trip = []
	long = (0,0)
	lat = (0,0)
	speed = (0,0)
	tripCounter = 0

	def __init__(self, tripPath=None, wantedAtt=None):
		self.long = (0,0)
		self.lat = (0,0)
		self.speed = (0,0)
		self.tripCounter = 0
		if(tripPath==None and wantedAtt==None):
			self.json = jsonParser.JsonParser()
			self.trip = self.json.getResources(self.json.getPath())
		else:
			self.json.setPath(tripPath)
			self.json.setWantedAttributes(wantedAtt)
			self.trip = self.json.getResources()

	def getTrip(self):
		return self.trip

	def getJson(self):
		return self.json

	def next(self):
		self.trip[self.tripCounter]
		self.tripCounter += 1
