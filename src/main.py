import time
import cv2
from exception import CustomException
from logger import logging
import numpy as np

from face_detector import HaarCascade, Mediapipe
from utils import PreserveFPS, detect_face, draw_face_rectangle
from rppgs import Green, GR

def rppg_from_file(file_path:str, face_detector, RPPG_computer):
    
    video = cv2.VideoCapture(file_path) # Open the video file
 
    if not video.isOpened(): # Check if the video file was successfully opened
        logging.info(f"Error when opening video file {file_path}")
        print("Error opening video file")
        return
    else:
        logging.info(f"Success when opening video file {file_path}")

    # Read and display each frame of the video
    traces = []

    while True:
        ret, frame = video.read() # Check if the frame was successfully read

        if not ret:
            break

        face = detect_face(face_detector, frame) # Face detection (coordinates)
        if face is not None:
            # Get R,G,B traces from the face
            x, y, w, h = face
            face_cropped = frame[y : y + h, x: x + w]
            traces.append(cv2.mean(face_cropped)[:3])
            draw_face_rectangle(frame, face) # Draw green rectangle
        else:
            traces.append((np.NaN, np.NaN, np.NaN))

        cv2.namedWindow("Video", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Video", frame)# Display the frame

        # Exit if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video file and close the window
    video.release()
    cv2.destroyAllWindows()

    # RPPG measurement
    rppg = RPPG_computer(traces)
    import matplotlib.pyplot as plt
    plt.figure(); plt.plot(rppg)

if __name__ == "__main__":
    print('================================================================')
    print('                         easy-rppg                              ')
    print('================================================================')
    print(time.strftime("%Y-%m-%d %H:%M:%S"))

    face_detector = 'mediapipe'#['mediapipe','haarcascade']
    method = 'Green' # ['Green', 'GR', 'POS']

    # Load the pre-trained face detection model
    if face_detector in ['haarcascade']:
        face_detector = HaarCascade()
    elif face_detector in ['mediapipe']:
        face_detector = Mediapipe()

    if method in ['Green']:
        RPPG_computer = Green()
    elif method in ['GR']:
        RPPG_computer = GR()


    RT = False # Real time

    if not RT:
        path = r'/media/dvd/DATA/repos/easy-rppg/data/p1v1s1/video.avi'
        rppg_from_file(path, face_detector, RPPG_computer)