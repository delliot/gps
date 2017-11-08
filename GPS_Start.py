'''
/*------------------------------------------------------------------------------------------------------------------
-- SOURCE FILE:		GPS_Start.py - starts the GPS reading
-- PROGRAM:			GPSDPython
--
-- FUNCTIONS:
--					__init__(self)
--					run(self)
--
-- DATE:			November 7, 2017
--
-- REVISIONS:		N/A
--
-- DESIGNER:		Delan Elliot, Roger Zhang
--
-- PROGRAMMER:		Roger Zhang
--
-- NOTES:
-- This is the gps reading class, it starts as a seperate thread and keeping reading for
-- for gps data.
----------------------------------------------------------------------------------------------------------------------*/
'''
import os
from gps3 import gps3
from time import *
import time
import threading
import config

class GPS_Start(threading.Thread):
	"""docstring for GPS_Start"""
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
	--
	-- RETURNS:			void
	--
	-- NOTES:
	-- This is the constructor where starts the stream of gps info and sets the gps object.
	----------------------------------------------------------------------------------------------------------------------*/
	'''
	def __init__(self):
		super(GPS_Start, self).__init__()
		print ("starting gps")
		#config.gpsd = gps(mode=WATCH_ENABLE)
		self.running = True
		config.socket = gps3.GPSDSocket()
		config.stream = gps3.DataStream()

		
	'''
	/*--------------------------------------------------------------------------------------------------------------------
	-- FUNCTION:		run
	--
	-- DATE:			November 7, 2017
	--
	-- REVISIONS:		N/A
	--
	-- DESIGNER:		Delan Elliot and Roger Zhang
	--
	-- PROGRAMMER:		Roger Zhang
	--
	-- INTERFACE:		run(self)
	--
	-- RETURNS:			void
	--
	-- NOTES:
	-- The running method will keep checking and update the gps object in the background, if there is new data available
	-- update the gps object, the timer is set to be every 5 seconds.
	----------------------------------------------------------------------------------------------------------------------*/
	'''
	def run(self):

		config.socket.connect()
		config.socket.watch()

		for data in config.socket:
			if not self.running:
				break
			if data:
				config.stream.unpack(data)
				config.gui.updateGui(config.stream)
			time.sleep(1)

