from scipy.fftpack import fft, fftfreq, ifft
from constants import *
import numpy as np

def perform_fft(video,fps, min_frequency=MIN_FREQUENCY, max_frequency=MAX_FREQUENCY, amplification_factor=AMPLIFICATION_FACTOR):
    """
    Perform a Fast Fourier Transform (FFT) on the given video.

    Args:
        video (numpy array): The input video.
        fps (float): The frames per second of the video.
        min_frequency (float, optional): The minimum frequency of interest. Defaults to MIN_FREQUENCY.
        max_frequency (float, optional): The maximum frequency of interest. Defaults to MAX_FREQUENCY.
        amplification_factor (float, optional): The factor by which to amplify the filtered video. Defaults to AMPLIFICATION_FACTOR.

    Returns:
        A tuple of (filtered_video, fft_video, freq), where filtered_video is the filtered video in the time domain,
        fft_video is the FFT of the video, and freq is the frequency array.
    """
    
    fft_video = fft(video,axis=0)
    # Calculate the frequency array from the length of the video and the
    # frames per second.
    freq = fftfreq(video.shape[0], d=1.0/fps)

    # Find the indices of the lower and upper bounds for the frequency
    # range of interest.
    lower_bound = np.abs(freq - min_frequency).argmin()
    upper_bound = np.abs(freq - max_frequency).argmin()

    # Set all the frequencies outside the range of interest to zero.
    fft_video[:lower_bound] = 0
    fft_video[upper_bound:-upper_bound] = 0
    fft_video[-lower_bound:] = 0

    # Perform the inverse FFT to get the filtered video in the time domain.
    ifft_video = ifft(fft_video,axis=0)
    ifft_out = np.abs(ifft_video)
    ifft_out *= amplification_factor
    
    return ifft_out, fft_video, freq


def get_heart_rate(fft_video, freqency_bins, min_frequency=MIN_FREQUENCY, max_frequency=MAX_FREQUENCY):
    """
    Calculate the heart rate of the given video.

    Args:
        fft_video (numpy array): The FFT of the video.
        freqency_bins (numpy array): The frequency bins of the video.
        min_frequency (float, optional): The minimum frequency of interest. Defaults to MIN_FREQUENCY.
        max_frequency (float, optional): The maximum frequency of interest. Defaults to MAX_FREQUENCY.

    Returns:
        The heart rate of the video.
    """
    
    # Find the indices of the lower and upper bounds for the frequency
    # range of interest.
    lower_bound = np.abs(freqency_bins - min_frequency).argmin()
    upper_bound = np.abs(freqency_bins - max_frequency).argmin()
    
