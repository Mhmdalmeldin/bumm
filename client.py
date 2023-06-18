import cv2
import io
import sys
import socket
import struct
import time
import pickle
import zlib
from tkinter import *
import tkinter.messagebox

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect(('127.0.0.1', 5432))
except ConnectionRefusedError:
    pass
connection = client_socket.makefile('wb')

cam = cv2.VideoCapture(0)

cam.set(3, 320);
cam.set(4, 240);

first = 'ayman'
first = str(first)

bum = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

try:
    while True:
        try:
            ret, frame = cam.read()
            result, frame = cv2.imencode('.jpg', frame, encode_param)
            #    data = zlib.compress(pickle.dumps(frame, 0))
            data = pickle.dumps(frame, 0)
            size = len(data)

            try:
                client_socket.send(first.encode());
            except OSError:
                pass


            try:
                client_socket.sendall(struct.pack(">L", size) + data)
            except OSError:
                pass



            if client_socket.recv(1024).decode() == "Y":
                time.sleep(6)
                bum = 0
            else:
                time.sleep(2)
                bum = bum +1
                if bum == 3 :
                    tkinter.messagebox.showinfo("Warning!!!", "Focus on your woek bruh")
        except :
            try:
                client_socket.connect(('127.0.0.1', 5432))
            except OSError:
                pass

    cam.release()
except KeyboardInterrupt:
    pass