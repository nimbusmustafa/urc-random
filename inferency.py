import cv2
from ultralytics import YOLO

model = YOLO('/home/mustafa/urc/runs/detect/train8/weights/best.pt')
source=("/home/mustafa/urc/bottl30.mp4")
results=model.predict(source, show=True, show_conf=True)
