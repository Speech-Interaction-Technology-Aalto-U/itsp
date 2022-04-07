# Fundamental frequency estimation

<div class="contentLayout2">

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

The [fundamental frequency (F0)](Fundamental_frequency_F0_) is central
in describing speech signals whereby we need methods for estimating the
F0 from speech signals. In speech analysis applications, it can be
informative to study the absolute value of the fundamental frequency as
such, but more commonly, extraction of the F0 is usually a
pre-processing step. For example, in [recognition
tasks](Recognition_tasks_in_speech_processing), F0 is often used as a
feature for machine learning methods. A voice activity detector could,
for instance, set a lower and higher threshold on the F0, such that
sounds with an F0 outside the valid range would be classified as
non-speech.

The fundamental frequency is visible in multiple different domains:

-   In an acoustic time-signal, the F0 is visible as a repetition after
    every *T* samples.
-   In the [autocovariance or
    -correlation](Autocorrelation_and_autocovariance), the F0 is visible
    as a peak at lag *T* as well as its integer multiples *kT*.
-   In the magnitude, power or log-magnitude
    [spectrum](Spectrogram_and_the_STFT), the F0 is visible as a peak at
    the frequency F0=*F<sub>s</sub>/T*, as well as its integer
    multiples, where *F<sub>s</sub>* is the sampling frequency.
-   In the [cepstrum](Cepstrum_and_MFCC), the F0 is visible as a peak at
    quefrency *T* as well as its integer multiples *kT*.

Consequently, we can use any of these domains to estimate the
fundamental frequency F0. A typical approach applicable in all domains
except the time-domain, is peak-picking. The fundamental frequency
corresponds to a peak in each domain, such that we can determine the F0
by finding the highest peak. For better robustness to spurious peaks and
for computational efficiency, we naturally limit our search to the range
of valid F0's, such as  \\( 80\\leq F_0\\leq 450. \\)  

The harmonic structure however poses a problem for peak-picking. Peaks
appear at integer multiples of either F0 or lag T, such that sometimes,
by coincidence or due to estimation errors, the harmonic peaks can be
higher than the primary peak. Such estimation errors are known
as *octave errors*, because the error in F0 corresponds to the musical
interval of an octave. A typical post-processing step is therefore to
check for octave jumps. We can check whether F0/2 or F0/3 would
correspond to a sensible F0. Alternatively, we can check whether the
previous analysis frame had an F0 which an octave or two octaves off.
Depending on application, we can then fix errors or label problematic
zones for later use.

Another problem with peak-picking is that peak locations might not align
with the samples. For example in the autocorrelation domain, the true
length of the period could be 100.3 samples. However, the peak in the
autocorrelation would then appear at lag 100. One approach would then be
to use quadratic interpolation between samples in the vicinity of a peak
and use the location of the maximum of the interpolated peak as an
estimate of the peak location. Interpolation makes the estimate less
sensitive to noise. For example, background noise could happen to have a
peak at lag 102, such that desired maximum of 100 is lower than the peak
at 102. By using data from more samples, as in the interpolation
approach, we can therefore reduce the likelihood that a single corrupted
data point would cause an error.

An alternative approach to peak-picking is to use all distinctive peaks
to jointly estimate the F0. That is, if you find *N* peaks at
frequencies *p<sub>k</sub>*, which approximately correspond to harmonic
peaks *kF0*, then you can approximate \\( F0 \\approx \\frac1N
\\sum\_{k=1}^N p_k/k. \\) Another alternative is to calculate the
distance between consecutive peaks an estimate \\( F0 \\approx
\\frac1{N-1} \\sum\_{k=1}^{N-1} (p\_{k+1}-p_k). \\) We can also combine
these methods as we like.

In many other applications, we use discrete Fourier transform (DFT) or
cosine transforms (DCT) to resolve frequency components. It would
therefore be tempting to apply the same approach also here. In such a
domain we would also already have a joint estimate which does not rely
on single data points. However, note that the spectrum is already the
DFT of the time signal and the cepstrum is the DCT or DFT of the
log-spectrum. Additional transforms therefore usually do not resolve the
ambiguity between harmonics. 

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

</div>
