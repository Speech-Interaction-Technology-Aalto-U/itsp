# Zero-crossing rate

By looking at different speech and audio waveforms, we can see that
depending on the content, they vary a lot in their smoothness. For
example, voiced speech sounds are more smooth than unvoiced ones.
Smoothness is thus a informative characteristic of the signal.

A very simple way for measuring smoothness of a signal is to calculate
the number of zero-crossing within a segment of that signal. A voice
signal oscillates slowly - for example, a 100 Hz signal will cross zero
100 per second - whereas an unvoiced fricative can have 3000 zero
crossing per second.

To calculate of the zero-crossing rate of a signal you need to compare
the sign of each pair of consecutive samples. In other words, for a
length $N$ signal you need $O(N)$ operations. Such calculations are also
extremely simple to implement, which makes the zero-crossing rate an
attractive measure for low-complexity applications. However, there are
also many drawbacks with the zero-crossing rate:

-   The number of zero-crossings in a segment is an integer number. A
    continuous-valued measure would allow more detailed analysis.
-   Measure is applicable only on longer segments of the signal, since
    short segments might not have any or just a few zero crossings.
-   To make the measure consistent, we must assume that the signal is
    zero-mean. You should therefore subtract the mean of each segment
    before calculating the zero-crossings rate.

An alternative to the zero-crossing rate is to calculate the
[autocorrelation](Autocorrelation_and_autocovariance) at lag-1. It can
be estimated also from short segments, it is continuous-valued and
arithmetic complexity is also $O(N)$.

  

