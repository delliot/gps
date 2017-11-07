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
-- PROGRAMMER:		Delan Elliot, Roger Zhang
--
-- NOTES:
-- This is the gps reading class, it starts as a seperate thread and keeping reading for
-- for gps data.
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
	-- FUNCTION:		__init__
	--
	-- DATE:			November 7, 2017
	--
	-- REVISIONS:		N/A
	--
	-- DESIGNER:		Delan Elliot and Roger Zhang
	--
	-- PROGRAMMER:		Delan Elliot and Roger Zhang
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
		#global  gpsd
		print "starting gps"
		config.gpsd = gps(mode=WATCH_ENABLE)
		self.running = True
		
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
	-- PROGRAMMER:		Delan Elliot and Roger Zhang
	--
	-- INTERFACE:		run(self)
	--
	-- RETURNS:			void
	--
	-- NOTES:
	-- This is the background running function. The running method will keep checking and update the gps object.
	-- Timer is set to be 5 seconds.
	----------------------------------------------------------------------------------------------------------------------*/
	'''
	def run(self):
		while self.running:
			if config.gpsd.waiting():
				config.gpsd.next()
			time.sleep(5)
