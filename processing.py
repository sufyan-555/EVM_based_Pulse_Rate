from scipy.fftpack import fft, fftfreq, ifft
from scipy import signal
from constants import *
import numpy as np

def perform_fft(video, fps, freq_min=MIN_FREQUENCY, freq_max=MAX_FREQUENCY, amplification_factor=AMPLIFICATION_FACTOR):
    fft_video = fft(video, axis=0)
    frequencies = fftfreq(video.shape[0], d=1.0 / fps)
    bound_low = (np.abs(frequencies - freq_min)).argmin()
    bound_high = (np.abs(frequencies - freq_max)).argmin()
    fft_video[:bound_low] = 0
    fft_video[bound_high:-bound_high] = 0
    fft_video[-bound_low:] = 0
    # iff_video = ifft(fft_video, axis=0)
    # result = np.abs(iff_video)
    # result *= amplification_factor

    # return result,fft_video, frequencies
    return fft_video, frequencies


def get_heart_rate(fft_video, freqency_bins, min_frequency=MIN_FREQUENCY, max_frequency=MAX_FREQUENCY):
    fft_maximums = []

    for i in range(fft_video.shape[0]):
        if min_frequency <= freqency_bins[i] <= max_frequency:
            fftMap = abs(fft_video[i])
            fft_maximums.append(fftMap.max())
        else:
            fft_maximums.append(0)

    peaks, properties = signal.find_peaks(fft_maximums)
    max_peak = -1
    max_freq = 0

    # Find frequency with max amplitude in peaks
    for peak in peaks:
        if fft_maximums[peak] > max_freq:
            max_freq = fft_maximums[peak]
            max_peak = peak

    return (freqency_bins[max_peak] * 60)    
