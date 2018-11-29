from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
import time

class SimpleEcho(WebSocket):

    def handleMessage(self):
        packet = json.loads(self.data)
        print(packet)
        print('\n\n')
        time.sleep(5)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('', 8000, SimpleEcho)
server.serveforever()
