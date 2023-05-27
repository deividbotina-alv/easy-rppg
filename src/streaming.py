import time
import cv2
from utils import preserve_fps

def stream_rppg(camera_index:int, width:int, height:int, fps:int, VERBOSE:int):
    """
    Main function to start streaming and compute rppg
    camera_index(int): Index of camera to be used
    fps(int): FPS for the streaming
    """
    ###
    # Create a videoCapture object
    cap = cv2.VideoCapture(camera_index) # Open camera port
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width) # Set width
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)# Set height
    # cap.set(cv2.CAP_PROP_FPS, fps) # Set camera fps

    if VERBOSE>0:
        print(f"[INFO]: Starting streaming: [{int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}",
              f"{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}]", f"{int(cap.get(cv2.CAP_PROP_FPS))} fps")

    fps_preserver = preserve_fps(fps) # It will guarantee fps streaming

    # Start capturing frames from the camera
    start_time = cv2.getTickCount()  # Add this line
    while cap.isOpened():
        with fps_preserver:
            # Calculate FPS
            elapsed_ticks = cv2.getTickCount() - start_time
            elapsed_time = elapsed_ticks / cv2.getTickFrequency()
            fps = 1 / elapsed_time if elapsed_time > 0 else 0
            start_time = cv2.getTickCount()  # Reset the start time

            ret, frame = cap.read()
            if ret == True:
                # Draw FPS on the video frame
                cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
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
    VERBOSE = 2

    # RUN MAIN FUNCTION
    stream_rppg(camera_index = camera_index,
                fps = fps,
                width = width,
                height = height,
                VERBOSE = VERBOSE
                ) 
