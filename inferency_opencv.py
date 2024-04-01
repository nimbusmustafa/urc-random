# import cv2
# from ultralytics import YOLO
# import numpy as np
# import time

# try:
#     new = YOLO('/home/mustafa/urc/runs/detect/train18/weights/best.pt')

#     cap = cv2.VideoCapture(0)

#     count = 0
#     start = time.time()

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Perform object detection
#         results = new.predict(frame, device='cpu', verbose=True)

#         # Display the frame with detections
#         cv2.imshow('frame', results)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     end = time.time()

#     print('FPS: ', count / (end - start))

# except KeyboardInterrupt:
#     print("KeyboardInterrupt: Stopping the script.")

# finally:
#     cap.release()
#     cv2.destroyAllWindows()

from ultralytics import YOLO
import cv2
from PIL import Image
import os

model = YOLO("/home/mustafa/urc/runs/detect/train18/weights/best.pt")

cap = cv2.VideoCapture(2)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)  
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)

while True:
 ret,frame = cap.read()
 if frame is not None:
    pil_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    pil_frame = Image.fromarray(pil_frame) 
    # pred = model.predict(pil_frame, show=True)
    pred=model(pil_frame)
    # pred = model.predict(pil_frame)

    pred = pred[0]
    if len(pred.boxes)>0:
        for value in pred.boxes:
            box = value.xyxy
            box = (list(list(box.cpu())[0]))
            clss = float(list(value.cls.cpu())[0])
            # if clss == 2:
            if clss==2:
               clss='Cone'
            elif clss==0:
             clss='Artag'
            else:
              clss='Left'
            prob = float(list(value.conf.cpu())[0])
            cv2.rectangle(frame,(int(box[0]),int(box[1])),(int(box[2]),int(box[3])),(200,0,0),2)
            cv2.putText(frame,'Class: '+str(clss)  +' Prob: '+str(prob) , org = (100, 100),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale = 1,color = (200, 0, 0),thickness = 3)

    q = cv2.waitKey(1)
    cv2.imshow('frame',frame)

    if q == ord('q'):
        break
    
