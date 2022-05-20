import numpy as np


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