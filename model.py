import os
import cv2
from ultralytics import YOLO
orb = cv2.ORB_create(1000)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
model = YOLO("yolo11n.pt")
def get_class(image):
    resultado = model(image)
    if len(resultado[0].boxes) > 0:
        classe = resultado[0].names[
            int(resultado[0].boxes.cls[0])
        ]
        confianca = float(
            resultado[0].boxes.conf[0]
        )
        return classe, confianca
    else:
        return "Desconhecido", 0