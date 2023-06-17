import grpc
import faceid_ai_pb2_grpc
import faceid_ai_pb2
import cv2


cam = cv2.VideoCapture(0)

cam.set(3, 320);
cam.set(4, 240);
#encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
ret, frame = cam.read()
result, encodedimg = cv2.imencode('.webp', frame)

myimage = encodedimg
myid = 19
with grpc.insecure_channel('localhost:50051') as channel:
    stub = faceid_ai_pb2_grpc.OurServiceStub(channel)
    response = stub.ids(faceid_ai_pb2.Request1(id=myid))
    response = stub.images(faceid_ai_pb2.Request2(image=myimage))
    print(response.message)