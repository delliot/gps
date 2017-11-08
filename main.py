'''
/*------------------------------------------------------------------------------------------------------------------
-- SOURCE FILE:		main.py - starts the program
-- PROGRAM:			GPSDPython
--
-- FUNCTIONS:
--					main()
--
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
-- Main function. Sets up the reader/printer and GPS receiver.
----------------------------------------------------------------------------------------------------------------------*/
'''
import os
from gps import *
from time import *
import time
import threading
import config
import GPS_Start
import GPS_Print
'''
/*--------------------------------------------------------------------------------------------------------------------
-- FUNCTION:		main
--
-- DATE:			November 7, 2017
--
-- REVISIONS:		N/A
--
-- DESIGNER:		Delan Elliot and Roger Zhang
--
-- PROGRAMMER:		Delan Elliot
--
-- INTERFACE:		main()
--
-- RETURNS:			void
--
-- NOTES:
-- Main function. Start up the program and creates a new thread for GPS reading. 
-- Print the gps coordinates every half a second until Ctrl-C is pressed to exit.
----------------------------------------------------------------------------------------------------------------------*/
'''

def main():
	global gpsd
	printGPS = GPS_Print.GPS_Print()
	readThread = GPS_Start.GPS_Start()
	readThread.start()
	time.sleep(1)
	try:
		while True:
			printGPS.GPS_Print(config.gpsd)
			time.sleep(.5)
	except(KeyboardInterrupt, SystemExit):
  		readThread.running = False
  		readThread.join()
  		print (' Exit Successful ')
if __name__=="__main__":
	main()
