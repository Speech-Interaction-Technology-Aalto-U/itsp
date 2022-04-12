# Voice activity detection (VAD)

<div class="contentLayout2">

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Introduction and motivation

Many speech processing algorithms are resource intensive and require
significant computing power or transmission bandwidth. Yet speech is
discontinuous such that we often have pauses between sentences and
breaks even within sentences. Moreover, in a dialogue, a speaker would
typically use polite turn-taking, such that others are silent when one
person is speaking. Resource-intensive processing is not necessary
during breaks in speech. Consequently, there is great potential in
saving resources by deactivating advanced speech processing methods
whenever the input signal does not contain speech.

*Voice activity detection* (VAD) refers to the task of determining
whether a signal contains speech or not. It is thus a binary decision. A
related task is to determine the *probability* that an input signal
contains speech or not, referred to as the *speech presence probability*
(SPP). The SPP is typically then expressed as the probability in the
range 0 to 1. Speech presence probability is typically an intermediate
step in voice activity detection, such that the voice activity
classification is obtained by thresholding the output of the speech
presence probability estimator.

Generally, voice activity detection algorithms are relatively simple,
such that the more complex tasks such as speech recognition, need to be
applied only when speech is present. Similarly, in speech coding, we
need to transmit speech only when speech is present and we can reduce
bitrate whenever speech is absent.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Problem formulation

For an input signal *x*, our objective is to determine whether it is
speech or not. We express the VAD algorithm as a function *y=VAD(x),*
where the desired target output is

\\\[ y^\* := \\begin{cases} 0, & x \\text{ is not speech,} \\\\ 1, & x
\\text{ is speech.} \\end{cases} \\\]

Correspondingly, the speech presence probability is the probability that
*x* is speech, *SPP(x)=P(x is speech).* A possible definition for the
VAD is then

\\\[ VAD(x) := \\begin{cases} 0, & SPP(x) \< \\theta\\\\ 1, & SPP(x)
\\geq \\theta, \\end{cases} \\\]

where θ is a scalar threshold. An example of speech presence probability
is illustrated in the following section.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Naïve approach 1 - Energy thresholding

A speech signal is not a stationary signal. Most prominently, sometimes
we speak energetically and sometimes we do not speak. It is then obvious
that *signal energy* can be used as an indicator of speech presence.
Speech adds energy to the signal, such that high-energy regions of the
signal are likely speech. For example, we can set a threshold \\(
\\theta\_{SILENCE} \\) such that when the energy of the signal \\(
\\sigma^2(x) \\) is above the threshold, the VAD indicates speech
activity

\\\[ VAD(x) := \\begin{cases} 0, & \\sigma^2(x) \<
\\theta\_{SILENCE}\\\\ 1, & \\sigma^2(x) \\geq \\theta\_{SILENCE}.
\\end{cases} \\\]

To implement this approach, we first apply [windowing](Windowing) to the
input signal with 30 ms windows and 50 % overlap. For each window, we
calculate signal energy as

\\\[ \\sigma^2(x) := \\\|x\\\|^2 = \\sum\_{k=0}^{N-1} x_k^2. \\\]

To choose a suitable threshold, in the figure on the right, we plot the
energy over a speech signal \\( \\sigma^2(x) \\) over a speech signal.
We can observe that areas in the speech signal with little activity have
an energy below 17 dB, whereby we can set the threshold at \\(
\\theta\_{SILENCE}:=17dB. \\) The resulting voice activity estimate is
illustrated in the lowest pane.

The result does seem reasonable. High-amplitude speech sounds are
clearly identified as speech. However, in the middle of the sentence,
the VAD frequently identifies non-speech frames. Is this correct?

In fact, it is not entirely clear what the output should be. It is a
matter of definition. On a heuristic level, we can define that speech
starts at the beginning of a sentence and finishes when the sentence
ends. But how should the VAD then handle sentences like "*What if ... we
would go on a holiday?.*" where there is a break in the middle of a
grammatically correct sentence. Should the break be identified as
non-speech? How long breaks do we allow? What about grammatically
incorrect sentence like "*We could go to..*."?

Moreover, sentences often have a trail-off, where the signal energy
decreases. For example in the figure on the right, the last word
diminishes in energy up to about the time 2.7 s, where the signal energy
goes below 10 dB. However, with the threshold of 17 dB, we have cut of
the VAD already before 2.6 s. If we would lower the threshold to 10dB,
then everything between 0.2 s and 1 s would be labelled incorrectly as
speech.

