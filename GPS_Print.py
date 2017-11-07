import os
from gps import *
from time import *
import time
import threading
import config

class GPS_Print(object):
	"""docstring for GPS_Print"""
	def __init__(self):
		#global gpsd
		f = 0


	def convertTODMS(lat):
		dd = int(lat)
		mm = int(lat-int(lat) * 60)
		ss = ((lat-int(lat)*60) - mm) * 60
		return 'Degrees: ' + dd + 'minutes: ' + mm + 'seconds: ' + ss
	
	def GPS_Print(self, gpsd):
			#os.system('clear')
			
			print ' GPS data '
	  		print 'Time (UTC):    ' , gpsd.utc,' + ', gpsd.fix.time
	  		print 'Latitude:    ' , convertTODMS(gpsd.fix.latitude)
	  		print 'Longitude:   ' , convertTODMS(gpsd.fix.longitude)
	  		print 'Elevation (m): ' , gpsd.fix.altitude
			print 'Satellites: ' , gpsd.satellites
	  		#print 'PRN: ' , gpsd.fix.PRN
	  		#print 'Azimuth: ' , gpsd.fix.Azimuth
	  		#print 'SNR: ' , gpsd.fix.SNR
	  		#print 'Used flag: ' , gpsd.fix.used


