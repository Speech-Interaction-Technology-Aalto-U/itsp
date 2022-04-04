# Pre-emphasis

<div class="contentLayout2">

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

The figure on the right illustrates the average magnitude spectrum of a
speech signal. We observe that a majority of the energy is concentrated
in the lower end of the spectrum. In fact, as a linear approximation, we
see that in this particular example, the energy drops at a rate of 2.2
dB/kHz. The exact rate of decrease varies for each speaker and depending
on several factors. A safe and often used assumption is that energy
drops at roughly 2 dB/kHz.

This rapid reduction in energy leads to practical problems in
implementations. For example, if we would implement a discrete Fourier
transform with [fixed-point
arithmetic](https://en.wikipedia.org/wiki/Fixed-point_arithmetic), then
the accuracy would be very different in different parts of the spectrum.
Typically the spectrum at 6kHz is 15dB lower than at 0Hz. On a linear
scale 15dB corresponds to a factor of 6. In other words, on a 16-bit
CPU, if we use the full range of a signed 15-bit representation for the
lowest frequencies, than we use effectively only 12-bit range for
frequency components at 6kHz.

A common pre-processing tool used to compensate for the average spectral
shape is *pre-emphasis*, which emphasises higher frequencies. Typically,
pre-emphasis is applied as a time-domain FIR filter with one free
parameter, for example, in speech coding at a sampling rate of 8kHz or
12.8kHz, we use the pre-emphasis filter \\( P(z)=1-0.68 z^{-1} \\) . The
spectrum of this filter is illustrated on the right. After applying the
filter, the spectrum is more flat and we can apply fixed-point
arithmetic with a lower accuracy and thus better optimize CPU
consumption.

There are numerous different ways of tuning pre-emphasis. Firstly,
though the average spectrum is decaying, unvoiced fricatives have
typically *more* energy at the high frequencies. Excessive pre-emphasis
would therefore cause problems for fricatives. Pre-emphasis also has an
effect on both perceptual and statistical modelling as well as
estimation of linear predictive models. The best amount of pre-emphasis
is therefore very much dependent on the application and implementation
details.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

<img src="attachments/149888451/149888832.png"
data-image-src="attachments/149888451/149888832.png"
data-unresolved-comment-count="0" data-linked-resource-id="149888832"
data-linked-resource-version="3" data-linked-resource-type="attachment"
data-linked-resource-default-alias="speech_avg_db.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="149888451"
data-linked-resource-container-version="5" height="250" /><img src="attachments/149888451/149888831.png"
data-image-src="attachments/149888451/149888831.png"
data-unresolved-comment-count="0" data-linked-resource-id="149888831"
data-linked-resource-version="3" data-linked-resource-type="attachment"
data-linked-resource-default-alias="pre_emph_db.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="149888451"
data-linked-resource-container-version="5" height="250" />

</div>

</div>

</div>

</div>

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[pre_emph_db.png](attachments/149888451/149888850.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[speech_avg_db.png](attachments/149888451/149889047.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[pre_emph_db.png](attachments/149888451/149888851.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[pre_emph_db.png](attachments/149888451/149888831.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[speech_avg_db.png](attachments/149888451/149889050.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[speech_avg_db.png](attachments/149888451/149888832.png) (image/png)  

</div>
