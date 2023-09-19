import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from exception import CustomException
from logger import logging

class RPPG:
    def __init__(self):
        pass

    def __call__(self, traces:list):
        return self.computeRPPG(traces)

    def computeRPPG(self, traces:list):
        raise NotImplementedError("Subclasses must implement the computeRPPG method.")

class Green(RPPG):
    def __init__(self):
        super().__init__()

    def computeRPPG(self, traces:list):
        traces = np.array(traces) # traces has channels B,G,R in columns 0,1, and 2 respectively.
        # Take R,G,B traces 
        G = traces[:,1] ; # plt.figure(); plt.plot(G)
        # Compute RPPG method
        rppg = G

        # Manage NaN values
        if np.isnan(rppg).any():   
            logging.info(f"NaN values found in the signal, using interpolation to fill them")
            # Replace NaN values with interpolation if needed        
            nan_indices = np.isnan(rppg) # Find the indices of NaN values
            non_nan_indices = np.arange(len(rppg))[~nan_indices] # array for non-NaN values
            rppg[nan_indices] = np.interp(np.arange(len(rppg))[nan_indices], non_nan_indices, rppg[~nan_indices])
            
        return rppg

class GR(RPPG):
    def __init__(self):
        super().__init__()

    def computeRPPG(self, traces:list):
        traces = np.array(traces) # traces has channels B,G,R in columns 0,1, and 2 respectively.
        # Take R,G,B traces 
        G = traces[:,1] #; plt.figure(); plt.plot(G)
        R = traces[:,2] #; plt.figure(); plt.plot(R)

        rppg = G-R #; plt.figure(); plt.plot(rppg)

        # Manage NaN values
        if np.isnan(rppg).any():   
            logging.info(f"NaN values found in the signal, using interpolation to fill them")
            # Replace NaN values with interpolation if needed        
            nan_indices = np.isnan(rppg) # Find the indices of NaN values
            non_nan_indices = np.arange(len(rppg))[~nan_indices] # array for non-NaN values
            rppg[nan_indices] = np.interp(np.arange(len(rppg))[nan_indices], non_nan_indices, rppg[~nan_indices])
            
        return rppg

# if __name__ == '__main__':
#     print('================================================================')
#     print('                     rppgs.py demo                            ')
#     print('================================================================')  

#     from utils import create_sinusoidal_array, plot_signal, bpm2hz

#     is_plot = True

#     # Simulate faces with rppg
#     array_size = (128,128)
#     duration = 15  # seconds
#     sampling_rate = 30  # samples per second
#     frequency = bpm2hz(80)  # Hz
#     amplitude = 1.0
#     noise_level = 0.1
#     faces_rppg = create_sinusoidal_array(array_size, duration, sampling_rate, frequency, amplitude, noise_level)

#     # Create class to measure RPPG
#     filter = BandPass(lowcut=0.7, highcut=3.5, fs=sampling_rate, order=5)# Define filter
#     rppg_computer = Green(filter=filter)
#     rppg = rppg_computer(faces_rppg)
#     print('ready')