import json
from pprint import pprint
from random import randint

class JsonParser:
	'''
	This class takes in testdata in a json format, and creates a list of dict with the wanted attributes. Since the json
	files are on over 1 million lines, this parser should only be used as a setup since it takes time to traverse a
	whole file.
	'''

	def __init__(self):
		'''
		Sets the default jsonfile as downtown-crosstown.json and wantedAttributes.
		:return: Nothing
		'''
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
			'ignition_status': False,
			'ABS': True
		}
		self.pathName = "Resources/downtown-crosstown.json"


	def getWantedAttributes(self):
		'''
		A dictionary of attribute names and true values if wanted, otherwise false.
		:return: Dictionary.
		'''
		return self.wantedAttributes

	def getPath(self):
		'''
		Returns the path associated with this jsonParser object.
		:return: String
		'''
		return self.pathName

	def setPath(self, newPath):
		'''
		Sets a new path to a jsonfile, there is no verification, so make sure it's correct.
		:param newPath: String.
		:return: Nothing.
		'''
		self.pathName = newPath

	def setWantedAttributes(self, attributeDict):
		'''
		Sets which attributes that is wanted from the json file.
		:param attributeDict: List of attributes that is in the jsonfile with true/false if wanted.
		:return: Nothing.
		'''
		self.wantedAttributes = attributeDict

	def addWantedAttribute(self, attribute, bool):
		'''
		Adds a single wanted attribute.
		:param attribute: The attribute name used in the jsonfile.
		:param bool: True if wanted, false if not.
		:return: Nothing.
		'''
		self.wantedAttributes[attribute] = bool

	def removeWantedAttribute(self, attribute):
		'''
		Removes a single attribute name. NB! DOES NOT SET TO FALSE, it is removed from the list.
		:param attribute: attribute name to be removed.
		:return: Nothing.
		'''
		del self.wantedAttributes[attribute]


	def isAttributeWanted(self, attributeLine):
		'''
		Checks if a jsonformatted object is wanted by looking it up in the wantedAttributes dictionary. If it is not
		found the attribute name will be printed so it can be added to the list.
		:param attributeLine: takes in a jsonformatted object and returns if the attribute is wanted.
		:return: true if the attribute is wanted, false if not and prints unlisted attribute names(nothing is returned).
		'''
		attName = attributeLine.split("\"")[3]
		if attName in self.wantedAttributes:
			return self.wantedAttributes[attName]
		else:
			print(attName) #Will print attName for attList incase we havn't come across it jet


	def getResources(self,pathname):
		#=pathName
		'''
		Returns a list of jsonobjects as dictionaries based on the wanted attributes, ignores the unwanted ones.
		:param pathname: Should take its own path as default, but doesn't at the moment, so needs a path to run.
		:return: A list of jsonobjects as dictionaries.
		'''
		jfile = list()
		with open(pathname) as f:
			for line in f:
				if not(self.isAttributeWanted(line)):
					randNumb = random.randint(1, 100)
					if randNumb == 1:
						temp = json.loads(line)['timestamp']
						jfile.append({'timestamp': temp, 'name': 'ABS', 'value': True})
					continue
				temp = json.loads(line)
				jfile.append(temp)
		jfile.append({'timestamp': 5000, 'name':'end_of_script','value':'end_of_script'})
		return jfile
