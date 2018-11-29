from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import os, shutil
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

def startServer():
    # removed cached files
    folder = '/home/nvidia/Downloads/output/'
    for f in os.listdir(folder):
        file_path = os.path.join(folder, f)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
    # start websocket server
    print('Starting websocket server')
    server = SimpleWebSocketServer('', 8000, SimpleEcho)
    server.serveforever()
