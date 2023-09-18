"""
Created on Fri May 26 2023
Last modification: 26/05/2023
@authors: HenRick, Deivid

Description: This code uses a face detector to detect faces in real-time video frames
and applies remote photoplethysmography (RPPG) to estimate physiological signals.
It displays the video feed with a green square around the detected face in one window,
while showing the real-time plot of the normalized RPPG signal in a separate window.
"""

import cv2
from face_detector import FaceDetector
from rppg import RPPG, RPPGPlot

def main():
    # Create an instance of FaceDetector
    face_detector = FaceDetector()

    # Create an instance of RPPG
    rppg = RPPG()

    # Create an instance of RPPGPlot
    rppg_plot = RPPGPlot()

    while True:
        # Read the current frame from the video capture
        ret, frame = face_detector.video_capture.read()

        # Perform face detection
        face = face_detector.detect_face(frame)

        if face is not None:
            # Extract the region of interest (ROI) containing the face
            face_roi = face_detector.extract_face_roi(frame, face)

            # Pass the face ROI to RPPG for processing
            rppg.process_frame(face_roi)

            # Draw a green square around the detected face
            face_detector.draw_face_rectangle(frame, face)

        # Display the frame in the first window
        face_detector.display_frame(frame)

        # Update the RPPG plot in the second window
        rppg_plot.update_plot(rppg.normalized_rppg)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close the windows
    face_detector.release()
    rppg_plot.close_plot()

if __name__ == '__main__':
    main()
