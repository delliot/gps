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
from gps3 import gps3
from time import *
import time
import threading
import tkinter
import config
from numpy import *
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
		print("starting")


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
			if latlong == 0:
				directionLat = ' N' if lat > 0 else ' S'
			else:
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
	def updateGui(self, data):
		print('time: ', data.TPV['time'])
		print('Lat: ', data.TPV['lat'])
		if data.TPV['lat'] != "n/a" and data.TPV['lon'] != "n/a":
			plotOnCanvas(config.canvas, data.TPV['lon'], data.TPV['lat'])



		config.textBox.configure(state="normal")
		config.textBox.delete('1.0', tkinter.END)
		config.textBox.add(tkinter.END, '----------GPS data----------')
		config.textBox.add(tkinter.END, 'Time (UTC):    ' + data.TPV['time'])
		config.textBox.configure(state="disabled")

		'''
			config.textBox.add('Latitude:    ', self.convertTODMS(gpsd.fix.latitude))
			config.textBox.add('Longitude:   ', self.convertTODMS(gpsd.fix.longitude))
			config.textBox.add('Elevation (m): ', gpsd.fix.altitude)
			config.textBox.add('Satellites: ', gpsd.satellites)
			for i in gpsd.satellites:
				config.textBox.add('\t', i)

			
			time.sleep(.5)

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
''' 

def toWebMercator(xLon, yLat):
	m_lon = deg2rad(xLon)
	m_lat= deg2rad(yLat)


	x = int((256 / pi) * 2 * (m_lon + pi))
	y = int(((256 / pi) * 2) * (pi - log((tan(pi / 4 + m_lat / 2)))))

	return x, y

def plotOnCanvas(canvas, x, y):

	pixels = toWebMercator(x, y)
	center = toWebMercator(0,0)
	pos = int(pixels[0] - center[0] + 500), int(pixels[1] - center[1] + 256)
	canvas.create_oval(pos[0], pos[1], pos[0] + 20, pos[1] + 20)
