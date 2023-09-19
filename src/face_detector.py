import cv2
import mediapipe as mp
import numpy as np

class FaceDetector:
    def __init__(self):
        pass

    def compute(self, input):
        raise NotImplementedError("Subclasses must implement the compute method.")

    def __call__(self, input):
        return self.compute(input)
    
class HaarCascade(FaceDetector):
    def __init__(self):
        super().__init__()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def compute(self, input):
        gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        return faces

class Mediapipe(FaceDetector):
    def __init__(self, min_detection_confidence:float=0.5):
        super().__init__()
        self.min_detection_confidence = min_detection_confidence
        self.mp_face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=self.min_detection_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    def compute(self, input):
        results = self.mp_face_detection.process(input)

        faces = []
        if results.detections:
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box
                h, w, c = input.shape
                x, y, width, height = int(bbox.xmin * w), int(bbox.ymin * h), int(bbox.width * w), int(bbox.height * h)
                faces.append((x, y, width, height))

        return faces