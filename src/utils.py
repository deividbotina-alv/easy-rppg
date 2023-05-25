import time
import numpy as np
import matplotlib.pyplot as plt

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


def create_sinusoidal_signal(duration:int, sampling_rate:int, frequency:float,
                              amplitude:int, noise_level:float)->np.array:
    """
    Create a sinusoidal signal of a specified duration.
    Args:
        duration (float): Duration of the signal in seconds.
        sampling_rate (int): Number of samples per second.
        frequency (float): Frequency of the sinusoidal signal in Hz.
        amplitude (float): Amplitude of the sinusoidal signal.
        noise_level (float): Level of additive white Gaussian noise.

    Returns:
        numpy.ndarray: Sinusoidal signal with specified characteristics.

    """

    # Calculate the total number of samples
    num_samples = int(duration * sampling_rate)
    # Generate time values for the signal
    t = np.arange(num_samples) / sampling_rate
    # Generate the clean sinusoidal signal
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    # Add additive white Gaussian noise to the signal
    noise = np.random.normal(0, noise_level, num_samples)
    signal_with_noise = signal + noise

    return signal_with_noise

def plot_signal(signal:np.array, sampling_rate):
    """
    Plot a signal with time on the x-axis in seconds.

    Args:
        signal (numpy.ndarray): Signal to be plotted.
        sampling_rate (int): Number of samples per second.

    """
    # Calculate the time values for the x-axis
    duration = len(signal) / sampling_rate
    t = np.linspace(0, duration, len(signal))
    # Plot the signal
    plt.figure()
    plt.plot(t, signal)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.title('Signal Plot')
    plt.grid(True)
    plt.show()

def bpm2hz(bpm:float):
    """
    helper function to change between beats per minute
    to hertz
    """
    return bpm/60

def create_sinusoidal_array(array_size:tuple, duration:int, sampling_rate:int, frequency:float,
                              amplitude:int, noise_level:float)->np.array:
    """
    Create a sinusoidal signal of a specified duration and then create an array for
    each individual value. This is useful to simulate a serie of human faces with
    a specific rppg value
    Args:
        duration (float): Duration of the signal in seconds.
        sampling_rate (int): Number of samples per second.
        frequency (float): Frequency of the sinusoidal signal in Hz.
        amplitude (float): Amplitude of the sinusoidal signal.
        noise_level (float): Level of additive white Gaussian noise.

    Returns:
        numpy.ndarray: Sinusoidal array with specified characteristics.
    """
    rppg = create_sinusoidal_signal(duration, sampling_rate, frequency, amplitude, noise_level)
    # Reshape the original array to have a singleton dimension
    reshaped_rppg = rppg[:, np.newaxis, np.newaxis, np.newaxis]

    # Tile the reshaped array to match the desired dimension
    faces_rppg = np.tile(reshaped_rppg, (1,) + array_size + (3,))

    return faces_rppg