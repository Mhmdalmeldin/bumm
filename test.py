#!/usr/bin/env python3
import grpc
import faceid_ai_pb2_grpc
import faceid_ai_pb2
import cv2

cam = cv2.VideoCapture(0)

cam.set(3, 320)
cam.set(4, 240)
#encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
ret, frame = cam.read()
result, encodedimg = cv2.imencode('.webp', frame)

myimage = encodedimg
myid = 1900
with grpc.insecure_channel('localhost:50051') as channel:
    stub = faceid_ai_pb2_grpc.FaceIdAiStub(channel)
    response = stub.BeAtYourDesk(
        faceid_ai_pb2.EmployeeInfo(
            id=myid, image=faceid_ai_pb2.Image(encoded_image=bytes(myimage))))
    print(response.status)
