import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('', 443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, certfile='/home/pi-box/cert/certificate.crt', keyfile='/home/pi-box/cert/private.key', ssl_version=ssl.PROTOCOL_TLSv1)
httpd.serve_forever()