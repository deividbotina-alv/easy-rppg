import time
import cv2

if __name__ == "__main__":
    print('================================================================')
    print('                         easy-rppg                              ')
    print('================================================================')
    print(time.strftime("%Y-%m-%d %H:%M:%S"))

    face_detector = 'mediapipe'#['mediapipe','haarcascade']
    RT = False # Real time

    if not RT:
        path = 'video' # ['video','images']

        rppg_from_video(path)