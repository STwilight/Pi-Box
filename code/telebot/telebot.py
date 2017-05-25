from telegram.ext import Updater, CommandHandler
import wiringpi
import sys

LED_GRN = 5
ON		= 1
OFF		= 0
INPUT	= 0
OUTPUT	= 1


def init():
	wiringpi.wiringPiSetup()
	wiringpi.pinMode(LED_GRN, OUTPUT)
	wiringpi.digitalWrite(LED_GRN, OFF)

def setPin(pin_name, pin_state):
	wiringpi.digitalWrite(pin_name, pin_state)


def start(bot, update):
	update.message.reply_text('I\'m the Pi-Box bot!')

def ledon(bot, update):
	wiringpi.digitalWrite(LED_GRN, ON)
	update.message.reply_text('LED On!')
	
def ledoff(bot, update):
	wiringpi.digitalWrite(LED_GRN, OFF)
	update.message.reply_text('LED Off!')

def check(bot, update):
	if(wiringpi.digitalRead(LED_GRN)):
		update.message.reply_text('LED is ON.')
	else:
		update.message.reply_text('LED is OFF.')
		
def shutdown(bot, update):
	update.message.reply_text('Shutting down the script...')
	updater.stop()
	print 'Bot was stopped by the command!'
	sys.exit(0)


if(len(sys.argv)>1):
	init()
	updater = Updater(sys.argv[1])
	updater.dispatcher.add_handler(CommandHandler('start', start))
	updater.dispatcher.add_handler(CommandHandler('ledon', ledon))
	updater.dispatcher.add_handler(CommandHandler('ledoff', ledoff))
	updater.dispatcher.add_handler(CommandHandler('check', check))
	# command not included in official /cmd list
	updater.dispatcher.add_handler(CommandHandler('shutdown', shutdown))
	updater.start_polling()
	updater.idle()
else:
	sys.exit('Telegram bot token ID must be specified as first option!')