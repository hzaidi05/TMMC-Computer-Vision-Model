from ultralytics import YOLO
import cv2

model = YOLO("/Users/sdey02/Downloads/TMMC_Challenge_Software/best.pt")
model.predict(source = "0", show=True, conf = .5)