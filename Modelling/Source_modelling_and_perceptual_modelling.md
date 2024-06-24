# Source modelling and perceptual modelling

Speech processing applications use predominantly two types of modelling,
models related to perception and to the source. They are always separate
models on a meta-level, where we describe the motivations why we use
them. In practical applications, they however have often complicated
interactions, such that it becomes difficult to separate them.

-   *Source models* characterize the objective properties of a signal. A
    source model can for example describe the statistical distribution
    of speech signals and their characteristics. One such model would be
    a model of the [fundamental frequency](content:f0);
    voiced signals have a fundamental frequency and we can specify the
    range where fundamental frequencies of speech signals can lie. Other
    obvious characteristics of speech signals we can model include the
    intensity of speech and how it can change over time, as well as the
    spectral envelope, what shapes are possible and how they can change
    over time.
-   *Perceptual models* characterize *what* human listeners *can hear*
    and *how* much they appreciate different qualities. Perceptual
    models thus try to predict how humans evaluate quality. To construct
    perceptual models we need to ask human listeners questions like "Can
    you hear distortions in this signal?" or "How much is this signal
    distorted?". Based on the responses of human listeners, we can then
    make an analysis algorithm, which predicts the answer based on an
    analysis of the input signal.

In other words, source models explain objectively "*what the world is
like*", where as perceptual models are evaluation models estimate
subjective preference, "*how good the world is*".

It is not however always so clear which model is active in which
situation. For example, consider a speech recognizer, to which we feed
speech with a loud background noise. We must decide whether the speech
recognizer would evaluate speech as a human would evaluate, or whether
we want to recognize speech as best we can. It is potentially possible
that the speech recognizer could tolerate noise better than humans, such
that it recognizes speech also when a human would fail. The model is
then objectively evaluating speech content. However, if we want for
example that a humanoid robot behaves like a human, then it should not
understand speech in situations where a human would not.

As another example, consider a noise attenuation task, where our
objective is to restore the original speech from a corrupted sample. We
can then remove noise and only evaluate objectively how close we are to
the original. This is an unambiguous objetive task, where perception
plays no role. More similar to the original is better. However, an
alternative approach is to consider all possible sounds $y$, and given a
noisy observation $v$, compute the likelihood of all possible inputs.
Suppose then that our output is $x$, we can then compute the perceptual
distortion between all possible inputs $d(x,y)$, and assign weighting to
them according to their likelihoods $P(y|v)$. Finally, we can
minimize the expected distortion $\min E[d(x,y) | P(y|v)].$ We thus
take into account all possible true inputs, calculate the perceptual
distortion between the true inputs and the output, and weight them
according to how likely they are. Now, for the same task as before, we
have a perceptual criterion with which we can choose the best output.
Clearly the latter is more complicated, but it is also better motivated,
so we have to choose which one we want to use. The first one is based on
source modelling only (model of speech and noise), while the latter is a
combination of source (likelihood of different speech signals, given a
noisy observation) and perceptual modelling (perceptual distortion
measure).
