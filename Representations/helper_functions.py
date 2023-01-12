# Initialization
import matplotlib.pyplot as plt
from scipy.io import wavfile
import scipy
import scipy.fft
import numpy as np


def stft(data,fs,window_length_ms=30,window_step_ms=20,windowing_function=None):
    window_length = int(window_length_ms*fs/1000)
    window_step = int(window_step_ms*fs/1000)
    if windowing_function == None:
        windowing_function = np.sin(np.pi*np.arange(0.5,window_length,1)/window_length)**2
    
    total_length = len(data)
    window_count = int( (total_length-window_length)/window_step) + 1
    
    spectrum_length = int((window_length)/2)+1
    spectrogram = np.zeros((window_count,spectrum_length))

    for k in range(window_count):
        starting_position = k*window_step

        data_vector = data[starting_position:(starting_position+window_length),]
        window_spectrum = np.abs(scipy.fft.rfft(data_vector*windowing_function,n=window_length))

        spectrogram[k,:] = window_spectrum
        
    return spectrogram

def istft(data,fs,window_length_ms=30,window_step_ms=20):
    window_length = int(window_length_ms*fs/1000)
    window_step = int(window_step_ms*fs/1000)
    windowing_function = np.sin(np.pi*np.arange(0.5,window_length,1)/window_length)**2
    
    total_length = len(data)
    window_count = int( (total_length-window_length)/window_step) + 1
    
    spectrum_length = int((window_length)/2)+1
    spectrogram = np.zeros((window_count,spectrum_length))

    for k in range(window_count):
        starting_position = k*window_step

        data_vector = data[starting_position:(starting_position+window_length),]
        window_spectrum = np.abs(scipy.fft.rfft(data_vector*windowing_function,n=window_length))

        spectrogram[k,:] = window_spectrum
        
    return spectrogram



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
    
    


def freq2mel(f): return 2595*np.log10(1 + (f/700))
def mel2freq(m): return 700*(10**(m/2595) - 1)


def melfilterbank(speclen, maxfreq, melbands = 20):
    maxmel = freq2mel(maxfreq)
    mel_idx = np.array(np.arange(.5,melbands,1)/melbands)*maxmel
    freq_idx = mel2freq(mel_idx)

    melfilterbank = np.zeros((speclen,melbands))
    freqvec = np.arange(0,speclen,1)*maxfreq/speclen
    for k in range(melbands-2):    
        if k>0:
            upslope = (freqvec-freq_idx[k])/(freq_idx[k+1]-freq_idx[k])
        else:
            upslope = 1 + 0*freqvec
        if k<melbands-3:
            downslope = 1 - (freqvec-freq_idx[k+1])/(freq_idx[k+2]-freq_idx[k+1])
        else:
            downslope = 1 + 0*freqvec
        triangle = np.max([0*freqvec,np.min([upslope,downslope],axis=0)],axis=0)
        melfilterbank[:,k] = triangle

    melreconstruct = np.matmul(np.diag(np.sum(melfilterbank**2+1e-12,axis=0)**-1),np.transpose(melfilterbank))
                  
    return melfilterbank, melreconstruct


def linearfilterbank(speclen, maxfreq_Hz, bandwidth_Hz=500):
    bandstep_Hz = bandwidth_Hz/2
    bands = int(maxfreq_Hz/bandstep_Hz)+1 
    filterbank = np.zeros((speclen,bands))
    freqvec = np.arange(0,speclen,1)*maxfreq_Hz/speclen
    freq_idx = np.arange(-bandstep_Hz/2,maxfreq_Hz+bandstep_Hz/2,bandstep_Hz)
    for k in range(bands-1):
        if k>0:
            upslope = (freqvec-freq_idx[k])/(freq_idx[k+1]-freq_idx[k])
        else:
            upslope = 1 + 0*freqvec
        if k<bands-2:
            downslope = 1 - (freqvec-freq_idx[k+1])/(freq_idx[k+2]-freq_idx[k+1])
        else:
            downslope = 1 + 0*freqvec
        triangle = np.max([0*freqvec,np.min([upslope,downslope],axis=0)],axis=0)
        filterbank[:,k] = triangle
                          
    reconstruct = np.matmul(np.diag(np.sum(filterbank**2+1e-12,axis=0)**-1),np.transpose(filterbank))
                  
    return filterbank, reconstruct
    