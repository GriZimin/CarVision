from ultralytics import YOLO
from PIL import Image
from roboflow import Roboflow

# Тренировка
#model = YOLO("yolov8n.yaml")  # build a new model from scratch
#model.train(data="config.yaml", epochs=200, batch=2)

# Загрузка датасета
#from roboflow import Roboflow
#rf = Roboflow(api_key="")
#project = rf.workspace("wordspace").project("dataset-tlqkv")
#dataset = project.version(1).download("yolov8")

# Проверка
model = YOLO('runs/detect/train12/weights/best.pt')
img = Image.open('valpic.jpg')
results = model.predict(source=img, save=True)