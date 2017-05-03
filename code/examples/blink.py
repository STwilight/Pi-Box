from threading import Timer
from time import sleep
import wiringpi

# Information
#	https://docs.python.org/3/library/threading.html#timer-objects

# Constant values definition
LED_RED = 4
LED_GRN = 5
ON		= 1
OFF		= 0
INPUT	= 0
OUTPUT	= 1
DELAY	= 250
PERIOD  = 0.5
SLEEP	= 3
COUNT	= 5

# Variables definition
counter = 0

# Methods definition
def setPin(pin_name, pin_state):
	wiringpi.digitalWrite(pin_name, pin_state)

def getPin(pin_name):
	return wiringpi.digitalRead(pin_name)

def togglePin(pin_name):
	setPin(pin_name, not getPin(pin_name))

def alloff():
	wiringpi.digitalWrite(LED_RED, OFF)
	wiringpi.digitalWrite(LED_GRN, OFF)

def delay_cycle():
	global counter
	setPin(LED_RED, ON)
	while counter < COUNT:
		togglePin(LED_RED)
		wiringpi.delay(DELAY)
		togglePin(LED_RED)
		wiringpi.delay(DELAY)
		counter += 1
	setPin(LED_RED, OFF)

def timer_cycle():
	timer = Timer(PERIOD, timer_cycle)
	togglePin(LED_GRN)
	timer.start()

def init():
	wiringpi.wiringPiSetup()
	wiringpi.pinMode(LED_RED, OUTPUT)
	wiringpi.pinMode(LED_GRN, OUTPUT)
	alloff()

# Main program
init()
timer_cycle()
sleep(SLEEP)
delay_cycle()