It is then clear that even in this simple example, it is not easy to set
a threshold which gives a good result. To make things worse, often
speech signals are corrupted by background noises, which makes
energy-thresholding even more difficult. To avoid labelling everything
as speech, the threshold must be higher, but then less of the speech
frames are labelled correctly. Which leads to the question, is it more
important to label speech or non-speech correctly?

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

Input sound sample

<a href="attachments/151500905/155463338.wav"
data-linked-resource-id="155463338" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="sound_example.wav"
data-nice-type="Multimedia"
data-linked-resource-content-type="audio/x-wav"
data-linked-resource-container-id="151500905"
data-linked-resource-container-version="27">sound_example.wav</a>

------------------------------------------------------------------------

VAD example with energy thresholding

<img src="attachments/151500905/155463332.png"
data-image-src="attachments/151500905/155463332.png"
data-unresolved-comment-count="0" data-linked-resource-id="155463332"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="vad.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="151500905"
data-linked-resource-container-version="27" width="640" />

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Performance criteria

The task of voice activity detection (VAD) is seemingly straightforward,
but even evaluation of performance is more difficult than one perhaps
would expect. As with the definition of correct labels, also the
performance criteria depend on the application;

-   In [speech transmission](Transmission_storage_and_telecommunication)
    (i.e. speech coding), we would like to save bandwidth by shutting
    off transmission when there is no speech present. However, turning
    off transmission during a speech segment would leave to severe
    degradations.
-   Some [speech enhancement](Speech_enhancement) algorithms can
    estimate noise-statistics during non-speech segments, which are
    identified using a VAD. During speech segments, the algorithm can
    then remove everything which looks like noise. If however speech is
    present in the segment where we estimate characteristics of the
    noise, then we would remove also such features which appear during
    noise segments. This would lead to a degradation of the desired
    speech signal.
-   In speech recognition, we would like to limit CPU usage by
    activating the algorithm only during speech segments. We would then
    like to be sure that no speech segments are omitted, because that
    would severely degrade output quality.
-   In wake-word spotting, we want to activate a device when a specific
    word is pronounced, such that the device can be in a sleep mode when
    the wake-word has not been pronounced. We can also turn the
    wake-word algorithm off for further reductions when there is no
    speech present. The latter functionality is achieved with the VAD.
    Overall, if some wake-words are missed, the user just has to say it
    again - no big deal. We can therefore allow some speech segments to
    be identified as non-speech. However, assuming that the wake-word
    spotting is not a too big load on the CPU, we can allow the VAD to
    be more sensitive. Detailed CPU cost vs. performance -optimization
    can however be complicated.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

We can observe that different applications emphasise different types of
errors. Speech transmission and recognition prefer a sensitive VAD where
we are certain that no speech-segments are lost. In contrast, speech
enhancement and wake-word spotting tend to prefer that the VAD is
conservative and labels audio to speech only when certain.

To quantify such differences, we can label performance with the
following attributes:

<div class="table-wrap">

|                     |                     |                     |
|---------------------|---------------------|---------------------|
| Input \\ VAD-output | VAD=Speech          | VAD=Non-speech      |
| Input=Speech        | True positive (TP)  | False negative (FN) |
| Input=Non-speech    | False positive (FP) | True negative (TN)  |

</div>

Then for example for speech recognition, we would penalise *less for
false positives* and penalise *more for false negatives*. In comparison,
in wake-word spotting, we would perhaps penalise equally for both false
positives and negatives. It really depends on your overall design.

In the above example of thresholding energy, we can then choose
different values for the threshold and plot the values for true positive
and negatives for each threshold (see figure on the right). Performance
for a threshold of 17 dB is indicated with a red cross. We can readily
see that there, all non-speech segments are correctly identified (TN=1
and FP=0), however, speech segments are not all correct (TP=0.72 and
FN=0.28). In fact, by reducing the threshold to 14.6 dB (yellow circle
in the figure), we would retain perfect false positives, (TN=1 and
FP=0), but we would improve false negatives (TP=0.80 and FN=0.20).

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

VAD performance in terms of percentage of true positives and true
negatives (left) and false negatives and false positives (right).

