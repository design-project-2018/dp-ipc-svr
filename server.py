from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import os, shutil
from random import randint
import json
import time

def scoreFrame(packet):
    frame_id = packet['frame_id']
    frame = cv2.imread(packet['original_frame'])

    label = randint(0, 3)
    color = (0, 0, 255)
    if label == 1:
        color = (255, 0, 255)
    if label == 2:
        color = (0, 255, 0)
    if label == 3:
        color = (255, 0, 0)
    print('Danger level: {}'.format(label))
    cv2.rectangle(frame, (0, 0), (224, 224), color, -1)
    cv2.imwrite('/home/nvidia/Downloads/output/{}-result.jpg'.format(frame_id), frame)

class SimpleEcho(WebSocket):

    def handleMessage(self):
        packet = json.loads(self.data)
        
        frame_id = packet['frame_id']
        frame = cv2.imread(packet['original_frame'])

        label = randint(0, 3)
        color = (0, 0, 255)
        if label == 1:
            color = (255, 0, 255)
        if label == 2:
            color = (0, 255, 0)
        if label == 3:
            color = (255, 0, 0)
        print('Danger level: {}'.format(label))
        cv2.rectangle(frame, (0, 0), (224, 224), color, -1)
        cv2.imwrite('/home/nvidia/Downloads/output/{}-result.jpg'.format(frame_id), frame)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

def startServer():
    # removed cached files
    print('Removing cached files')
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
