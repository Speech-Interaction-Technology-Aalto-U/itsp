# Objective quality evaluation

## Objective estimators for perceptual quality

With "objective evaluation" we usually refer to *estimators of
perceptual quality*, where the objective is to predict the mean output
of a [subjective listening](Subjective_quality_evaluation) test using an
algorithm. That is, we want a computer to listen to a sound sample and
try to "guess" what a human listener would say about its quality (on
average).

It is then clear that [*subjective
evaluation*](Subjective_quality_evaluation) is always the "true" measure
of performance and objective evaluation is an approximation thereof. In
this sense, subjective evaluation is "better". However, there are many
good reasons to use objective instead of subjective evaluation:

-   *Subjective evaluation is expensive*; a test requires that a large
    number of persons listens to sound samples, which is both
    time-consuming and requires infrastructure. Objective evaluation is
    performed on a computer, such that you can generally test a large
    number of sound samples in a short time.
-   *Subjective evaluation is noisy*; even with a large number of expert
    listeners it is generally difficult to get exactly the same result
    in two consecutive tests. Objective evaluation always gives the same
    rating for the same input, such that testing is consistent and
    reliable. This is especially important for scientific
    reproducibility; an independent laboratory can verify and confirm
    your results, the objective measure always gives the same output.
    With subjective evaluation, independent researchers can get
    different results, and you can never be 100% certain where the
    difference in results comes from. Did one of the researchers do an
    error or is it just that subjective listeners give always slightly
    different results?

Some of the most frequently used objective measures include:

