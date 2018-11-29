from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import os, shutil
from random import randint
import json
import time
import cv2

def scoreFrame(packet):
    frame_id = packet['frame_id']
    frame = cv2.imread(packet['original_frame'])

    label = randint(0, 3)
    level = 'low'
    if label == 1:
        level = 'moderate'
    if label == 2:
        level = 'high'
    if label == 3:
        level = 'extreme'

    print('Danger level for frame {}: {}'.format(frame_id, label))
    danger_mapping = {
        'low': (0, 255, 0),
        'moderate': (0, 255, 255),
        'high': (0, 165, 255),
        'extreme': (0, 0, 255)
    }
    result = frame.copy()
    cv2.rectangle(frame, (0, 0), (224, 224), danger_mapping[level], -1)
    cv2.addWeighted(frame, 0.3, result, 1 - 0.3,0, result)
    cv2.putText(result,'Danger Level: {}'.format(level),(25,25), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(255,255,255),1,cv2.LINE_AA)

    cv2.imwrite('/home/nvidia/Downloads/output/{}-result.jpg'.format(frame_id), result)

class SimpleEcho(WebSocket):

    def handleMessage(self):
        packet = json.loads(self.data)
        scoreFrame(packet)

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
