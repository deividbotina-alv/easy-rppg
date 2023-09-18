"""
Created on Fri May 26 2023
Last modification: 26/05/2023
@authors: HenRick, Deivid

Description: This file works for real-time RPPG signal processing and visualization
using OpenCV, detrending, and matplotlib in Python..
"""

import cv2
import numpy as np
from scipy.signal import detrend
import matplotlib.pyplot as plt

class RPPG:
    def __init__(self):
        self.time_buffer = []
        self.rppg_buffer = []
        self.normalized_rppg = []

    def process_frame(self, frame):
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Resize the grayscale frame to the desired size
        roi = cv2.resize(gray, (100, 100))

        # Compute the mean value of the ROI
        roi_mean = np.mean(roi)

        # Append the current time and ROI mean to the buffers
        self.time_buffer.append(cv2.getTickCount())
        self.rppg_buffer.append(roi_mean)

        # Detrend the RPPG signal
        detrended_rppg = detrend(np.array(self.rppg_buffer))

        # Normalize the RPPG signal between 0 and 255
        max_value = np.max(detrended_rppg)
        min_value = np.min(detrended_rppg)
        self.normalized_rppg = ((detrended_rppg - min_value) / (max_value - min_value) * 255).astype(np.uint8)

class RPPGPlot:
    def __init__(self):
        # Create a plot figure and axis
        self.fig, self.ax = plt.subplots()
        self.plot_line, = self.ax.plot([], [])
        plt.title('Normalized RPPG Signal')
        plt.xlabel('Time')
        plt.ylabel('Signal')
        plt.ylim(0, 255)

        # Initialize the animation
        self.animation = None

        # Start the animation
        self.start_animation()

    def update_plot(self, rppg_signal):
        # Update the plot with the new RPPG signal
        self.plot_line.set_data(range(len(rppg_signal)), rppg_signal)

        # Adjust the plot limits
        self.ax.set_xlim(0, len(rppg_signal))

        # Redraw the plot
        self.fig.canvas.draw()

    def start_animation(self):
        # Start the animation
        self.animation = plt.show(block=False)

    def close_plot(self):
        # Close the plot
        plt.close(self.fig)
