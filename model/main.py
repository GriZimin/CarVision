from ultralytics import YOLO
from PIL import Image
import cv2

from roboflow import Roboflow

# Тренировка
"""model = YOLO("yolov8n.yaml")  # build a new model from scratch
model.train(data="config.yaml", epochs=1)"""

# Загрузка датасета
#from roboflow import Roboflow
#rf = Roboflow(api_key="")
#project = rf.workspace("wordspace").project("dataset-tlqkv")
#dataset = project.version(1).download("yolov8")

# Проверка
#model = YOLO('runs/detect/train12/weights/best.pt')
#img = cv2.imread("valpic.jpg")
#results = model.predict(img)
#for result in results:
#    boxes = result.boxes.cpu().numpy()
#    xyxys = boxes.xyxy
#    for xyxy in xyxys:
#        cv2.rectangle(img, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0, 255, 0), thickness=8)
#img = cv2.resize(img, (711, 430), interpolation=cv2.INTER_LINEAR)
#cv2.imshow('Image', img)
#cv2.waitKey(0)

names = ['barricade', 'crossing', 'person']
colors = [(0,0,255), (0,255,0), (255,255,0)]
def detect(image):
    model = YOLO('model/runs/detect/train12/weights/best.pt')
    results = model.predict(image)
    # for result in results:
    #     boxes = result.boxes.cpu().numpy()
    #     xyxys = boxes.xyxy
    #     print(boxes.cls)
    #     for i in range(len(xyxys)):
    # cv2.rectangle(image, (int(xyxys[i][0]), int(xyxys[i][1])), (int(xyxys[i][2]), int(xyxys[i][3])),
    #               colors[int(boxes.cls[i])], thickness=3)
    # cv2.putText(image, names[int(boxes.cls[i])], (int(xyxys[i][0]), int(xyxys[i][1])), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
    #             colors[int(boxes.cls[i])], thickness=3, lineType=3)
    #
    # image = cv2.resize(image, (711, 430), interpolation=cv2.INTER_LINEAR)
    boxes = results[0].boxes.cpu().numpy()
    xyxys = boxes.xyxy
    cls = boxes.cls
    return xyxys, cls
