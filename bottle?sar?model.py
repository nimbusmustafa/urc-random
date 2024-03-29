import ultralytics
ultralytics.checks()
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(data="/home/mustafa/urc/databottle.yaml",epochs=400, batch=24, val=False, fliplr=0.3,cache=True, dropout=0.3, weight_decay=0.001, patience = 20)