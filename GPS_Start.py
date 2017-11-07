'''
/*------------------------------------------------------------------------------------------------------------------
-- SOURCE FILE:		GPS_Start.py - starts the GPS reading
-- PROGRAM:			GPSDPython
--
-- FUNCTIONS:
--					init(self)
--					run(self)
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
-- 
----------------------------------------------------------------------------------------------------------------------*/
'''
import os
from gps import *
from time import *
import time
import threading
import config

class GPS_Start(threading.Thread):
	"""docstring for GPS_Start"""
	'''
	/*--------------------------------------------------------------------------------------------------------------------
	-- FUNCTION:		GPS_Start
	--
	-- DATE:			November 7, 2017
	--
	-- REVISIONS:		N/A
	--
	-- DESIGNER:		Delan Elliot and Roger Zhang
	--
	-- PROGRAMMER:		Delan Elliot and Roger Zhang
	--
	-- INTERFACE:		init(self)
	--
	--
	-- RETURNS:			void
	--
	-- NOTES:
	-- This is the constructor.
	----------------------------------------------------------------------------------------------------------------------*/
	'''
	def __init__(self):
		super(GPS_Start, self).__init__()
		#global  gpsd
		print "starting gps"
		config.gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
		self.running = True
		
	'''
	/*--------------------------------------------------------------------------------------------------------------------
	-- FUNCTION:		GPS_Start
	--
	-- DATE:			November 7, 2017
	--
	-- REVISIONS:		N/A
	--
	-- DESIGNER:		Delan Elliot and Roger Zhang
	--
	-- PROGRAMMER:		Delan Elliot and Roger Zhang
	--
	-- INTERFACE:		run(self)
	--
	--
	-- RETURNS:			void
	--
	-- NOTES:
	-- 
	----------------------------------------------------------------------------------------------------------------------*/
	'''
	def run(self):
		while self.running:
			if config.gpsd.waiting():
				config.gpsd.next()
			time.sleep(5)
