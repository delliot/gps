import os
from gps import *
from time import *
import time
import threading
import config

class GPS_Start(threading.Thread):
	"""docstring for GPS_Start"""
	def __init__(self):
		super(GPS_Start, self).__init__()
		#global  gpsd
		print "starting gps"
		config.gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
		self.running = True
		
	def run(self):
		while self.running:
			if config.gpsd.waiting():
				config.gpsd.next()
			time.sleep(5)
