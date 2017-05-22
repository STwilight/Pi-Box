from SimpleWebSocketServer import SimpleSSLWebSocketServer, WebSocket
import wiringpi

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


class socketHandler(WebSocket):

    def handleMessage(self):
        # echo message back to client
		msg = self.data
		if msg == "ledon":
			wiringpi.digitalWrite(LED_GRN, ON)
		elif msg == "ledoff":
			wiringpi.digitalWrite(LED_GRN, OFF)
		self.sendMessage(msg)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')


init()
wssServer = SimpleSSLWebSocketServer('', 9800, socketHandler, '/home/pi-box/cert/certificate.crt', '/home/pi-box/cert/private.key')
wssServer.serveforever()