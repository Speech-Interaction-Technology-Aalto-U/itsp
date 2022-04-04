# Fundamental frequency (F0)

<div class="contentLayout2">

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

The fundamental frequency of a speech signal, often denoted by F0 or
F<sub>0</sub>, refers to the approximate frequency of the
(quasi-)periodic structure of voiced speech signals. The oscillation
originates from the vocal folds, which oscillate in the airflow when
appropriately tensed. The fundamental frequency is defined as the
average number of oscillations per second and expressed in Hertz. Since
the oscillation originates from an organic structure, it is not exactly
periodic but contains significant fluctuations. In particular, amount of
variation in period length and amplitude are known respectively as
*jitter* and *shimmer*. Moreover, the F0 is typically not stationary,
but changes constantly within a sentence. In fact, the F0 can be used
for expressive purposes to signify, for example, emphasis and questions.

Typically fundamental frequencies lie roughly in the range *80* to *450
Hz*, where males have lower voices than females and children. The F0 of
an individual speaker depends primarily on the length of the vocal
folds, which is in turn correlated with overall body size. Cultural and
stylistic aspects of speech naturally have also a large impact.

The fundamental frequency is closely related to *pitch*, which is
defined as our perception of fundamental frequency. That is, the F0
describes the actual physical phenomenon, whereas pitch describes how
our ears and brains interpret the signal, in terms of periodicity. For
example, a voice signal could have an F0 of 100 Hz. If we then apply a
high-pass filter to remove all signal components below 450 Hz, then that
would remove the actual fundamental frequency. The lowest remaining
periodic component would be 500 Hz, which correspond to the fifth
harmonic of the original F0. However, a human listener would then
typically still perceive a pitch of 100 Hz, even if it does not exist
anymore. The brain somehow reconstructs the fundamental from the upper
harmonics. This well-known phenomenon is however still not completely
understood. 

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

A speech signal with a fundamental frequency of approximately F0=93Hz.

<img src="attachments/149890776/175515681.png"
data-image-src="attachments/149890776/175515681.png"
data-unresolved-comment-count="0" data-linked-resource-id="175515681"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="aaa_wav.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="149890776"
data-linked-resource-container-version="15" height="250" />

The spectrum of a speech signal with a fundamental frequency of
approximately F0=93Hz (original) and a high-pass filtered version of it
such that the fundamental frequency has been removed (high-pass
filtered).

<img src="attachments/149890776/175515679.png"
data-image-src="attachments/149890776/175515679.png"
data-unresolved-comment-count="0" data-linked-resource-id="175515679"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="aaa_highpass.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="149890776"
data-linked-resource-container-version="15" height="250" />

A speech signal with a fundamental frequency of approximately F0=93Hz
<a href="attachments/149890776/175515683.wav"
data-linked-resource-id="175515683" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="aaa.wav" data-nice-type="Multimedia"
data-linked-resource-content-type="audio/x-wav"
data-linked-resource-container-id="149890776"
data-linked-resource-container-version="15">aaa.wav</a> and a high-pass
filtered version of it such that the fundamental frequency has been
removed <a href="attachments/149890776/175515684.wav"
data-linked-resource-id="175515684" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="aaa_highpass.wav"
data-nice-type="Multimedia"
data-linked-resource-content-type="audio/x-wav"
data-linked-resource-container-id="149890776"
data-linked-resource-container-version="15">aaa_highpass.wav</a>.

  

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

If *F*<sub>0</sub> is the fundamental frequency, then the length of a
single period in seconds is

\\\[ T=\\frac{1}{F_0}. \\\]

The speech waveform thus repeats itself after every *T* seconds.

A simple way of modelling the fundamental frequency is to repeat the
signal after a delay of *T* seconds. If a signal is sampled with a
sampling rate of *F<sub>s</sub>*, then the signal repeats after a delay
of *L* samples where

\\\[ L = F_s T = \\frac{F_s}{F_0}. \\\]

A signal *x<sub>n</sub>* then approximately repeats itself such that

\\\[ x_n \\approx x\_{n-L} \\approx x\_{n-2L} \\approx x\_{n-3L}. \\\]

In the Z-domain this can be modelled by an IIR-filter as

\\\[ B(z) = 1 - \\gamma_L z^{-L}, \\\]

where the scalar \\( 0\\leq\\gamma_L\\leq 1 \\) scales with the accuracy
of the period. The Z-transform of the signal *x<sub>n</sub>* can then be
written as \\( X(z)=B^{-1}(z) E(z), \\) where *E(z)* is the Z-transform
of a single period.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

Segment of a speech signal, with the period length *L*, and fundamental
frequency *F0=1/L*.<img src="attachments/149890776/149891410.png"
data-image-src="attachments/149890776/149891410.png"
data-unresolved-comment-count="0" data-linked-resource-id="149891410"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="f0_L.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="149890776"
data-linked-resource-container-version="15" height="250" />

  

Spectrum of speech signal with the fundamental frequency *F<sub>0</sub>*
and harmonics *kF*<sub>0</sub>**, as well as the
formants *F1*, *F2*, *F3*... Notice how the harmonics form a regular
comb-structure.

<img src="attachments/149890776/175515678.png"
data-image-src="attachments/149890776/175515678.png"
data-unresolved-comment-count="0" data-linked-resource-id="175515678"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="f0_formants.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="149890776"
data-linked-resource-container-version="15" height="250" />

  

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

The magnitude spectrum of *B<sup>-1</sup>(z)*, has then a periodic
comb-structure. That is, the magnitude spectrum has peaks at \\( k\\,F_0
\\) , for integer *k.  
*For a discussion about the fundamental frequency in the cepstral
domain, see [Cepstrum and MFCC](Cepstrum_and_MFCC).

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

Spectrum of fundamental frequency model *B<sup>-1</sup>(z)*, showing the
characteristic comb-structure with harmonic peaks appearing at integer
multiples of *F0*.

<img src="attachments/149890776/149891452.png"
data-image-src="attachments/149890776/149891452.png"
data-unresolved-comment-count="0" data-linked-resource-id="149891452"
data-linked-resource-version="2" data-linked-resource-type="attachment"
data-linked-resource-default-alias="comb.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="149890776"
data-linked-resource-container-version="15" height="250" />

</div>

</div>

</div>

</div>

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[f0_L.png](attachments/149890776/149891410.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[comb.png](attachments/149890776/149891453.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[comb.png](attachments/149890776/149891452.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[f0_formants.png](attachments/149890776/175515678.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[aaa_highpass.png](attachments/149890776/175515679.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[aaa_wav.png](attachments/149890776/175515681.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[aaa.wav](attachments/149890776/175515683.wav) (audio/x-wav)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[aaa_highpass.wav](attachments/149890776/175515684.wav) (audio/x-wav)  

</div>
