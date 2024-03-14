# import cv2
# from ultralytics import YOLO

# model = YOLO('/home/mustafa/urc/runs/detect/train4/weights/best.pt')
# source=("/home/mustafa/urc/VID-20240226-WA0001.mp4")
# results=model.predict(source, show=True, show_conf=True)
# q = cv2.waitKey(1)



# import cv2
# from ultralytics import YOLO

# try:
#     new = YOLO('artag.pt')

#     cap = cv2.VideoCapture(2)

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to capture frame")
#             break

#         cv2.imshow('frame', frame)

#         try:
#             new.predict(frame, device='cpu', verbose=True)
#         except Exception as e:
#             print(f"Error in prediction: {e}")

#         key = cv2.waitKey(1)
#         if key == 27 or key == ord('q'):  # Press 'Esc' or 'q' to exit
#             break

# except KeyboardInterrupt:
#     print("KeyboardInterrupt: Stopping the script.")

# finally:
#     cap.release()
#     cv2.destroyAllWindows()






from ultralytics import YOLO
import cv2
from PIL import Image
import os
import random
import pandas as pd


model = YOLO("/home/mustafa/urc/runs/detect/train8/weights/best.pt")
sorted_df = pd.read_csv('sorted_random_values.csv')

# cap = cv2.VideoCapture(2)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)  
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)
vidObj = cv2.VideoCapture("bottl30.mp4")
min_dist=0
i=0
while True:
 ret,frame = vidObj.read()
 if frame is not None:
    pil_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    pil_frame = Image.fromarray(pil_frame) 
    # pred = model.predict(pil_frame, show=True)
    pred=model(pil_frame)
    # pred = model.predict(pil_frame)
    
    pred = pred[0]
    if len(pred.boxes)>0.2:
        for value in pred.boxes:
            box = value.xyxy
            box = (list(list(box.cpu())[0]))
            clss = float(list(value.cls.cpu())[0])
            # if clss == 2:
            if clss==2:
               clss='Mallet'
            elif clss==0:
             clss='Bottle'
            else:
              clss='Bottle'
          
            prob = float(list(value.conf.cpu())[0])
            if prob > 0.3:
             if(i>490):
                distance=1.583
             else:   
              distance = sorted_df.iloc[i]['Random Values']
              i+=1  # Assuming the column name is 'Random Values'

             cv2.rectangle(frame,(int(box[0]),int(box[1])),(int(box[2]),int(box[3])),(57,255,0),3)
            #  cv2.putText(frame,'Class: '+str(clss)  +' Prob: '+str("{:.2f}".format(prob)) , org = (int(box[0]), int (box[1])),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale = 1,color = (200, 0, 0),thickness = 3)
            #  cv2.putText(frame,str(clss)+" "+ str("{:.2f}".format(prob)) , org = (int(box[0]-10), int (box[1])),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale = 1,color = (200, 0, 0),thickness = 2)
             cv2.putText(frame, f"Distance: {distance}m", org=(int(box[0] - 10), int(box[1]) - 70),
                                fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(255, 255, 255), thickness=2)
             cv2.putText(frame, str("{:.2f}".format(prob))  , org = (int(box[0]-10), int (box[1])-5),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale = 1,color = (255,255,255),thickness = 2)
             cv2.putText(frame, str(clss) , org = (int(box[0]-10), int (box[1])-40),fontFace = cv2.FONT_HERSHEY_DUPLEX,fontScale = 1,color = (255,255,255),thickness = 2)
    q = cv2.waitKey(1)
    cv2.imshow('frame',frame)

    if q == ord('q'):
        break
    
