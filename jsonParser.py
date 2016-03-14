import json
from pprint import pprint

class JsonParser:

	wantedAttributes = dict()
	pathName = ""

	def JsonParser(self):
		self.wantedAttributes = {
			'accelerator_pedal_position': False,
			'engine_speed': False,
			'vehicle_speed': True,
			'torque_at_transmission': False,
			'fuel_consumed_since_restart': False,
			'odometer': False,
			'fuel_level': False,
			'steering_wheel_angle': False,
			'latitude': True,
			'longitude': True,
			'transmission_gear_position': False,
			'brake_pedal_status': False,
			'door_status': False,
			'button_state': False,
			'headlamp_status': False,
			'windshield_wiper_status': False,
			'ignition_status': False
		}
		self.pathName = "Resources/downtown-crosstown.json"


	def getWantedAttributes(self):
		return self.wantedAttributes

	def getPath(self):
		return self.pathName

	def setPath(self, newPath):
		self.pathName = newPath

	def setWantedAttributes(self, attributeDict):
		wantedAttributes = attributeDict

	def addWantedAttribute(self, attribute,bool):
		self.wantedAttributes[attribute] = bool

	def removeWantedAttribute(self, attribute):
		del self.wantedAttributes[attribute]


	def isAttributeWanted(self, attributeLine):
		attName = attributeLine.split("\"")[3]
		if attName in self.wantedAttributes:
			return self.wantedAttributes[attName]
		else:
			print(attName)


	def getResources(self,pathname=pathName):
		jfile = list()
		with open(pathname) as f:
			for line in f:
				if self.isAttributeWanted(line):
					continue
				temp = json.loads(line)
				jfile.append(temp)
		jfile.append({"end_of_script":"True"})
		return jfile