<img src="attachments/151500905/155463472.png"
data-image-src="attachments/151500905/155463472.png"
data-unresolved-comment-count="0" data-linked-resource-id="155463472"
data-linked-resource-version="3" data-linked-resource-type="attachment"
data-linked-resource-default-alias="vad_tptn.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="151500905"
data-linked-resource-container-version="27" width="640" />

  

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Naïve approach 2 - More features

To improve performance of the voice activity detector (VAD), we can
analyse more properties of the speech signal, which we usually call
*features*. For example, 

-   [*Linear predictors*](Linear_prediction) describe the spectral shape
    of speech signals efficiently. In other words, if the modelling
    error of a linear predictor is small, then the signal is likely a
    speech signal.

-   Alternatively, if we prefer a lower-complexity solution instead of
    linear prediction, we can analyse the normalised
    [autocorrelation](Autocorrelation_and_autocovariance) \\( c_k/c_0
    \\) at lag *k=1*. Speech signals are highly correlated over time,
    such that if the absolute value  \\( \|c_1\|/c_0 \\) is high, then
    it is likely a speech signal. However, noise signals can also have a
    negative correlation which is close to -1, such  
    that we can prefer to omit the absolute value.  
    An alternative which is roughly equivalent to the covariance at
    lag-1, is to use to [zero-crossing rate](Zero-crossing_rate).

-   Signals with a prominent [fundamental
    frequency](Fundamental_frequency_F0_) in the range which is typical
    to humans (approx 80 to 450 Hz) are likely to be voiced speech
    signals. However, unvoiced speech signals have by definition no
    fundamental frequency and would not be detected by this method.

-   [Mel-frequency cepstral coefficients (MFCCs)](Cepstrum_and_MFCC)
    have been shown to give excellent performance as features in many
    classification tasks.

These features can be further augmented by their trends over time. A
classic method is to measure time-derivatives, known as the deltas and
delta-deltas, defined for a feature  \\( f_k(t) \\) at time *t* as

\\\[ \\begin{cases} \\Delta_k(t) &= f_k(t) - f_k(t-1) \\\\
\\Delta\\Delta_k(t) &= \\Delta_k(t) - \\Delta_k(t-1). \\end{cases} \\\]

Alternatively, we can just consider features explicitly over time \\(
f_k(t-N) ... f_k(t). \\)  

We can use all these parameters and many more to effectively
characterize speech signals. The question however is how we can merge
the information from a vector of features into a single output value? A
naïve approach would be to implement a binary decision tree, such that
for example,

-   If energy is sufficiently high, then output is speech and we return
    VAD(x)=1.
-   If covariance is sufficiently high, then output is speech and we
    return VAD(x)=1.
-   If there is a prominent fundamental frequency in the range 80 to 450
    Hz, then return VAD(x) = 1.
-   Otherwise return VAD(x) = 0.

This is an entirely heuristic and non-scientific approach which is
difficult to design when the number of features increases.

A better way is the classic method of linear estimation, even if it is
now considered old-fashioned (with good reasons). In this method we take
all features \\( f=\[f_0\\dots f\_{N-1}\]^T \\) and take their linear
combination weights \\( w=\[w_0\\dots w\_{N-1}\]^T \\) , as

\\\[ \\hat y = f^T w. \\\]

The objective is to find weights such that the estimate \\( \\hat y \\)
is approximately equal to the desired output \\( y\\approx\\hat y. \\)
By collecting the features of a large amount of speech samples in a
matrix \\( F=\[f(t) \\dots f(t+T)\] \\) , the output is \\( \\hat y =
F^T w \\) and we can minimize the squared estimation error

\\\[ \\\| y -\\hat y\\\|^2 = \\\|y- F^T w\\\|^2. \\\]

To find the optimum, we set the derivative to zero

\\\[ 0=\\frac{\\partial}{\\partial w}\\\|y- F^T w\\\|^2 = F(y-F^Tw) =
Fy-FF^T w. \\\]

Clearly the optimal weight vector is then

\\\[ w^\* = (FF^T)^{-1} Fy = F^\\dagger y. \\\]

Here the superscript \\( \\dagger \\) denotes the pseudo-inverse.

  

Once we have found the optimal weights, for an individual frame we then
have

\\\[ \\hat y = f(t)^T w^\*, \\\]

and we can apply thresholding to get the VAD output as

