import os
from gps import *
from time import *
import time
import threading
import config
import GPS_Start
import GPS_Print

def main():
	global gpsd
	print('START')
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
  		print ' Exit Successful '
if __name__=="__main__":
	main()
