#!/usr/bin/env python3
import grpc
import faceid_ai_pb2_grpc
import faceid_ai_pb2
import cv2
import io
import sys
import time


cam = cv2.VideoCapture(0)

cam.set(3, 620)
cam.set(4, 440)
#encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
ret, frame = cam.read()
result, encodedimg = cv2.imencode('.webp', frame)

cam = cv2.VideoCapture(0)

cam.set(3, 620)
cam.set(4, 440)
# encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

file2 = open(r"C:\Intel\config.txt", "r")
myid=int(file2.read())

file2.close()

absence = 0
myimage = encodedimg
# serverip = sys.argv[1]
#192.168.137.142
with grpc.insecure_channel('192.168.137.142:50051') as channel:
    while True :

        ret, frame = cam.read()
        result, encodedimg = cv2.imencode('.webp', frame)
        myimage = encodedimg

        stub = faceid_ai_pb2_grpc.FaceIdAiStub(channel)
        response = stub.BeAtYourDesk(
            faceid_ai_pb2.EmployeeInfo(
                id=myid, image=faceid_ai_pb2.Image(encoded_image=bytes(myimage))))
        if response.status :
            try:
                time.sleep(10)
                absence=0
            except KeyboardInterrupt:
                pass
        else :
            response2 = stub.RecordTimeData(faceid_ai_pb2.TimeData(id = myid, is_absent = False))
            print("OK")
            time.sleep(5)
            response3 = stub.GetAllowedDuration(faceid_ai_pb2.Null())
            print(response3.time)
            time.sleep(5)
            response4 = stub.SetupService(faceid_ai_pb2.EmployeeId(id=myid))
            print(response4.status)
            try:
                time.sleep(3)
            except KeyboardInterrupt:
                pass



cam.release()