\\\[ VAD(x) := \\begin{cases} 0, & f^Tw^\* \< \\theta\\\\ 1, & f^Tw^\*
\\geq \\theta. \\end{cases} \\\]

The figure on the right illustrates a linear classifier with this
approach using the 8 first autocorrelation values as well as their delta
and delta-delta values as features. The figure illustrates the desired,
raw as well as the thresholded output. Compared to energy thresholding
implemented above, the result seems much better. In the
false-positives/false-negatives plot, we see a comparison of the two
methods, energy thresholding and linear classifier. Both error-types are
reduced by an order of magnitude using the improved method.

It is important to note, however, that voice activity detection in
silence is a very easy task. The good results we obtained here are
therefore not unexpected. Speech distorted by background noises is much
more difficult for VAD algorithms.

The problems with this approach include that it hiddenly assumes that
the distribution of the input features for speech and non-speech signals
are linearly separable. That is, it cannot take into account any
non-linear shapes of the distribution, nor can it take into account the
fact that speech signals are represented by a multitude of sub-classes
such as voiced and unvoiced samples.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

<img src="attachments/151500905/155463830.png" class="image-center"
data-image-src="attachments/151500905/155463830.png"
data-unresolved-comment-count="0" data-linked-resource-id="155463830"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="vad_linear.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="151500905"
data-linked-resource-container-version="27" width="640" />

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Modern approach - Machine learning

Executive summary: Use machine learning for voice activity detection
tasks.

The basic design principle is:

1.  Choose a selection of the features described above.
2.  Choose the design of your machine learning method.
3.  Train the parameters over a large database of speech, which is
    representative of your intended application.

Unfortunately, the scientific methods for feature-selection and choosing
designs of machine learning methods have not yet matured. It is however
important to remember that voice activity detection is intended to be a
low-complexity method which saves resources. We can therefore accept
using a smaller number of parameters and a simpler design, even if that
sacrifices quality to some extent.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Post-processing

In general, speech onsets (when an utterance begins) are relatively easy
to detect, whereas it is difficult to determine where an utterance ends,
especially when speech trails off slowly. Another typical error in voice
activity detectors (VAD) are isolated errors, where one or small number
of consecutive frames are incorrectly labelled. And even if onsets are
generally easily detected, sometimes the VAD activates a bit too slowly,
such that the first frame of the speech segment is incorrectly
classified as non-speech.

Such errors can be easily corrected with heuristic methods such as
hangover, where we define a modified output as

\\\[ VAD'(x) = \\max\\left(VAD(k-K)..VAD(k)\\right). \\\]

In other words, if any of the last *K* frames was speech, then also this
frame is speech. If future frames are available, we can even extend this
to the future by defining

\\\[ VAD'(x) = \\max\\left(VAD(k-K)..VAD(k+H)\\right). \\\]

Such hangover -type functionalities can reduce false negatives with a
substantial amount. A similar approach can be implemented to remove very
short segments labelled as speech, since very short speech utterances
are both non-informative, but also cannot realistically be speech
sounds.

The figure on the right illustrates post-processing applied on the
output of the linear model implemented above. In this case, we first
remove isolated peaks with \\( VAD'(x) =
\\min\\left(VAD(k-1)..VAD(k+1)\\right) \\) and then apply a hangout with
a two-samples backward and one-sample lookahead as \\( VAD''(x) =
\\max\\left(VAD'(k-2)..VAD'(k+1)\\right). \\) In this simple case, we
get then a perfect output.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

<img src="attachments/151500905/155463844.png" class="image-center"
data-image-src="attachments/151500905/155463844.png"
data-unresolved-comment-count="0" data-linked-resource-id="155463844"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="vad_postproc.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="151500905"
data-linked-resource-container-version="27" width="640" />

</div>

</div>

</div>

</div>

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[vad.pdf](attachments/151500905/155463331.pdf) (application/pdf)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[vad.png](attachments/151500905/155463332.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[sound_example.wav](attachments/151500905/155463338.wav) (audio/x-wav)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[vad_tptn.png](attachments/151500905/155463474.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[vad_tptn.png](attachments/151500905/155463476.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[vad_tptn.png](attachments/151500905/155463472.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[vad_linear.png](attachments/151500905/155463830.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[vad_postproc.png](attachments/151500905/155463844.png) (image/png)  

</div>
