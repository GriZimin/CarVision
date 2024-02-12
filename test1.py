import cv2
import numpy as np
import tensorflow as tf
from imageai.Detection import ObjectDetection

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo-tiny.h5")
detector.loadModel(1)

detector.detectObjectsFromImage(input_image="123.jpg",output_type="new_image.jpg")
