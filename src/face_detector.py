import cv2

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
