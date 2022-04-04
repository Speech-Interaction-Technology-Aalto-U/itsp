# Linear prediction

<div class="contentLayout2">

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Definition

Speech is a continuous signal, which means that consecutive samples of
the signal are correlated (see figure on the right). In particular, if
we know a previous sample *x<sub>n-1</sub>*, we can make a *prediction*
of the current sample, \\( \\hat x_n = x\_{n-1}, \\) such that \\( \\hat
x_n \\approx x_n. \\) By using more previous samples we have more
information, which should help us make a better prediction.
Specifically, we can define a predictor which uses *M* previous samples
to predict the current sample *x<sub>n </sub>*as

\\\[ \\hat x_n = - \\sum\_{k=1}^M a_k x\_{n-k}. \\\]

This is a *linear predictor* because it takes a linearly weighted sum of
past components to predict the current one.

The error of the prediction, also known as the *prediction residual* is

\\\[ e_n = x_n - \\hat x_n = x_n + \\sum\_{k=1}^M a_k x\_{n-k} =
\\sum\_{k=0}^M a_k x\_{n-k}, \\\]

where *a<sub>0</sub>=1*. This explains why the definition \\( \\hat x_n
\\) included a minus sign; when we calculate the residual, the double
negative disappears and we can collate everything into one summation.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

A short segment of speech. Notice how consecutive samples are mostly
near each other, which means that consecutive samples are correlated.

<img src="attachments/149884819/149884842.png"
data-image-src="attachments/149884819/149884842.png"
data-unresolved-comment-count="0" data-linked-resource-id="149884842"
data-linked-resource-version="3" data-linked-resource-type="attachment"
data-linked-resource-default-alias="speech_segment.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="149884819"
data-linked-resource-container-version="8" height="250" />

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Vector notation

Using vector notation, we can make the expressions more compact

\\\[ e = Xa \\\]

where

\\\[ e =
\\begin{bmatrix}e_0\\\\e_1\\\\\\vdots\\\\e\_{N-1}\\end{bmatrix},\\qquad
X = \\begin{bmatrix}x_0 & x\_{-1} & \\dots & x\_{M} \\\\x_1 & x_0 &
\\dots & x\_{M-1} \\\\ \\vdots & \\vdots & & \\vdots \\\\ x\_{N-1} &
x\_{N-2} & \\dots & x\_{N-M} \\end{bmatrix}, \\qquad a =
\\begin{bmatrix}a_0\\\\a_1\\\\\\vdots\\\\a\_{M}\\end{bmatrix}. \\\]

Here we calculated the residual for a length *N* frame of the signal.

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

## Parameter estimation

Vector *a* holds the unknown coefficients of the predictor. To find the
best possible predictor, we can minimize the minimum mean-square error
(MMSE). The square error is the 2-norm of the residual, \\(
\\\|e\\\|^2=e^T e \\) . The mean of that error is defined as the
expectation

\\\[ E\\left\[\\\|e\\\|^2\\right\] = E\\left\[a^T X^T X a\\right\] = a^T
E\\left\[X^T X\\right\] a = a^T R_x a, \\\]

