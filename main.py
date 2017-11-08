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
from gps3 import gps3
from time import *
import time
import tkinter
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
	print('START')

	top = tkinter.Tk()
	window = tkinter.PanedWindow(top, orient=tkinter.VERTICAL)
	canvas = tkinter.Canvas(top, width=config.width, height=config.height)
	bg = tkinter.PhotoImage(file='map1024x512.gif')

	canvas.create_image((config.width/2), (config.height/2), image=bg)
	text = tkinter.Text(top)
	text.configure(state="disabled")
	config.textBox = text
	config.canvas = canvas


	window.add(canvas)
	window.add(text)
	window.pack()

	config.gui = GPS_Print.GPS_Print()
	readThread = GPS_Start.GPS_Start()
	readThread.start()

	top.mainloop()

	readThread.running = False
	readThread.join()

if __name__=="__main__":
	main()
