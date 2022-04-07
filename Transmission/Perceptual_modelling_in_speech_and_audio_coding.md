# Perceptual modelling in speech and audio coding

<div class="contentLayout2">

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

Humans are usually the intended recipients of speech signals in
telecommunication, such that the quality of a transmission should be
measured in terms of how good a human listener would judge its quality.
*Perceptual models* refer to methods which try to approximate or predict
the judgement of auditory quality perceived by human listeners. In
coding applications we can thus define perceptual models as *evaluation
models*, with which we approximate the perceptual effect of distortions.

An another type of models which are frequently used in speech coding are
*source models*, which describe the inherent characteristics of the
source, which is the speech signal. You can think of a source model as
for example 1) physical models, which describe the physiological
processes which cause speech sounds or 2) the probability distribution
of speech signals. The important distinction is that source models do
not care about who is observing, but they only describe the objective
reality. In contrast, perceptual models are applied when *we
subjectively observe* the signal, to evaluate properties of the signal.

In speech and audio coding applications, practically all distortions
caused by the algorithms are due to quantization of the signal. The
objective of perceptual modelling is then to choose the quantization
accuracy such that the perceptually degrading effect of quantization is
minimized. Roughly speaking, this means that those signal components
which are more important to a human listener are quantized with a higher
accuracy than those which are less important.

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

## Frequency masking

If we play two sinusoid with slightly different frequencies, then the
louder of the two can *mask* the second sinusoid such that it becomes
inaudible. This effect is known as *frequency masking*. In other words,
people are less sensitive to sounds which are near in frequency to other
sounds. In particular, when quantizing a signal, we can use a lower
quantization accuracy in frequency-regions which have more energy. The
effect is reduced the further away we are in frequency.

In practice, frequency masking models are similar to spectral (energy)
envelopes. That is, the shape of the frequency masking model is similar
to the spectral envelope, but a smoothed and less pronounced version
thereof. More accurate versions of the model can be generated based on
[psychoacoustic](https://en.wikipedia.org/wiki/Psychoacoustics) theory.

Frequency masking models are used in two ways:

-   In frequency-domain codecs, where a frequency-domain representation
    of the signal is quantized, we choose the quantization accuracy in
    different regions of the spectrum based on a perceptual model.
    Typically high-energy regions are quantized with less accuracy than
    low-energy regions.
-   In time-domain codecs such as CELP, we typically use a
    analysis-by-synthesis loop, where different quantized versions are
    synthesized and the error between original and quantized signal is
    determined with perceptual weighting. The weighting is here based on
    a frequency masking model. Out of the different possible
    quantizations, the one with the smallest perceptually weighted error
    is chosen.

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

## Frequency scale

The sensitivity of human hearing depends on the frequency range where
the sound is present. We are more sensitive in the "low" regions and
less sensitive at "high" frequencies. There is however some ambiguity in
how sensitivity is defined, and we have two prominent different
interpretations:

-   In the cochlea of the human ear, sounds are processed in spectral
    bands, which are independent such that sounds in separate bands do
    not interfere with each other, but sounds within the same band *do
    interfere* with the perception of each other. This is known as
    auditory masking. The width of these bands is frequency dependent
    and increases with increasing frequency. This aspect of perception
    has been approximated with several models, including the
    [Bark](https://en.wikipedia.org/wiki/Bark_scale) and
    [ERB](https://en.wikipedia.org/wiki/Equivalent_rectangular_bandwidth)
    scales.
-   The distance between pitches are perceived differently depending on
    their frequencies. In short, a perceptually small step in pitch
    (measured in frequencies) is much larger at higher frequencies than
    at low frequencies. This aspect of perception can be approximated
    with the [Mel scale](https://en.wikipedia.org/wiki/Mel_scale).

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

## Temporal masking

The variation in accuracy and sensitivity of perception is interesting
also across time. In particular, a loud sound can make imperceptible a
second, weaker sound which comes later in time. Say, if we have two
impulses, consecutive in time, and such that the second one is weaker,
and their distance in time is sufficiently short, then we cannot hear
the second impulse. Surprisingly, such temporal masking can occur also
the other way around, a *later* loud sound can mask a preceding weaker
sound.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

</div>
