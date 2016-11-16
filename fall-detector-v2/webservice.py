# Fall detector webservice
#
# Kim Salmi, kim.salmi(at)iki(dot)fi
# http://tunn.us/arduino/falldetector.php
# License: GPLv3

import requests

class Webservice(object):
	
	def __init__(self, place, phone):
		#self.url = 'http://tunn.us/tools/healthservice/add.php?place='+place+'&phone='+phone
		self.url = 'http://salmi.pro/ject/fall/add.php?place='+place+'&phone='+phone	
		self.data = ''


	def alarm(self, detectiontype, personid):
		tempurl = self.url
		tempurl = tempurl+'&type=+'+detectiontype+'&personid='+str(personid)
		response = requests.get(tempurl, data=self.data)
		print response