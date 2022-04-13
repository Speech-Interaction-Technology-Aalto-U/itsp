# Jitter and shimmer

The speech production system is not a rigid, mechanical machine, but
composed of an assortment of soft-tissue components. Therefore, although
parts of a speech signal might seem stationary, there are always small
fluctuations in it, as vocal fold oscillation is not exactly periodic.
Variations in signal frequency and amplitude are called jitter and
shimmer, respectively. Jitter and shimmer are acoustic characteristics
of voice signals, and they are caused by irregular vocal fold vibration.
They are perceived as roughness, breathiness, or hoarseness in a
speaker’s voice. All natural speech contains some level of jitter and
shimmer, but measuring them is a common way to detect voice pathologies.
Personal habits such as smoking or alcohol consumption might increase
the level of jitter and shimmer in voice. However, many other factors
can have an effect as well, such as loudness of voice, language, or
gender. As jitter and shimmer represent individual voice characteristics
that humans might use to recognize familiar voices, these measures could
even be useful for speaker recognition systems.

There are several different ways to measure jitter and shimmer. For
instance, when detecting voice disorders, they are measured as
percentages of the average period, where values above certain thresholds
are potentially related to pathological voices. Jitter and shimmer are
most clearly detected from long, sustained vowels.

A commonly used jitter value is the absolute jitter. This measure
expresses the average absolute difference between consecutive periods.

$$ Jitter(absolute) = \frac{1}{N-1}\sum_{i=1}^{N-1}\|T_i-T_{i+1}\|
$$

where Ti are the extracted F0 period lengths and N is the number of
extracted F0 periods.

When this is divided by the average period, another common measure,
relative jitter, is obtained.

$$ Jitter(relative) =
\frac{\frac{1}{N-1}\sum_{i=1}^{N-1}\|T_i-T_{i+1}\|}{\frac{1}{N}\sum_{i=1}^{N}T_i}
$$

where Ti are the extracted F0 period lengths and N is the number of
extracted F0 periods.

A commonly used shimmer value, here Shimmer(dB), expresses the average
absolute base-10 logarithm of the difference between the amplitudes of
consecutive periods multiplied by 20.

$$ Shimmer(dB) =
\frac{1}{N-1}\sum_{i=1}^{N-1}\|20\log(A_{i+1}/A_i)\| $$

where Ai are the extracted peak-to-peak amplitude data and N is the
number of extracted fundamental frequency periods.

Relative shimmer expresses the average absolute difference between the
amplitudes of consecutive periods divided by the average amplitude.

$$ Shimmer(relative) =
\frac{\frac{1}{N-1}\sum_{i=1}^{N-1}\|A_i-A_{i+1}\|}{\frac{1}{N}\sum_{i=1}^{N}A_i}
$$

where Ai are the extracted peak-to-peak amplitude data and N is the
number of extracted fundamental frequency periods.

  

  
