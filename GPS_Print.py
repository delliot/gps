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
	def convertToDMS(self, lat, latlong):
		if not lat == 'n/a':
			directionLat = ''
			if latlong == 0:
				directionLat = ' N' if lat > 0 else ' S'
			else:
				directionLat = ' E' if lat > 0 else ' W'
			dd = int(lat)
			mm = int((lat-int(lat))*60)
			ss = (((lat-int(lat))*60) - mm) * 60
			return str('Degrees: ' + str(dd) + ' minutes: ' + str(mm) + ' seconds: ' + str(ss) + directionLat)
		else:
			return str('not available')

	'''
	/*--------------------------------------------------------------------------------------------------------------------
	-- FUNCTION:		updateGui
	--
	-- DATE:			November 7, 2017
	--
	-- REVISIONS:		N/A
	--
	-- DESIGNER:		Delan Elliot 
	--
	-- PROGRAMMER:		Delan Elliot
	--
	-- INTERFACE:		updateGui(self, data)
	-- 					
	--						data: python dictionary generated by gps3 socket
	--
	-- RETURNS:			void
	--
	-- NOTES:
	-- This method updates the gui and is called each time the gps read thread gets new data. 
	-- It updates the canvas and text elements. The canvas element is called by plotOnCanvas 
	-- method which is called here. 
	----------------------------------------------------------------------------------------------------------------------*/
	'''
	def updateGui(self, data):
		print('----------GPS Data----------')
		print('Time: ', data.TPV['time'])
		print('Latitude: ', self.convertToDMS(data.TPV['lat'], 0))
		print('Longitude: ', self.convertToDMS(data.TPV['lon'], 1))
		print('Elevation (m): ', data.TPV['alt'])
		print('Speed (m/s): ', data.TPV['speed'])
		print('Climb: ', data.TPV['climb'])
		print('Satellites:')
		if isinstance(data.SKY['satellites'], list):
			for i in data.SKY['satellites']:
				print('\t', i)
		else:
			print(' N/A ')
		if data.TPV['lat'] != "n/a" and data.TPV['lon'] != "n/a":
			self.plotOnCanvas(config.canvas, data.TPV['lon'], data.TPV['lat'])

		config.textBox.configure(state="normal")
		config.textBox.delete('1.0', tkinter.END)
		config.textBox.insert(tkinter.END, '----------GPS data----------')
		config.textBox.insert(tkinter.END, 'Time (UTC):    ' + data.TPV['time'] + '\n')
		config.textBox.insert(tkinter.END, 'Latitude: ' + self.convertToDMS(data.TPV['lat'], 0) + '\n')
		config.textBox.insert(tkinter.END, 'Longitude: ' + self.convertToDMS(data.TPV['lon'], 1) + '\n')
		config.textBox.insert(tkinter.END, 'Elevation (m): ', data.TPV['alt'] + '\n')

		if isinstance(data.SKY['satellites'], list):
			config.textBox.insert(tkinter.END, 'Satellites: \n')
			for s in data.SKY['satellites']:
				config.textBox.insert(tkinter.END, s + '\n')
		else:
			config.textBox.insert(tkinter.END, 'No Satellites \n')
		config.textBox.configure(state="disabled")



	def toWebMercator(self, xLon, yLat):
		m_lon = deg2rad(xLon)
		m_lat= deg2rad(yLat)


		x = int((256 / pi) * 2 * (m_lon + pi))
		y = int(((256 / pi) * 2) * (pi - log((tan(pi / 4 + m_lat / 2)))))

		return x, y

	def plotOnCanvas(self, canvas, x, y):

		pixels = self.toWebMercator(x, y)
		center = self.toWebMercator(0,0)
		pos = int(pixels[0] - center[0] + 500), int(pixels[1] - center[1] + 256)
		canvas.create_oval(pos[0], pos[1], pos[0] + 20, pos[1] + 20)
