# Multi-channel speech enhancement and beamforming


Simple, single-channel [noise attenuation](Noise_attenuation) and
dereverberation is often not sufficient for acceptable quality,
especially in very noisy environments, such as in a car or on a busy
sidewalk. To reach better quality, we can then add more microphones. The
benefit of added microphones includes at least:

-   Time-of-arrival differences between sources enables the use of
    beamforming filters, which use such time (phase) differences to
    separate between sources.
-   Intensity level differences between sources; In for example a mobile
    phone, we can have forward and backward facing microphones such that
    the backward facing microphone is used primarily for estimating
    background noise, while the forward facing microphone records the
    desired speech signal. By using the background-noise estimate from
    the backward facing microphone, we can then use noise attenuation on
    the forward facing microphone to gain better quality.
-   Each microphone will feature some level of sensor-noise, that is,
    the hardware itself causes some inaccuracies to the signal.
    Sensor-noises are for most parts independent across microphones such
    that with each additional microphone we can better separate desired
    sources from noise.

The most-frequently discussed approach is to use microphone arrays,
typically in either a linear configuration, where microphones are
equi-spaced on a straight line, or in a circular configuration, where
microphones are equi-spaced on a circle. The benefits include that a
linear configuration makes analytical analysis easier, whereas a
circular array can have an almost uniform response in all directions.



## Delay-and-sum beamforming

As an introduction to beamforming consider a linear array of $K$
microphones with input signals $x_{k}(t)$, where $k$ and $t$ are
the microphone and time indices. We assume that the desired source is
sufficiently far away that we can approximate it with a plane wave. Then
the signal will arrive at the microphones at different times  $
\Delta t_{x_k} $ and we can calculate time [time difference of
arrival (TDOA)](tdoa.ipynb) of each microphone $ t_{x_k} = \Delta
t_{x_k}-\Delta t_{x_1} $ where we used microphone $k=1$ as a
reference point. The delayed signals thus have $ x_k(t) = x(t-\Delta
t_{x_k}) = x\left(t-\Delta t_{x_k}+\Delta t_{x_1} - \Delta
t_{x_1}\right) = x_1(t-t_{x_k}). $ Similarly, for the noise sources
we have $ y_k(t) = t_1(t-t_{y_k}). $  

If the desired and noise sources appear at different angles, then their
corresponding delays will be different. Moreover, if we add a
signal $z(t)$ with itself at a random offset δ, then the summation is
destructive, that is, smaller than the original $
\frac12\left\|z(t)+z(t+\delta)\right\| \leq \left\|z(t)\right\|
$ . Addition without an offset is obviously constructive, such that we
can form the *delay and sum estimate* as

$$ \hat x(t) = \frac 1K \sum_{k=1}^K x_k(t-t_{x_k}). $$

In this summation, all signals approaching from the same direction as
the desired source will be additive (constructive) and other directions
will be (more or less) destructive.

Trivial as it is, the delay-and-sum should however be treated as a
pedagogical example only. It does not ideally amplify the desired source
nor attenuate the noise source, and it is sensitive to errors in the
TDOAs.


![delayandsum.png](attachments/175509409.png)

