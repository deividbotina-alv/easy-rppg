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
    cap.set(cv2.CAP_PROP_FPS, fps) # Set camera fps

    if VERBOSE>0:
        print(f"[INFO]: Starting streaming: [{int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}",
              f"{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}]", f"{int(cap.get(cv2.CAP_PROP_FPS))} fps")

    fps_preserver = preserve_fps(fps) # It will guarantee fps streaming

    # Start capturing frames from the camera
    while cap.isOpened():
        with fps_preserver:
            #start_time = time.time() # To manage stream at fps

            ret, frame = cap.read()
            if ret == True:
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

    camera_index = 4
    width = 1280
    height = 720
    fps = 10 
    VERBOSE = 2

    # RUN MAIN FUNCTION
    stream_rppg(camera_index = camera_index,
                fps = fps,
                width = width,
                height = height,
                VERBOSE = VERBOSE
                ) 