-   [PESQ](https://en.wikipedia.org/wiki/PESQ) is probably the most
    frequently used objective evaluation method and it is defined in
    [ITU-T Recommendation P.862: Perceptual evaluation of speech quality
    (PESQ): An objective method for end-to-end speech quality assessment
    of narrow-band telephone networks and speech
    codecs](https://www.itu.int/rec/T-REC-P.862/en) (2001). It is thus
    an evaluation method designed explicitly for telecommunications
    applications. It estimates the mean score of an P.800 ACR test.  
    PESQ accepts only narrow-band input and is *not directly applicable*
    on other bandwidths. The degradation types whose effect PESQ can
    reliably predict are  
    -   Speech input levels to a codec

    -   Transmission channel errors

    -   Packet loss and packet loss concealment with CELP codecs

    -   Bit rates if a codec has more than one bit-rate mode

    -   Transcodings

    -   Environmental noise at the sending side

    -   Effect of varying delay in listening only tests

    -   Short-term time warping of audio signal

    -   Long-term time warping of audio signal

    Observe that distortions other than those listed above can provide
    unreliable results. An important missing feature are distortions
    caused by spectral processing, such as musical noise. Specifically,
    for example, using PESQ to evaluate [speech
    enhancement](Speech_enhancement) methods based on processing in the
    [STFT](Spectrogram_and_the_STFT) domain, *can give unreliable
    results*.
-   Perceptual Objective Listening Quality Assessment
    ([POLQA](https://en.wikipedia.org/wiki/POLQA "POLQA")) is the
    successor of PESQ and defined in [ITU-T Recommendation P.863:
    Perceptual objective listening quality
    assessment](http://www.itu.int/rec/T-REC-P.863/en). It is important
    to notice that for most practical purposes, POLQA is better than
    PESQ. It has a wider range of applications and acceptable
    degradation types and the output is more reliable. However, from a
    scientific perspective it is extremely regrettable that
    implementations of POLQA are commercial and *expensive* products,
    rendering application of POLQA infeasible in normal scientific work.
    Even if an individual team could afford purchasing a POLQA licence,
    verification of POLQA results by independent research labs is
    possible only if they also purchase a POLQA licence. Despite of its
    limitations, PESQ has therefore remained the scientific standard in
    objective evaluation of speech.
-   Perceptual Evaluation of Audio Quality
    ([PEAQ](https://en.wikipedia.org/wiki/PEAQ "PEAQ")) evaluates,
    instead of only speech, also other types of audio samples. It is
    therefore less accurate with respect to distortions specific to
    speech signals, but it generalizes better to other audio such as
    music and background noises. The measure is defined in
    <a href="http://www.itu.int/rec/R-REC-BS.1387/en" rel="nofollow">ITU-R
    Recommendation BS.1387</a>: Method for objective measurements of
    perceived audio quality (PEAQ).
-   The [short-term objective intelligibility
    (STOI)](https://ieeexplore.ieee.org/document/5713237) measure
    focuses on how *intelligible* a speech sample is. It is thus clearly
    focused on lower-quality scenarios where speech is so badly
    corrupted that it is hard to understand what is said. Like all
    objective measures, it is not a completely reliable estimate of
    quality, but can be useful in combination with other measures. A
    good feature of STOI is that an [implementation is
    available](http://amtoolbox.sourceforge.net/amt-0.9.5/doc/speech/taal2011_code.php).


## Other objective performance criteria

There are many cases where other performance criteria are well-warranted
than merely prediction of subjective listening test results. Most
typically these criteria are applied when there is no user involved,
such as speech recognition, or, when we want to have more detailed
characterization of performance than given by predictors of subjective
listening test results.

Some examples of such performance criteria include:

-   *[Word error rate
    (WER)](https://en.wikipedia.org/wiki/Word_error_rate)* is used in
    speech recognition to measure the proportion of words correctly
    recognized from a test signal.
-   *[Signal to noise ratio
    (SNR)](https://en.wikipedia.org/wiki/Signal-to-noise_ratio)* is used
    to measure the proportion of the desirable speech signal and
    undesirable noise components (which includes for example background
    noises, distortions caused by processing algorithms and
    transmission, as well as undesirable competing speakers). With a clean input spectrum $X_k$ and its distorted counterpart $\hat X_k$, the SNR is defined as
    $$
    D_{SNR} = \frac{ \sum_{k=0}^{N-1} |X_k|^2 }{ \sum_{k=0}^{N-1} |X_k - \hat X_k|^2 }.
    $$
    Typically, SNR is presented in units of decibel, obtained by $10\log_{10} D_{SNR}$. The motivation of the SNR is that it reflects the proportion of energy which is distorted. By using a ratio, we thus normalize the error to reflect *accuracy*, rather than error energy.
-   *Perceptual signal to noise ratio (pSNR)* measures SNR in a
    perceptually motivated domain. Essentially distortions are weighted
    such that they approximately correspond to human perception. This is
    similar to the above predictors of subjective listening tests, but
    works also on small segments of speech. It can be used to for
    detailed analysis of distortions to, for example, which parts of the
    signal contain undesirable distortions.
-   *The speech distortion index (SDI)* measures the amount by which a
    desirable speech signal is distorted. In [speech
    enhancement](Speech_enhancement), it is often used in combination
    with the *noise attenuation factor* (NAF), which measures the amount
    by which undesirable noises are removed. It is clear that by doing
    nothing, we obtain a perfect SDI and by setting the output to zero,
    we obtain a perfect NAF. Neither outcome is usually satisfactory. It
    is therefore usually not clear what the right balance between the
    two measures are.
-   Unweighted and weighted average recall (UAR, WAR) are often used to
    measure performance in speech classification tasks, such as
    classifying a speech segment into one of finite number of possible
    emotions. UAR is defined as the mean of class-specific recalls (the
    proportion of class samples recognized correctly) while WAR is the
    overall proportion of samples recognized correctly across all
    classes (sometimes also referred to as *accuracy*). UAR is often
    preferred over WAR in experiments where there is a notable class
    imbalance in the test data, and where it is important to have
    systems that are also sensitive to the less-frequent classes. 
-   [Receiver operating characteristic (ROC)
    curves](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
    and its derivatives such as [area under the curve
    (AUC)](https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve)
    or equal error rate (EER) are often used to report performance of
    systems that have some type of detection threshold that can be
    varied, and when performance for each threshold value is measured in
    terms of [precision and
    recall](https://en.wikipedia.org/wiki/Precision_and_recall). For
    instance, performance of speaker verification systems is often
    evaluated using such metrics. 
    
- The [log-spectral distance](https://en.wikipedia.org/wiki/Log-spectral_distance) or log-spectral distortion (LSD) measures spectral error of the log-magnitude spectrum $10\log_{10} P(\omega)$, where $P(\omega)=|X(\omega)|^2$ is the power (energy) of the clean signal spectrum $X(\omega)$. The LSD is then defined using the corrupted spectrum $\hat P(\omega)$ as
$$
D_{LS}
=\sqrt {{\frac {1}{2\pi }}\int _{-\pi }^{\pi }\left[10\log _{10}{\frac {P(\omega )}{{\hat {P}}(\omega )}}\right]^{2}\,d\omega } =\sqrt {{\frac {1}{2\pi }}\int _{-\pi }^{\pi }\left[10\log _{10} {P(\omega )}-10\log _{10}{\hat {P}}(\omega )\right]^{2}\,d\omega }.
$$
In practical applications the integral needs to be replaced with a summation such as 
$$
D_{LS}
=\sqrt {{\frac {1}{N }}\sum _{k=0}^{N-1 }\left[10\log _{10}{\frac {P_k}{{\hat {P}}_k}}\right]^{2} }, $$
where $N$ is the number of spectral components. Observe that the LSD thus corresponds to the mean of the squared error in the log-domain. The LSD is motivated by the fact that human perception of distortion is approximately logarithmic.
  