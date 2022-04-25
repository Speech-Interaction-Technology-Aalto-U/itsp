# Initialization
import matplotlib.pyplot as plt
from scipy.io import wavfile
import scipy
import scipy.fft
import numpy as np


def stft(data,fs,window_length_ms=30,window_step_ms=20,windowing_function=None):
    window_length = int(window_length_ms*fs/2000)*2
    window_step = int(window_step_ms*fs/1000)
    #if windowing_function is None:
    #    windowing_function = np.sin(np.pi*np.arange(0.5,window_length,1)/window_length)**2
    
    total_length = len(data)
    window_count = int( (total_length-window_length)/window_step) + 1
    
    spectrum_length = int((window_length)/2)+1
    spectrogram = np.zeros((window_count,spectrum_length),dtype=np.cdouble)

    for k in range(window_count):
        starting_position = k*window_step

        data_vector = data[starting_position:(starting_position+window_length),]
        window_spectrum = scipy.fft.rfft(data_vector*windowing_function,n=window_length)

        spectrogram[k,:] = window_spectrum
        
    return spectrogram

def istft(spectrogram,fs,window_length_ms=30,window_step_ms=20,windowing_function=None):
    window_length = int(window_length_ms*fs/2000)*2
    window_step = int(window_step_ms*fs/1000)
    #if windowing_function is None:
    #    windowing_function = np.ones(window_length)
    window_count = spectrogram.shape[0]
    
    total_length = (window_count-1)*window_step + window_length
    data = np.zeros(total_length)
    
    for k in range(window_count):
        starting_position = k*window_step
        ix = np.arange(starting_position,starting_position+window_length)

        thiswin = scipy.fft.irfft(spectrogram[k,:],n=window_length)
        data[ix] = data[ix] + thiswin*windowing_function
        
    return data


def halfsinewindow(window_length):
    return np.sin(np.pi*np.arange(0.5,window_length,1)/window_length)

def zcr(data,fs,window_length_ms=30,window_step_ms=20):
    window_length = int(window_length_ms*fs/1000)
    window_step = int(window_step_ms*fs/1000)
    windowing_function = np.sin(np.pi*np.arange(0.5,window_length,1)/window_length)**2
    
    total_length = len(data)
    window_count = int( (total_length-window_length)/window_step) + 1

    y = np.zeros(window_count)

    for k in range(window_count):
        starting_position = k*window_step

        data_vector = data[starting_position:(starting_position+window_length),]
        y[k] = np.sum(np.abs(np.diff(np.sign(data_vector))))
        
    return y
    