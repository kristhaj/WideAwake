import json
from pprint import pprint

wantedAttributes = {
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

def getWantedAttributes():
	return wantedAttributes

def setWantedAttributes(attributeDict):
	wantedAttributes = attributeDict

def addWantedAttribute(attribute,bool):
	wantedAttributes[attribute] = bool

def removeWantedAttribute(attribute):
	del wantedAttributes[attribute]


def isAttributeWanted(attributeLine):
	attName = attributeLine.split("\"")[3]
	if attName in wantedAttributes:
		return wantedAttributes[attName]
	else:
		print(attName)


def getResources(pathname):
	jfile = list()
	with open(pathname) as f:
		i = -1
		for line in f:
			if isAttributeWanted(line):
				continue
			jfile += json.loads(line)


getResources("Resources/downtown-crosstown.json")