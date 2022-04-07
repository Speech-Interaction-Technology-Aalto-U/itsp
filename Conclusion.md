# Conclusion

Speech is our most important signal. Everything important in life is
communicated with speech. Any time we want to interact with someone, the
preferred method is speech. That is how humans are built (with the
exception of some disabilities and such).

Consequently, any technology that we can develop to support speech
communication or which takes advantage of our speaking abilities, can be
very useful. For example, improving telecommunication technologies is
important because that helps us connect with remote persons. Similarly,
developing improved user interfaces to better support voice input,
allows more intuitive interaction with devices. That is convenient for
the average people, but can be life changing for children, the elderly
and people with disabilities who have limited ability to interact with
visual and tactile interfaces.

Speech signals are acoustic pressure waves, which vary a lot over time,
yet it would be convenient to analyse the spectrum of signals, because
we have an intuitive interpretation for spectral characteristics. For
example, everyone knows the difference between high and low pitch, as
well as between a dark and bright sound. Such features can be easily
visualized with a spectrogram, where the spectral content (i.e.
frequency content) is analyzed in short segments and illustrated with a
heat-map.

For automated analysis of speech, the spectrogram is then also a good
starting point. However, to reduce the dimensionality, we can apply
perceptual compression to the mel-frequency scale, and we can apply
decorrelation with the discrete cosine transform (DCT) to make the data
better digestible for machine learning. This is known as the
*mel-frequency cepstral coefficient (MFCC)* representation and it is the
most commonly used feature in speech and audio recognition and
classification tasks.

Application of machine learning on speech data is then straightforward.
For example, a frequently appearing task is *voice activity detection*
(VAD), where the objective is to determine whether an acoustic signal
contains speech or not. We can then train a simple machine learning
algorithm with MFCCs as input and the desired label (speech or
non-speech) as the output. When a VAD is implemented in an efficient
way, it can be very useful in reducing overall resource-consumption of a
system. For example, we can let the VAD run all the time and when it
detects speech, only then would we trigger a computationally expensive
speech recognition engine.

Overall, speech processing is an exciting field of engineering, where
signal processing and machine learning methods to solve practical,
important and meaningful problems.

