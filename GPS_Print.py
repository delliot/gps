'''
/*------------------------------------------------------------------------------------------------------------------
-- SOURCE FILE:		GPS_Print.py - prints the GPS data
-- PROGRAM:			GPSDPython
--
-- FUNCTIONS:
--					__init__(self)
--					convertTODMS(float)
--					GPS_Print(self, GPS_Object)
--
-- DATE:			November 7, 2017
--
-- REVISIONS:		N/A
--
-- DESIGNER:		Delan Elliot, Roger Zhang
--
-- PROGRAMMER:		Delan Elliot, Roger Zhang
--
-- NOTES:
-- The GPS print class takes in the GPS object and prints out the gps information to the console.
----------------------------------------------------------------------------------------------------------------------*/
'''
import os
from gps import *
from time import *
import time
import threading
import config
import math

class GPS_Print(object):
	'''
	/*--------------------------------------------------------------------------------------------------------------------
	-- FUNCTION:		__init__
	--
	-- DATE:			November 7, 2017
	--
	-- REVISIONS:		N/A
	--
	-- DESIGNER:		Delan Elliot and Roger Zhang
	--
	-- PROGRAMMER:		Roger Zhang
	--
	-- INTERFACE:		__init__(self)
	--
	-- RETURNS:			void
	--
	-- NOTES:
	-- This is the constructor for GPS_Print.
	----------------------------------------------------------------------------------------------------------------------*/
	'''
	"""docstring for GPS_Print"""
	def __init__(self):
		f = 0

	'''
	/*--------------------------------------------------------------------------------------------------------------------
	-- FUNCTION:		convertTODMS
	--
	-- DATE:			November 7, 2017
	--
	-- REVISIONS:		N/A
	--
	-- DESIGNER:		Delan Elliot and Roger Zhang
	--
	-- PROGRAMMER:		Roger Zhang
	--
	-- INTERFACE:		convertTODMS(float)
	--
	-- RETURNS:			String
	--
	-- NOTES:
	-- This is the conversion function that converts the latitude/longitude to Degrees,
	-- Minutes, Seconds and directions.
	----------------------------------------------------------------------------------------------------------------------*/
	'''
	def convertTODMS(self, lat, latlong):
		if not math.isnan(lat):
			directionLat = ''
			if latlong == 0
				directionLat = ' N' if lat > 0 else ' S'
			else
				directionLat = ' E' if lat > 0 else ' W'
			dd = int(lat)
			mm = int((lat-int(lat))*60)
			ss = (((lat-int(lat))*60) - mm) * 60
			print ('Degrees: ' + str(dd) + ' minutes: ' + str(mm) + ' seconds: ' + str(ss) + directionLat)
		else:
			print ('not available')
	'''
	/*--------------------------------------------------------------------------------------------------------------------
	-- FUNCTION:		GPS_Print
	--
	-- DATE:			November 7, 2017
	--
	-- REVISIONS:		N/A
	--
	-- DESIGNER:		Delan Elliot and Roger Zhang
	--
	-- PROGRAMMER:		Roger Zhang
	--
	-- INTERFACE:		GPS_Print(self, GPS_Object)
	--
	-- RETURNS:			void
	--
	-- NOTES:
	-- This is the printing method that prints out the gps coordinates and data.
	----------------------------------------------------------------------------------------------------------------------*/
	'''
	def GPS_Print(self, gpsd):
		#os.system('clear')
		
		print ('----------GPS data----------')
		print ('Time (UTC):    ' , gpsd.utc,' + ', gpsd.fix.time)
		print ('Latitude:    ' , self.convertTODMS(gpsd.fix.latitude, 0))
		print ('Longitude:   ' , self.convertTODMS(gpsd.fix.longitude, 1))
		print ('Elevation (m): ' , gpsd.fix.altitude)
		print ('Speed m/s      ' , gpsd.fix.speed)
		print ('Climb          ' , gpsd.fix.climb)
		print ('Track          ' , gpsd.fix.track)
		print ('Mode           ' , gpsd.fix.mode)
		for i in gpsd.satellites:
			print ('\t', i)
			