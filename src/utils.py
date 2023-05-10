import time

class preserve_fps:
    """
    Helper class to mantain the desired fps
    """
    def __init__(self, desired_fps):
        self.desired_fps = desired_fps
        self.frame_duration = 1 / desired_fps
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self.start_time
        if elapsed_time < self.frame_duration:
            time.sleep(self.frame_duration - elapsed_time) 
