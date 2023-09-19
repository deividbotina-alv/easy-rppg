import time
import os
import sys
import cv2
from logger import logging
import numpy as np
import pandas as pd
import argparse

from face_detector import FaceDetector, HaarCascade, Mediapipe
from utils import detect_face, draw_face_rectangle
from rppgs import RPPG, Green, GR

def rppg_from_file(file_path: str, face_detector: FaceDetector, RPPG_computer: RPPG, method: str, SHOW: bool):
    """
    Measure RPPG from a file.

    Args:
        file_path (str): Path to the file.
        face_detector (FaceDetector): An instance of a face detection class.
        RPPG_computer (RPPG): An instance of an RPPG measurement method class.
        method (str): The RPPG measurement method ('Green' or 'GR').
        SHOW (bool): Whether to show the video stream with face detection (True or False).

    Returns:
        None
    """
    output_path = os.path.dirname(file_path)
    
    video = cv2.VideoCapture(file_path) # Open the video file
 
    if not video.isOpened(): # Check if the video file was successfully opened
        logging.error(f"Impossible to open the file {file_path}")
        print(f"[ERROR] Impossible to open the file {file_path}")
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
            # Get R, G, B traces from the face
            x, y, w, h = face
            face_cropped = frame[y : y + h, x: x + w]
            traces.append(cv2.mean(face_cropped)[:3])
            if SHOW:
                draw_face_rectangle(frame, face) # Draw green rectangle
        else:
            traces.append((np.NaN, np.NaN, np.NaN))

        if SHOW:
            cv2.namedWindow("Video", cv2.WINDOW_AUTOSIZE)
            cv2.imshow("Video", frame) # Display the frame

        # Exit if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video file and close the window
    video.release()
    cv2.destroyAllWindows()

    # RPPG measurement
    rppg = RPPG_computer(traces)

    # Save the RPPG signal as a CSV file
    rppg_df = pd.DataFrame({'rppg': rppg})
    rppg_file_name = os.path.join(output_path, f'rppg_{method}.csv')
    rppg_df.to_csv(rppg_file_name, index=False)
    logging.info(f"Output file successfully saved in {rppg_file_name}")
    print(f"[SUCCESS] Output file successfully saved in {rppg_file_name}")

if __name__ == "__main__":
    print('================================================================')
    print('                         easy-rppg                              ')
    print('================================================================')
    print(time.strftime("%Y-%m-%d %H:%M:%S"))

    parser = argparse.ArgumentParser(description='RPPG measurement')
    parser.add_argument('--method', '-m', type=str, default='Green', choices=['Green', 'GR'],
                        help='RPPG measurement method (Green, GR)')
    parser.add_argument('--face_detector', '-fd', type=str, default='mediapipe', choices=['mediapipe', 'haarcascade'],
                        help='Face detection method (mediapipe or haarcascade)')
    parser.add_argument('--path', type=str, help='Path to the file (video or first enumerated image)')
    parser.add_argument('--RT', action='store_true', help='Real-time processing mode')
    parser.add_argument('--SHOW', action='store_true', help='Stream face detection')

    args = parser.parse_args()

    # Show parameters for this experiment
    for arg in vars(args):
        print(f'{arg} : {getattr(args, arg)}')
    print('================================================================')
    print('================================================================') 

    if not args.RT and args.path is None:
        logging.error("You must specify the input file path")
        print("[ERROR]: You must specify the input file path")
        sys.exit()

    # Load the pre-trained face detection model
    if args.face_detector in ['haarcascade']:
        face_detector = HaarCascade()
    elif args.face_detector in ['mediapipe']:
        face_detector = Mediapipe()

    # Instantiate the RPPG computer
    if args.method in ['Green']:
        RPPG_computer = Green()
    elif args.method in ['GR']:
        RPPG_computer = GR()

    if args.RT:
        """
        Real-time rppg measurement
        """
        logging.error(f"Real-time rppg measurement has not been implemented yet.")
        print("[ERROR] Real-time rppg measurement has not been implemented yet.")
        sys.exit()

    else:     
        """
        rppg measurement from file
        """
        logging.info(f"Measuring rppg from file")
        rppg_from_file(file_path=args.path,
                        face_detector=face_detector,
                        RPPG_computer=RPPG_computer,
                        method=args.method,
                        SHOW=args.SHOW)
