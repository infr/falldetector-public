# Fall detector webservice
#
# Kim Salmi, kim.salmi(at)iki(dot)fi
# http://tunn.us/arduino/falldetector.php
# License: GPLv3

import requests

class Webservice(object):
	
	def __init__(self, place):
		self.url = 'http://tunn.us/tools/healthservice/add.php?place='+place+'&type='
		self.data = ''


	def alarm(self, detectiontype, personid):
		tempurl = self.url
		tempurl = tempurl+detectiontype+'&personid='+str(personid)
		response = requests.get(tempurl, data=self.data)
		print response