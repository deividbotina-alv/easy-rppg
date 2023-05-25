import numpy as np
from filters import Filter

class RPPG:
    def __init__(self, filter:Filter=None):
        if not isinstance(filter, Filter):
            raise TypeError("filter must be a Filter object.")
        self.filter = filter

    def __call__(self, x):
        return self.computeRPPG(x)

    def computeRPPG(self, x:str):
        raise NotImplementedError("Subclasses must implement the computeRPPG method.")

class Green(RPPG):
    def __init__(self, filter:Filter=None):
        super().__init__(filter=filter)

    def computeRPPG(self, x:str):
        raise NotImplementedError("Subclasses must implement the computeRPPG method.")

if __name__ == '__main__':
    print('================================================================')
    print('                     rppgs.py demo                            ')
    print('================================================================')  

    from filters import BandPass
    from utils import create_sinusoidal_array, plot_signal, bpm2hz

    is_plot = True

    # Simulate faces with rppg
    array_size = (128,128)
    duration = 15  # seconds
    sampling_rate = 30  # samples per second
    frequency = bpm2hz(80)  # Hz
    amplitude = 1.0
    noise_level = 0.1
    faces_rppg = create_sinusoidal_array(array_size, duration, sampling_rate, frequency, amplitude, noise_level)

    # Create class to measure RPPG
    filter = BandPass(lowcut=0.7, highcut=3.5, fs=sampling_rate, order=5)# Define filter
    rppg_computer = Green(filter=filter)
    rppg = rppg_computer(faces_rppg)
    print('ready')