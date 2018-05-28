import signal
import flicklib
import time
def message(value):
   print value
@flicklib.move()
def move(x, y, z):
   global xyztxt
   xyztxt = '{:5.3f} {:5.3f} {:5.3f}'.format(x,y,z)
@flicklib.flick()
def flick(start,finish):
   global flicktxt
   flicktxt = 'FLICK-' + start[0].upper() + finish[0].upper()
   message(flicktxt)
def main():
   global xyztxt
   global flicktxt
   xyztxt = ''
   flicktxt = ''
   flickcount = 0
   while True:

	xyztxt = ''
	if len(flicktxt) > 0 and flickcount < 5:
    	flickcount += 1
	else:
      flicktxt = ''
      flickcount = 0
main()