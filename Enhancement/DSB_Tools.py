#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
rng = np.random.default_rng()

class SensorArray:
    """
    Class to store Uniform Linear Array geometry.
    
    L : float
        Array length [m]
    
    M : int
        Number of sensors (must be odd)
    
    d : float
        Inter sensor spacing [m]
        
    XY : (2,M) array_like
        Numpy array with sensor coordinates in 2D (x,y) space
        
    m : (M,) array_like
        Numpy array of integer sensor indices, from -(M-1)/2 to +(M-1)/2
    """
    
    def __init__(self, L, M):
        self.M = M
        self.L = L
        
        self.XY, self.d, self.m = self.create_unif_lin_array(L, M)

        
    def create_unif_lin_array(self, L, M):
        """
        Creates a uniform linear array with length 'L' and 'M' elements
        distributed over the 'x' axis. By convenience, 'M' must be odd.
        
        Parameters
        ----------
        L : float
            Array length [m]
        
        M : int
            Number of sensors (must be odd)
        
        Returns
        -------
        XY_array : (2, M) array_like
            Numpy array with (x,y) coordinates of array elements
        
        d : float
            Array inter-element spacing [m]
        
        m_indices : 
            Array of indices from -(M-1)/2 to +(M-1)/2, with index 0 being at
            the center.
        
        Notes
        -----
        By convenience, the number of elements 'M' in the array must always be
        odd.
        """
    
        M_even_error = "Number of sensors must be odd"
        assert M%2, M_even_error
    
        # inter sensor spacing
        d = L/(M-1)
    
        print("Array inter sensor spacing is {} m".format(d))
    
        # array sensor indices
        m_indices = np.linspace(-(M//2), M//2, M, dtype=int)
    
        # array elements spatial coordinates
        XY_array = np.zeros((2, M))
        XY_array[0, :] = np.linspace(-L/2, L/2, M)
    
        return XY_array, d, m_indices
        

def delay_signal(x, t0, fs):
    """
    Delay a time-domain signal 'x', sampled at 'fs' Hz, by 't0' seconds.

    Parameters
    ----------
    x : (N_dft,) array_like
        Numpy vector of length 'N_dft' containing signal of interest

    t0 : float
        Time by which to delay signal 'x', in seconds
        
    fs : int
        Sampling frequency, in Hz

    Returns
    -------
    x_delayed : (N,)
        Time-delayed copy of input signal 'x'

    """
    
    X_f = np.fft.rfft(x)
    
    N_dft = x.shape[0]
    df = fs/N_dft
    f = np.linspace(0, fs-df, N_dft)[:N_dft//2+1]
    
    X_f_delayed = X_f*np.exp(-1j*2*np.pi*f*t0)
    
    return np.fft.irfft(X_f_delayed)


def create_narrowband_pulse(A, T, f0, fs):
    """
    Creates a narrowband pulse signal with amplitude 'A', duration 'T' seconds,
    center frequency 'f0' Hz, and sampling frequency 'fs' Hz.
    
    Parameters
    ----------
    A : float
        Signal peak amplitude
    
    T : float
        Signal duration, in seconds
    
    f0 : float
        Signal center frequency, in Hz
    
    fs : int
        Sampling frequency, in Hz
    
    Returns
    -------
    p_pulse : (N_pulse,) array_like
        Numpy vector containing narrowband pulse signal.
    
    Notes
    -----
    The signal is a sine wave of amplitude 'A', frequency 'f0', and random
    initial phase, modulated by a Hann window of duration 'T'.
    """
    
    # pulse duration [samples]
    N_pulse = int(T*fs)
    dt = 1./fs

    t_pulse = np.linspace(0, T-dt, N_pulse)
    p_pulse = A*np.sin(2*np.pi*f0*t_pulse
                       + rng.uniform(0, 2*np.pi, 1)[0])*np.hanning(N_pulse)
    
    return p_pulse


def create_array_signals(SensorArrayObj, p_source, t_initial, T, theta0_deg,
                         fs, c0=1500, SNR_dB=None):
    """
    Create a Numpy array of time-domain signals simulating a recording with a
    Uniform Linear Array

    Parameters
    ----------
    SensorArrayObj : instance of SensorArray class
        Instance containing array geometry information
    
    p_source : (N,) array_like
        Numpy vector containing 'clean' (i.e. no noise) source signal in time.
    
    t_initial : float
        Time at which source signal reaches the center array sensor.
    
    T : float
        Total sensor signal duration, in seconds.
    
    theta0_deg : float
        Direction of arrival of source signal, relative to array axis, in
        degrees.
    
    fs : int
        Sampling frequency, in Hz.
    
    c0 : float, optional
        Speed of sound, in meters per second. The default is 343 (m/s).
    
    SNR_dB : float, optional
        Signal-to-noise ratio, in decibels, as observed at sensor elements. The
        default is None (no noise at array sensors).

    Returns
    -------
    p_array : (M, T*fs) array_like
        Numpy array containing 'M' channels of array signals over time.

    Notes
    -----
    This model assumes the source signal arrives at the array as a plane wave.
    
    The 'SNR_dB' parameter controls how much uncorrelated white noise is added
    to the sensors. If 'SNR_dB=None', no white noise is added to the array
    signals.
    
    The SNR is calculated from the ratio between the total variance in
    'p_source' to the total variance in the additive white noise signal, so
    it denotes a 'broadband' notion of SNR. This interpretation of SNR might
    not be valid to all contexts.
    """
    
    # instantiate a random number generator
    rng = np.random.default_rng()
    
    # direction of arrival of signals (plane wave propagation)
    theta0 = theta0_deg*np.pi/180
    
    # vector of times-of-arrival for each sensor
    times_of_arrival = -SensorArrayObj.m*SensorArrayObj.d*np.cos(theta0)/c0
    
    N_initial= int(t_initial*fs)
    N_final = N_initial + p_source.shape[0]
    
    # No. of samples in array data (total duration)
    N = int(T*fs)
    
    # create array of sensor signals    
    if SNR_dB is None:
        # if SNR_dB is not given, initialize signals as array of zeros (no
        # noise)
        p_array = np.zeros((SensorArrayObj.M, N))
    
    else:
        # if SNR_dB is given, add random noise to array signals at desired SNR
        signal_var = np.var(p_source)
        noise_var = signal_var/(10**(SNR_dB/10))
        p_array = rng.normal(0., np.sqrt(noise_var), (SensorArrayObj.M, N))
    
    # for each sensor in array...
    for m in range(SensorArrayObj.M):
        # ...adds signal at time 't_initial'...
        p_array[m, N_initial:N_final] += p_source
        
        # ...and time-shifts signal for given time-of-arrival
        p_array[m, :] = delay_signal(p_array[m, :], times_of_arrival[m], fs)
    
    return p_array



def delayandsum_beamformer(SensorArrayObj, p_array, theta, weights, fs,
                           c0=1500):
    """
    Calculates simplified delay-and-sum beamformer for a given array geometry 
    and sensor signals, over a set of pre-determined directions.
    
    Parameters
    ----------
    SensorArrayObj : instance of SensorArray class
        Instance containing array geometry information
        
    p_array : (M, T*fs) array_like
        Numpy array containing 'M' channels of array signals over time.
    
    theta : (N_theta,) array_like
        Numpy vector containing set of desired steering directions, in radians.
    
    weights : (M,) array_like
        Numpy vector containing array amplitude weighting coefficients.
    
    fs : int
        Sampling frequency, in Hz.
    
    c0 : float, optional
        Speed of sound, in meters per second. The default is 343 (m/s).
    
    Returns
    -------
    y_beamformer : (N_theta, T*fs,) array_like
        Numpy array containing the time-domain beamformer output signal for
        each steering direction.
    
    """
    
    N_theta = theta.shape[0]
    
    M, N_time = p_array.shape
    
    # initialize array of beamformer data (angle, time)
    y_beamformer = np.zeros((N_theta, N_time))

    # for each direction...
    for theta_i in range(N_theta):
        
        # calculate candidate time delays (TDoA) referring to all microphone using its steering direction (DoA)
        #The time delays due to propagation are given by d *m *cos (theta) /c, where d is the distance of the n-th microphone to the center         of the array and theta is the angle of arrival relative to the array axis.
        
        time_delays = -SensorArrayObj.m*SensorArrayObj.d*np.cos(theta[theta_i])/c0
    
        # and for each sensor...
        for m in range(M):
            # delay and sum signals
            y_beamformer[theta_i, :] += weights[m]*delay_signal(p_array[m, :], -time_delays[m], fs)
    
    # compensate for Nweights / No. of sensors in array
    y_beamformer *= 1./np.sum(weights**2)
    
    return y_beamformer

