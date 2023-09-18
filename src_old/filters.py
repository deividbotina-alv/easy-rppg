import numpy as np
from scipy.signal import butter, lfilter

#%% Main classes and functions

class Filter:
    def __call__(self, x):
        return self.forward(x)

    def forward(self, x):
        raise NotImplementedError("Subclasses must implement the forward method.")
    
class BandPass(Filter):
    def __init__(self, lowcut:float=0.7, highcut:float=3.5, fs:int=10, order:int=8):
        """
        lowcut(float): Lower cut for the bandpass filter
        highcut(float): Upper cut for the bandpass filter
        fs(int): frequency sampling in hertz/fps. Default = 10
        """
        super().__init__()
        self.lowcut = lowcut
        self.highcut = highcut
        self.fs = fs
        self.order = order  

    def forward(self, x):
        return self.butter_bandpass_filter(data=x)

    def butter_bandpass(self, lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a

    def butter_bandpass_filter(self, data):
        b, a = self.butter_bandpass(self.lowcut, self.highcut, self.fs, self.order)
        y = lfilter(b, a, data)
        return y    

if __name__ == '__main__':
    print('================================================================')
    print('                     filters.py demo                            ')
    print('================================================================')  

    is_plot = True

    from utils import create_sinusoidal_signal, plot_signal, bpm2hz
    import matplotlib.pyplot as plt

    if is_plot: plt.switch_backend('TkAgg')

    # Create the sinusoidal signal
    duration = 60  # seconds
    sampling_rate = 30  # samples per second
    frequency = bpm2hz(100)  # Hz
    amplitude = 1.0
    noise_level = 0.1
    rppg = create_sinusoidal_signal(duration, sampling_rate, frequency, amplitude, noise_level)
    if is_plot: plot_signal(rppg, sampling_rate)

    # Create filter
    BP = BandPass(lowcut=0.7, highcut=3.5, fs=sampling_rate, order=5)
    rppg_filtered = BP(rppg)
    if is_plot: plot_signal(rppg_filtered, sampling_rate)