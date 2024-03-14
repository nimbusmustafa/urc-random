import ultralytics
ultralytics.checks()
from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/last.pt")
model.train(data="/home/mustafa/urc/data.yaml", batch=24, val=False, fliplr=0.3,cache=True, dropout=0.3, weight_decay=0.001, patience = 20,save=True,resume=True)