where \\( R_x = E\\left\[X^T X\\right\] \\) and \\(
E\\left\[\\cdot\\right\] \\) is the expectation operator. Note that, as
shown in the [autocorrelation
section](Autocorrelation_and_autocovariance), the matrix
*R<sub>x</sub>*, can be usually assumed to have a symmetric
[Toeplitz](https://en.wikipedia.org/wiki/Toeplitz_matrix) structure.

If we would directly minimize the mean-square error  \\(
E\\left\[\\\|e\\\|^2\\right\], \\) then clearly we would obtain the
trivial solution *a=0*, which is not particularly useful. However that
solution contradicts with the requirement that the first coefficient is
unity, *a<sub>0</sub>=1*. In vector notation we can equivalently write

\\\[ a_0-1=u^T a -1=0,
\\qquad\\text{where}\\,u=\\begin{bmatrix}1\\\\0\\\\0\\\\\\vdots\\\\0\\end{bmatrix}.
\\\]

The standard method for quadratic minimization with constraints is to
use a [Langrange
multiplier](https://en.wikipedia.org/wiki/Lagrange_multiplier), λ, such
that the objective function is

\\\[ \\eta(a,\\lambda) = a^T R_x a - 2\\lambda\\left(a^T u - 1\\right).
\\\]

This function can be heuristically interpreted such that λ is a free
parameter. Since our objective is to minimize \\( a^T R_x a \\) if   \\(
a^T u - 1 \\) is non-zero, then the objective function can become
arbitrarily large. To allow any value for λ, the constraint must
therefore be zero.

The objective function is then minimized by setting its derivative with
respect to *a* to zero

\\\[ 0 = \\frac\\partial{\\partial a}\\eta(a,\\lambda) =
\\frac\\partial{\\partial a} \\left\[a^T R_x a -2\\lambda\\left(a^T u -
1\\right)\\right\] = 2 R_x a - 2 \\lambda u. \\\]

It follows that the optimal predictor coefficients are found by solving

\\\[ R_x a = \\lambda u. \\\]

Since *R<sub>x</sub>*, is symmetric and
[Toeplitz](https://en.wikipedia.org/wiki/Toeplitz_matrix), the above
system of equations can be efficiently solved using the [Levinson-Durbin
algorithm](https://en.wikipedia.org/wiki/Levinson_recursion) with
algorithmic complexity *O(M<sup>2</sup>)*. However, note that with
direct solution we obtain \\( a':=\\frac1\\lambda a = R_x^{-1}u \\) that
is, instead of *a* we get *a* scaled with λ. However, since we know that
*a<sub>0</sub>=1*, we can find *a* by \\( a=\\lambda a' =
\\frac{a'}{a'\_0}. \\)

## Spectral properties

Linear prediction is usually used to predict the current sample of a
time-domain signal *x<sub>n</sub>*. The usefulness of linear prediction
however becomes evident by studying its Fourier spectrum Specifically,
since *e=Xa*, the corresponding Z-domain representation is

\\\[ E(z) = X(z)A(z)\\qquad\\Rightarrow\\qquad X(z)=\\frac{E(z)}{A(z)},
\\\]

where *E(z)*, *X(z)*, and *A(z)*, are the Z-transforms of
*e<sub>n</sub>*, *x<sub>n</sub>* and *a<sub>n</sub>*, respectively. The
residual *E(z)* is white-noise, whereby the inverse *A(z)<sup>-1</sup>*,
must follow the shape of *X(z)*.

In other words, the linear predictor models the macro-shape or
*envelope* of the spectrum.

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

## Physiological interpretation and model order

Linear prediction has a surprising connection with physical modelling of
[speech production](Speech_production_and_acoustic_properties). Namely,
a linear predictive model is equivalent with a *tube-model of the vocal
tract* (see figure on the right). A useful consequence is that from the
acoustic properties of such a tube-model, we can derive a relationship
between the physical length of the vocal tract *L* and the number of
parameters *M* of the corresponding linear predictor as

\\\[ M = \\frac{2f_sL}c, \\\]

where *f<sub>s</sub>* is the sampling frequency and *c* is the speed of
sound. With an air-temperature of 35 C, the speed of sound is
*c*=350m/s. The mean length of vocal tracts for females and males are
approximately 14.1 and 16.9 cm. We can then choose to
overestimate *L*=0.17m. At a sampling frequency of 16kHz, this gives 
\\( M\\approx 17 \\) . The linear predictor will catch also features of
the glottal oscillation and lip radiation, such that a useful
approximation is \\( M\\approx
{\\text{round}}\\left(1.25\\frac{f_s}{1000}\\right) \\) . For different
sampling rates we then get the number of parameters *M* as

  

<div class="table-wrap">

|                 |     |
|-----------------|-----|
| *f<sub>s</sub>* | M   |
| 8 kHz           | 10  |
| 12.8 kHz        | 16  |
| 16 kHz          | 20  |

</div>

  

Observe however that even if a tube-model is equivalent with a linear
predictor, the relationship is non-linear and highly sensitive to small
errors. Moreover, when estimating linear predictive models from speech,
in addition to features of the vocal tract, we will also capture
features of glottal oscillation and lip-radiation It is therefore very
difficult to estimate meaningful tube-model parameters from speech. A
related sub-field of speech analysis is [glottal inverse
filtering](Glottal_inverse_filtering), which attempts to estimate the
glottal source from the acoustic signal. A necessary step in such
inverse filtering is to estimate the acoustic effect of the vocal tract,
that is, it is necessary to estimate the tube model.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

A tube model of the vocal tract consisting of constant-radius
tube-segments

<img src="attachments/148294391/149889201.png"
data-image-src="attachments/148294391/149889201.png"
data-unresolved-comment-count="0" data-linked-resource-id="149889201"
data-linked-resource-version="2" data-linked-resource-type="attachment"
data-linked-resource-default-alias="tubemodel.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="148294391"
data-linked-resource-container-version="25" height="250" />

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Uses in speech coding

Linear prediction has been highly influential especially in early speech
coders. In fact, the dominant speech coding method is [code-excited
linear prediction (CELP)](Code-excited_linear_prediction_CELP_), which
is based on linear prediction.

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

## Alternative representations (advanced topic)

Suppose scalars *a<sub>m,k</sub>*, are the coefficients of an *M*th
order linear predictor. Coefficients of consecutive orders *M* and *M+1*
are then related as

\\\[ a\_{M+1,k} = a\_{M,k} + \\gamma\_{M+1} a\_{M,M+1-k}, \\\]

where the real valued scalar \\( \\gamma\_{M}\\in(-1,+1) \\) is the
*M*th [reflection
coefficient](https://en.wikipedia.org/wiki/Reflection_coefficient). This
formulation is the basis for the [Levinson-Durbin
algorithm](https://en.wikipedia.org/wiki/Levinson_recursion) which can
be used to solve the linear predictive coefficients. In a physical
sense, reflection coefficients describe the amount of the acoustic wave
which is reflected back in each junction of the tube-model. In other
words, there is a relationship between the *cross-sectional areas*
*S<sub>k</sub>* of each tube-segment and the reflection coefficients as

\\\[ \\gamma_k = \\frac{S_k - S\_{k+1}}{S_k + S\_{k+1}}. \\\]

Furthermore, the logarithmic ratio of cross-sectional areas, also known
as the [*log-area
ratios*](https://en.wikipedia.org/wiki/Log_area_ratio), are defined as

\\\[ A_k = \\log\\frac{S_k}{S\_{k+1}} =
\\log\\frac{1-\\gamma_k}{1+\\gamma_k}. \\\]

This form has been used in coding of linear predictive models, but is
today mostly of historical interest.

  

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

</div>
