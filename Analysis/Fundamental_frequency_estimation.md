# Fundamental frequency estimation


The [fundamental frequency (F0)](Fundamental_frequency_F0) is central
in describing speech signals whereby we need methods for estimating the
$F_0$ from speech signals. In speech analysis applications, it can be
informative to study the absolute value of the fundamental frequency as
such, but more commonly, extraction of the $F_0$ is usually a
pre-processing step. For example, in [recognition
tasks](Recognition_tasks_in_speech_processing), $F_0$ is often used as a
feature for machine learning methods. A voice activity detector could,
for instance, set a lower and higher threshold on the $F_0$, such that
sounds with an $F_0$ outside the valid range would be classified as
non-speech.

The fundamental frequency is visible in multiple different domains:

-   In an acoustic time-signal, the $F_0$ is visible as a repetition after
    every $T$ samples.
-   In the [autocovariance or
    -correlation](Autocorrelation_and_autocovariance), the $F_0$ is visible
    as a peak at lag $T$ as well as its integer multiples $kT$.
-   In the magnitude, power or log-magnitude
    [spectrum](Spectrogram_and_the_STFT), the $F_0$ is visible as a peak at
    the frequency $F_0=F_{s}/T$, as well as its integer
    multiples, where $F_{s}$ is the sampling frequency.
-   In the [cepstrum](Cepstrum_and_MFCC), the $F_0$ is visible as a peak at
    quefrency $T$ as well as its integer multiples $kT$.

Consequently, we can use any of these domains to estimate the
fundamental frequency $F_0$. A typical approach applicable in all domains
except the time-domain, is peak-picking. The fundamental frequency
corresponds to a peak in each domain, such that we can determine the $F_0$
by finding the highest peak. For better robustness to spurious peaks and
for computational efficiency, we naturally limit our search to the range
of valid $F_0$'s, such as  $ 80\leq F_0\leq 450. $  

The harmonic structure however poses a problem for peak-picking. Peaks
appear at integer multiples of either $F_0$ or lag T, such that sometimes,
by coincidence or due to estimation errors, the harmonic peaks can be
higher than the primary peak. Such estimation errors are known
as *octave errors*, because the error in $F_0$ corresponds to the musical
interval of an octave. A typical post-processing step is therefore to
check for octave jumps. We can check whether $F_0/2$ or $F_0/3$ would
correspond to a sensible $F_0$. Alternatively, we can check whether the
previous analysis frame had an $F_0$ which an octave or two octaves off.
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
to jointly estimate the $F_0$. That is, if you find $N$ peaks at
frequencies $p_{k}$, which approximately correspond to harmonic
peaks $kF0$, then you can approximate $ F_0 \approx \frac1N
\sum_{k=1}^N p_k/k. $ Another alternative is to calculate the
distance between consecutive peaks an estimate $ F_0 \approx
\frac1{N-1} \sum_{k=1}^{N-1} (p_{k+1}-p_k). $ We can also combine
these methods as we like.

In many other applications, we use discrete Fourier transform (DFT) or
cosine transforms (DCT) to resolve frequency components. It would
therefore be tempting to apply the same approach also here. In such a
domain we would also already have a joint estimate which does not rely
on single data points. However, note that the spectrum is already the
DFT of the time signal and the cepstrum is the DCT or DFT of the
log-spectrum. Additional transforms therefore usually do not resolve the
ambiguity between harmonics. 

