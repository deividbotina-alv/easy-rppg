"""
Created on Fri May 26 2023
Last modification: 26/05/2023
@authors: HenRick, Deivid

Description: This file defines a FaceDetector class that uses the OpenCV library to
detect faces in real-time video frames.
"""

import cv2

class FaceDetector:
    def __init__(self):
        # Load the face cascade classifier
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Create a video capture object
        self.video_capture = cv2.VideoCapture(0)

    def detect_face(self, frame):
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            # Return the first detected face
            return faces[0]
        else:
            return None

    @staticmethod
    def extract_face_roi(frame, face):
        # Extract the region of interest (ROI) containing the face from the frame
        x, y, w, h = face
        face_roi = frame[y:y+h, x:x+w]
        return face_roi

    @staticmethod
    def draw_face_rectangle(frame, face):
        # Draw a green rectangle around the detected face
        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    @staticmethod
    def display_frame(frame):
        # Display the frame in the first window
        cv2.imshow('Camera Capture', frame)

    def release(self):
        # Release the video capture and close the first window
        self.video_capture.release()
        cv2.destroyAllWindows()
