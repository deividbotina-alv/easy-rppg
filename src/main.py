import time
import cv2
from exception import CustomException
from logger import logging

def rppg_from_file(file_path:str):
    
    video = cv2.VideoCapture(file_path) # Open the video file
 
    if not video.isOpened(): # Check if the video file was successfully opened
        logging.info(f"Error when opening video file {file_path}")
        print("Error opening video file")
        return

    # Read and display each frame of the video
    while True:
        ret, frame = video.read() # Check if the frame was successfully read

        if not ret:
            break

        cv2.namedWindow("Video", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Video", frame)# Display the frame

        # Exit if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video file and close the window
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print('================================================================')
    print('                         easy-rppg                              ')
    print('================================================================')
    print(time.strftime("%Y-%m-%d %H:%M:%S"))

    face_detector = 'mediapipe'#['mediapipe','haarcascade']
    RT = False # Real time

    if not RT:
        path = r'/media/dvd/DATA/repos/easy-rppg/data/p1v1s1/video1.avi'
        rppg_from_file(path)