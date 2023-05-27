import time
import cv2
from utils import PreserveFPS, detect_face, draw_face_rectangle
from face_detector import HaarCascade

def stream_rppg(camera_index: int, width: int, height: int, fps: int, face_detector: str, verbose: int):
    """
    Main function to start streaming and compute rppg
    camera_index(int): Index of camera to be used
    fps(int): FPS for the streaming
    """
    cap = cv2.VideoCapture(camera_index)  # Create a videoCapture object
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # Set width
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # Set height

    # Load the pre-trained face detection model
    if face_detector in ['haarcascade']:
        face_detector = HaarCascade()

    if verbose > 0:
        print(f"[INFO]: Starting streaming: [{int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))},"
              f"{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}] {int(cap.get(cv2.CAP_PROP_FPS))} fps")

    fps_preserver = PreserveFPS(fps)  # It will guarantee fps streaming

    start_time = cv2.getTickCount()  # Start capturing frames from the camera
    while cap.isOpened():
        with fps_preserver:
            # Manage current FPS measurement
            elapsed_ticks = cv2.getTickCount() - start_time  # Calculate FPS
            elapsed_time = elapsed_ticks / cv2.getTickFrequency()
            fps = 1 / elapsed_time if elapsed_time > 0 else 0
            start_time = cv2.getTickCount()  # Reset the start time

            ret, frame = cap.read()
            if ret:
                # Manage face detection
                face = detect_face(face_detector, frame) # Face detection
                if face is not None:
                    draw_face_rectangle(frame, face) # Draw green rectangle
                cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2) # Draw fps
                cv2.imshow("Video live", frame)
            else:
                print("[INFO] No camera device found")

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print('================================================================')
    print('                         RPPG streaming                         ')
    print('================================================================')
    print(time.strftime("%Y-%m-%d %H:%M:%S"))

    camera_index = 0
    width = 640
    height = 480
    fps = 25
    verbose = 2
    face_detector = 'haarcascade'

    stream_rppg(camera_index=camera_index,
                fps=fps,
                width=width,
                height=height,
                face_detector=face_detector,
                verbose=verbose)
