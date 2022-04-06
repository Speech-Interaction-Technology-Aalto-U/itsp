# Deprecated! Pending to be removed

# Waveform

Speech signals are sound signals, defined as pressure variations
travelling through the air. These variations in pressure can be
described as waves and correspondingly they are often called sound
waves. In the current context, we are primarily interested in analysis
and processing of such waveforms in digital systems. We will therefore
always assume that the acoustic speech signals have been captured by a
microphone and converted to a digital form.

A speech signal is then represented by a sequence of numbers $ x_n $
, which represent the relative air pressure at time-instant $
n\in{\mathbb N} $ .  This representation is known as [pulse code
modulation](https://en.wikipedia.org/wiki/Pulse-code_modulation) often
abbreviated as *PCM*. The accuracy of this representation is then
specified by two factors; 1) the sampling frequency (the step in time
between $n$ and $n+1$) and 2) the accuracy and distribution of
amplitudes of $x_n$.

<img src="../attachments/148294912/148294966.png"
data-image-src="../attachments/148294912/148294966.png"
data-unresolved-comment-count="0" data-linked-resource-id="148294966"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="sample_sentence-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148294912"
data-linked-resource-container-version="30" height="250" />


## Sampling rate

[Sampling](https://en.wikipedia.org/wiki/Sampling_(signal_processing))
is a classic topic of signal processing. Here the most important aspect
is the Nyquist frequency, which is half the sampling rate
$F_s$ and defines the upper end of the largest bandwidth $
\left[0, \frac{F_s}2\right] $ which can be uniquely represented.
In other words, if the sampling frequency would be 8000 Hz, then signals
in the frequency range 0 to 4000 Hz can be uniquely described with this
sampling frequency. The AD-converter would then have to contain a
low-pass filter which removes any content above the Nyquist frequency.

The most important information in speech signals are the formants, which
reside in the range 300 Hz to 3500 Hz, such that a lower limit for the
sampling rate is around 7 or 8kHz. In fact, first digital speech codecs
like the AMR-NB use a sampling rate of 8 kHz known as narrow-band. Some
consonants, especially fricatives like /s/, however contain substantial
energy above 4kHz, whereby narrow-band is not sufficient for high
quality speech. Most energy however remains below 8kHz such that
wide-band, that is, a sampling rate of 16 kHz is sufficient for most
purposes. Super-wide band and full band further correspond,
respectively, to sampling rates of 32 kHz and 44.1 kHz (or 48kHz). The
latter is also the sampling rate used in compact discs (CDs). Such
higher rates are useful when considering also non-speech signals like
music and generic audio.

  


Frequency-range of different bandwidth-definitions

<img src="../attachments/148296254/175528670.png"
data-image-src="../attachments/148296254/175528670.png"
data-unresolved-comment-count="0" data-linked-resource-id="175528670"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="bandwidth-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" width="600" />

  

Sound samples at different sampling rates / bandwidths


<table class="wrapped confluenceTable">
<tbody>
<tr class="header">
<th class="confluenceTh">Bandwidth</th>
<th class="confluenceTh">Sound sample</th>
</tr>

<tr class="odd">
<td class="confluenceTd"><div class="content-wrapper">
<p>Narrowband (300 Hz to 3.3 kHz)</p>
</div></td>
<td class="confluenceTd"><div class="content-wrapper">
<p><a href="../attachments/148296254/203122322.wav"
data-linked-resource-id="203122322" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="speechexample_300_3300.wav"
data-nice-type="Multimedia"
data-linked-resource-content-type="audio/x-wav"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24">speechexample_300_3300.wav</a></p>
</div></td>
</tr>
<tr class="even">
<td class="confluenceTd">Wideband (50 Hz to 7 kHz)</td>
<td class="confluenceTd"><div class="content-wrapper">
<p><a href="../attachments/148296254/203122321.wav"
data-linked-resource-id="203122321" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="speechexample_50_7000.wav"
data-nice-type="Multimedia"
data-linked-resource-content-type="audio/x-wav"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24">speechexample_50_7000.wav</a></p>
</div></td>
</tr>
<tr class="odd">
<td class="confluenceTd" style="text-align: center;">Superwideband (50
Hz to 16 kHz)</td>
<td class="confluenceTd" style="text-align: center;"><div
class="content-wrapper">
<p><a href="../attachments/148296254/203122319.wav"
data-linked-resource-id="203122319" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="speechexample_50_16000.wav"
data-nice-type="Multimedia"
data-linked-resource-content-type="audio/x-wav"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24">speechexample_50_16000.wav</a></p>
</div></td>
</tr>
<tr class="even">
<td class="confluenceTd">Fullband (50 Hz to 22 kHz)</td>
<td class="confluenceTd"><div class="content-wrapper">
<p><a href="../attachments/148296254/203122318.wav"
data-linked-resource-id="203122318" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="speechexample_50_22000.wav"
data-nice-type="Multimedia"
data-linked-resource-content-type="audio/x-wav"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24">speechexample_50_22000.wav</a></p>
</div></td>
</tr>
<tr class="odd">
<td class="confluenceTd">Original (0 to 22050 Hz)</td>
<td class="confluenceTd"><div class="content-wrapper">
<p><a href="../attachments/148296254/203122316.wav"
data-linked-resource-id="203122316" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="speechexample.wav"
data-nice-type="Multimedia"
data-linked-resource-content-type="audio/x-wav"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24">speechexample.wav</a></p>
</div></td>
</tr>
</tbody>
</table>


## Accuracy and distribution of steps on the amplitude axis

In digital representations of a signal you are forced to use a finite
number of steps to describe the amplitude. In practice, we must quantize
the signal to some discrete levels.


### Linear quantization

Linear quantization with a step size $\Delta q $ would correspond
to defining the quantized signal as 
$$ \hat x = \Delta q\,\cdot {\mathrm{round}}(x/\Delta q). $$
The intermediate representation, $ y={\mathrm{round}}(x/\Delta q),
$ can then be taken to represent, for example, signed 16-bit integers.
Consequently, the quantization step size  $ \Delta q $ has to be
then chosen such that $y$ remains in the range  $
y\in(-2^{15},\,2^{15}] $ to avoid numerical overflow.

The beauty of this approach is that it is very simple to implement. The
drawback is that this approach is sensitive to the choice of the
quantization step size. To make use of the whole range and thus get best
accuracy for $x$, we should choose the smallest  $ \Delta q $ where
we still remain within the bounds of integers. This is difficult because
the amplitudes of speech signals vary on a large range. 

  


<img src="../attachments/148296254/149882928.png"
data-image-src="../attachments/148296254/149882928.png"
data-unresolved-comment-count="0" data-linked-resource-id="149882928"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="quantization_uniform.png-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" height="150" />

  


### Logarithmic quantization and mu-law

To retain equal accuracy for loud and weak signals, we *could* quantize
on an logarithmic scale as 
$$ \hat x = {\mathrm{sign}}(x)\cdot\exp\left[ \Delta
q\cdot\,{\mathrm{round}} \left(\log\left(\|x\|\right)/\Delta
q\right) \right]. $$
Such operations which limit the detrimental effects of limited range are
known as *[companding](https://en.wikipedia.org/wiki/Companding)*
algorithms.

Here the intermediate representation is  $ y = {\mathrm{round}}
\left(\log\left(\|x\|\right)/\Delta q\right) $ which can be
reconstructed by  $ \hat x = {\mathrm{sign}}(x)\cdot\exp\left[
\Delta q\cdot\,\|y\| \right]. $ A benefit of this approach would
be that we can encode signals on a much larger range and the
quantization accuracy is relative to the signal magnitude.
Unfortunately, very small values cause catastrophic problems. In
particular, for $x=0$, the intermediate value goes to negative infinity 
$ y=-\infty, $ which is not realizable in finite digital systems.

A practical solution to this problem is quantization with the mu-law
algorithm, which defines a modified logarithm as

$$
F(x):={\mathrm{sign}}(x)\cdot\,\frac{\log\left(1+\mu\|x\|\right)}{\left(1+\mu\right)}.
$$

By replacing the logarithm with $F(x)$, we retain the properties of the
logarithm for large $x$, but avoid the problems when $x$ is small.


<img src="../attachments/148296254/149882926.png"
data-image-src="../attachments/148296254/149882926.png"
data-unresolved-comment-count="0" data-linked-resource-id="149882926"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="quantization_log.png-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" height="150" />

<img src="../attachments/148296254/149882927.png"
data-image-src="../attachments/148296254/149882927.png"
data-unresolved-comment-count="0" data-linked-resource-id="149882927"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="quantization_mulaw.png-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" height="150" />


## Wav-files

The most typical format for storing sound signals is the [wav-file
format](https://en.wikipedia.org/wiki/WAV). It is basically merely a way
to store a time sequence, with typically either 16 or 32 bit accuracy,
as integer, mu-law or float. Sampling rates can vary in a large range
between 8 and 384 kHz. The files typically have no compression (no
lossless nor lossy coding), such that recording hours of sound can
require a lot of disk space. For example, an hour of mono (single
channel) sound with a sampling rate of 44.1kHz requires 160 MB of disk
space.


## Adaptive quantization, APCM

-   To obtain a uniform quantization error during single phones or
    sentences, the quantization error has to change slowly over time.
-   In *adaptive quantization* (adaptive PCM or APCM) the quantization
    step size is adapted slowly such that
    -   the available quantization levels cover a sufficient range such
        that numerical overflow can be avoided,
    -   the quantization error is stable over time and
    -   as long as the above constraints are fulfilled, quantization
        error is minimized.
-   An alternative, equivalent implementation to the change in
    quantization step size is to apply an adaptive gain to the input
    signal before quantization.


<img src="../attachments/148296254/175529208.png"
data-image-src="../attachments/148296254/175529208.png"
data-unresolved-comment-count="0" data-linked-resource-id="175529208"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="apcm_ff_q_re-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" width="450" />

<img src="../attachments/148296254/175529206.png" class="image-center"
data-image-src="../attachments/148296254/175529206.png"
data-unresolved-comment-count="0" data-linked-resource-id="175529206"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="apcm_ff_g_re-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" width="500" />


### Adaptive quantization with the feed-forward algorithm using an adaptive quantization step

-   The feed-forward algorithm requires that in addition to the
    quantized signal, also the gain-coefficients or the quantization
    step is transmitted to the recipient.

    -   Transmitting such extra information increases the bit-rate,
        whereby the feed-forward algorithm is not optimal for
        applications which try to minimize transmission rate.


<img src="../attachments/148296254/175529207.png"
data-image-src="../attachments/148296254/175529207.png"
data-unresolved-comment-count="0" data-linked-resource-id="175529207"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="apcm_ff_q2_re-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" width="500" />


### Adaptive quantization with the feed-forward algorithm using an adaptive gain (compressor)

-   In *feed-backward* algorithms the quantization step or
    gain-coefficient is determined from previous samples which are
    already quantized.
-   Since the previous samples are available also at the decoder, the quantization step or gain-coefficient can be determined also at the decoder without extra transmitted information.
-   If the signal grows very rapidly, this approach can however not guarantee that there are no numerical overflows, since adaptation is performed only after quantization.


<img src="../attachments/148296254/175529205.png"
data-image-src="../attachments/148296254/175529205.png"
data-unresolved-comment-count="0" data-linked-resource-id="175529205"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="apcm_ff_g2_re-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" width="500" />


### Adaptive quantization with the feed-backward algorithm using an adaptive quantization step

-   Note that the feed-forward algorithms all require transmission of the scaling or gain coefficient, which can increase demand on bandwidth and adds to the complexity of the system.
-   The parallel transmission line can be avoided by predicting those
    coefficients from previously transmitted elements, with a
    feed-backward algorithm.


<img src="../attachments/148296254/175529204.png" class="image-center"
data-image-src="../attachments/148296254/175529204.png"
data-unresolved-comment-count="0" data-linked-resource-id="175529204"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="apcm_fb_q_re-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" width="500" />


### Adaptive quantization with the feed-backward algorithm using an adaptive gain coefficient

-   The feed-backward algorithm can naturally be applied on gain
    adaptation as well.


<img src="../attachments/148296254/175529203.png"
data-image-src="../attachments/148296254/175529203.png"
data-unresolved-comment-count="0" data-linked-resource-id="175529203"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="apcm_fb_g_re-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" width="550" />


#### Differential quantization DPCM

-   In *differential quantization* we predict the subsequent sample,
    whereby we can quantize only the difference between the prediction
    and the actual sample.
-   If the predictor is simply $ \tilde x_k:=x\_{k-1}, $ then
        the error is $ e_k = x_k - \tilde x_k = x_k - x\_{k-1}. $
-   The first difference (delta modulation) is the simplest  predictor, which uses the assumption that subsequent samples are highly correlated.
-   The reconstruction is obtained by reorganization of terms as $ x_k = e_k + x\_{k-1}. $
-   Observe that the reconstruction is needed at both the encoder and decoder, to feed the predictor.
-   NB: At this point the flow-graphs start to get a bit complicated         as there are several feedback loops.
-   More generally, we can use a predictor $P$, which predicts a sample
    based on a weighted sum of previous samples
    $$ \tilde x_k = -\sum\_{h=1}^M a_h x\_{k-h}, $$
    where the scalars  $ a_h $  are the predictor parameters.
-   A feed-backward would here use the past quantized samples $ \hat
    x_k. $


<img src="../attachments/148296254/175529209.png"
data-image-src="../attachments/148296254/175529209.png"
data-unresolved-comment-count="0" data-linked-resource-id="175529209"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="dpcm_re-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" width="550" />


### Adaptive and differential quantization with feed-forward

-   The differential, source-model based quantization can naturally be combined with adaptive, perception-based quantization.
-   The adaptive differential PCM (ADPCM) adaptively predicts the signal and adaptively choosing the quantization step.


<img src="../attachments/148296254/175529202.png" class="image-center"
data-image-src="../attachments/148296254/175529202.png"
data-unresolved-comment-count="0" data-linked-resource-id="175529202"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="adpcm_re-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" width="600" />


### Adaptive differential quantization with feed-backward

-   The ADPCM can again, naturally, be implemented as a feed-backward algorithm as well.

### Adaptive differential quantization w/ adaptive predictor

-   A differential quantizer can be further improved by letting also the
    predictor be adaptive.
-   The predictor learns adaptively properties of the signal.
-   The flow-graph becomes complicated and is omitted here.


<img src="../attachments/148296254/175529201.png"
data-image-src="../attachments/148296254/175529201.png"
data-unresolved-comment-count="0" data-linked-resource-id="175529201"
data-linked-resource-version="2" data-linked-resource-type="attachment"
data-linked-resource-default-alias="adpcm_fb_re-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" width="650" /><img src="../attachments/148296254/175529201.png"
data-image-src="../attachments/148296254/175529201.png"
data-unresolved-comment-count="0" data-linked-resource-id="175529201"
data-linked-resource-version="2" data-linked-resource-type="attachment"
data-linked-resource-default-alias="adpcm_fb_re-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" width="650" />


### Comparison of the SNR of different quantizers (not perceptual)

-   The more bits we can use the better the quality (Duh!).
-   The more prior information we can use about the signal the better
    the efficiency (SNR/bits).
    -   More advanced models (can) improve quality.
    -   More parameters (can) improve quality.
    -   It would naturally also be entirely possible to create
        complicated models which do not improve quality, but simple
        models can go only so far.
-   The linear prediction -approach can be extended into a full-blown
    speech production model (see separate chapter).
-   Note that quality as measured by SNR does not necessarily reflect
    perceptual quality.

  

<img src="../attachments/148296254/175529210.png"
data-image-src="../attachments/148296254/175529210.png"
data-unresolved-comment-count="0" data-linked-resource-id="175529210"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="quant_comp_re.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" height="400" />

[Adapted from Noll,
1975.](https://doi.org/10.1002/j.1538-7305.1975.tb02053.x)

  

## Source modelling in quantization

-   Adaptive quantization is based on our understanding of perception;
    we use the knowledge that we prefer slowly changing quantization
    errors.
    -   This is a simple *perceptual model*.
    -   Perceptual models are *quality evaluation* models.
-   When we know that the signal is *speech*, we can use that to further
    improve quantization.
    -   Models of speech signals are known as *source* models.
-   At its simplest form, we can use the fact that voiced phones are
    fairly continuous signals = they have low-pass character = are
    dominated by low-frequency components.
    -   Samples have a high correlation.
    -   The difference between subsequent samples is much smaller than
        the magnitude of samples!
-   The amplitude of the first difference is 41% of the original.
-   Uniform quantization of the first difference thus gives a 59%
    reduction in the range which is approx 1 bitsample. At 44kHz that
    would be 44kbit/s improvement in bitrate, which is definitely
    noticeable.


<img src="../attachments/148296254/175529216.png" class="image-center"
data-image-src="../attachments/148296254/175529216.png"
data-unresolved-comment-count="0" data-linked-resource-id="175529216"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="puhesignaali-1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148296254"
data-linked-resource-container-version="24" height="400" />


## Conclusion

-   Time-domain representation of speech signals is simple in
    floating-point processors.
    -   We only need to choose a sampling rate (typically in the range 8
        to 48 kHz).
-   For fixed-point and lower-bitrate representations, we have several
    considerations and options;
    -   We would like the quantization noise to be relative to the
        signal magnitude but stable over time for best perceptual
        quality.
    -   We can use information about signal properties to improve
        efficiency with a source model.
    -   If we want to reduce bit-rate, then we must make sure that the
        required information to decode the signal is available also at
        the receiving end.
-   Practical processing algorithms for speech operate on a digital
    representation of the acoustic signal.
    -   Accuracy is determined by sampling rate and quantization.
-   Most common (high-quality) storage format for digital speech and
    audio signals is PCM (such as WAV-files).
-   Some very basic analysis tools for speech signals include the
    autocorrelation and the zero-crossing rate.
-   Many classical DSP algorithms, in their flow-grap representation,
    are very much alike modern machine learning methods.

  
  

