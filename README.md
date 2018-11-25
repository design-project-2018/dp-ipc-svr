# Design Project Socket Server

This repository holds a socket server used for communication between C++ and Python processes. Preprocessed frames from a C++ program will be sent in through the socket and piped into a Python method that will run the frames through a trained LSTM model for predicting required attention levels.

# Installation 

To run the websocket, run the following command to install the module:

```
sudo python setup.py install
```
# Running Server 

To start the server, run the following command:

```
python server.py
```

To test the socket, use the **socket-test.html** file to easily send commands.
