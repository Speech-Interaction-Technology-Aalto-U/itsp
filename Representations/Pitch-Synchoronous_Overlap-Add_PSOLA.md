# Pitch-Synchoronous Overlap-Add (PSOLA)

<div class="contentLayout2">

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

Many speech applications require the ability to modify the fundamental
frequency. For a classic but marginal application, think of the
[auto-tune](https://en.wikipedia.org/wiki/Auto-Tune) function often used
in post-processing of singing voices. With such tools it is possible to
change the fundamental frequency of a speaker's or singer's voice
without changing the phoneme or timbre of the sound. One of the more
popular tools developed for this purpose is pitch-synchronous
overlap-add (PSOLA). Like the name suggests, it is closely related to
the overlap-add method used in the [short-time Fourier
transform](Spectrogram_and_the_STFT) algorithm. It allows changing the
pitch of a speech sound without modifying or with only minor influence
on other characteristics of the signal, such as vowel-identity. In
addition to auto-tune, an important application of PSOLA is [speech
synthesis](https://en.wikipedia.org/wiki/Speech_synthesis), where we
want to be able generate speech with any reasonable pitch contour. Voice
conversion is another application, where the objective is to convert the
speech of one person, such that it sounds like speech of another person.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

Illustration of the PSOLA process; find period length and maximum peak
in each period.

<img src="attachments/155477136/175514551.png"
data-image-src="attachments/155477136/175514551.png"
data-unresolved-comment-count="0" data-linked-resource-id="175514551"
data-linked-resource-version="2" data-linked-resource-type="attachment"
data-linked-resource-default-alias="psola1.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="155477136"
data-linked-resource-container-version="5" width="400" />

  

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

The basic idea of PSOLA is to decompose the signal into individual
pitch-periods, such that we can move the pitch-periods to change the
effective length of those periods. That is, the fundamental frequency of
a signal is expressed as a periodic structure of the time-signal. If we
cut the signal into segment corresponding to the length of such periodic
structures, then we can shift their positions as desired and then add
them back together, like in the overlap-add process (see STFT). Since
short-term correlations in the signal are not changed, that is, signal
inside the windows/segments is not changed, then the spectral envelope
of the signal is not changed.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

PSOLA analysis windowing, time-shift and synthesis windowing

<img src="attachments/155477136/175514552.png"
data-image-src="attachments/155477136/175514552.png"
data-unresolved-comment-count="0" data-linked-resource-id="175514552"
data-linked-resource-version="2" data-linked-resource-type="attachment"
data-linked-resource-default-alias="psola2.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="155477136"
data-linked-resource-container-version="5" width="400" />

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

To illustrate the principle, consider the following basic algorithm:

1.  Estimate the fundamental frequency contour of a speech sample.
2.  Find pitch periods of the speech sample, for example by identifying
    the largest peak in each period.
3.  Extract windows of the speech signal covering *two* pitch periods.
    Apply a [windowing function](Windowing) with perfect reconstruction.
    (Observe: Perfect reconstruction should apply for each period, so we
    construct half-length windows for each period. Conversely, the left
    and right parts of windows can be of different length.)
4.  Shift windows to match the desired pitch-period length.

In the sound examples on the right, the pitch period lengths are
adjusted by a fixed multiplier to increase or decrease the fundamental
frequency. Observe that the implementation is not perfectly tuned such
that the output sound has some audible distortions.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

Sound examples with varying multiplier on distance between pitch periods

-   <a href="attachments/155477136/175514533.wav"
    data-linked-resource-id="175514533" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="sound_example_psola0.6.wav"
    data-nice-type="Multimedia"
    data-linked-resource-content-type="audio/x-wav"
    data-linked-resource-container-id="155477136"
    data-linked-resource-container-version="5">sound_example_psola0.6.wav</a>
-   <a href="attachments/155477136/175514532.wav"
    data-linked-resource-id="175514532" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="sound_example_psola0.8.wav"
    data-nice-type="Multimedia"
    data-linked-resource-content-type="audio/x-wav"
    data-linked-resource-container-id="155477136"
    data-linked-resource-container-version="5">sound_example_psola0.8.wav</a>
-   <a href="attachments/155477136/175514531.wav"
    data-linked-resource-id="175514531" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="sound_example_psola0.9.wav"
    data-nice-type="Multimedia"
    data-linked-resource-content-type="audio/x-wav"
    data-linked-resource-container-id="155477136"
    data-linked-resource-container-version="5">sound_example_psola0.9.wav</a>
-   <a href="attachments/155477136/175514530.wav"
    data-linked-resource-id="175514530" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="sound_example_psola1.wav"
    data-nice-type="Multimedia"
    data-linked-resource-content-type="audio/x-wav"
    data-linked-resource-container-id="155477136"
    data-linked-resource-container-version="5">sound_example_psola1.wav</a>
    (original)
-   <a href="attachments/155477136/175514529.wav"
    data-linked-resource-id="175514529" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="sound_example_psola1.1.wav"
    data-nice-type="Multimedia"
    data-linked-resource-content-type="audio/x-wav"
    data-linked-resource-container-id="155477136"
    data-linked-resource-container-version="5">sound_example_psola1.1.wav</a>
-   <a href="attachments/155477136/175514528.wav"
    data-linked-resource-id="175514528" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="sound_example_psola1.2.wav"
    data-nice-type="Multimedia"
    data-linked-resource-content-type="audio/x-wav"
    data-linked-resource-container-id="155477136"
    data-linked-resource-container-version="5">sound_example_psola1.2.wav</a>
-   <a href="attachments/155477136/175514527.wav"
    data-linked-resource-id="175514527" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="sound_example_psola1.4.wav"
    data-nice-type="Multimedia"
    data-linked-resource-content-type="audio/x-wav"
    data-linked-resource-container-id="155477136"
    data-linked-resource-container-version="5">sound_example_psola1.4.wav</a>

  

</div>

</div>

</div>

</div>

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[sound_example_psola1.4.wav](attachments/155477136/175514527.wav)
(audio/x-wav)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[sound_example_psola1.2.wav](attachments/155477136/175514528.wav)
(audio/x-wav)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[sound_example_psola1.1.wav](attachments/155477136/175514529.wav)
(audio/x-wav)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[sound_example_psola1.wav](attachments/155477136/175514530.wav)
(audio/x-wav)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[sound_example_psola0.9.wav](attachments/155477136/175514531.wav)
(audio/x-wav)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[sound_example_psola0.8.wav](attachments/155477136/175514532.wav)
(audio/x-wav)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[sound_example_psola0.6.wav](attachments/155477136/175514533.wav)
(audio/x-wav)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[psola1.png](attachments/155477136/175514554.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[psola2.png](attachments/155477136/175514555.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[psola1.png](attachments/155477136/175514551.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[psola2.png](attachments/155477136/175514552.png) (image/png)  

</div>
