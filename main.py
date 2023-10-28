from ultralytics import YOLO
import cv2

model = YOLO("")
model.predict(source = "0", show=True, conf = .5)