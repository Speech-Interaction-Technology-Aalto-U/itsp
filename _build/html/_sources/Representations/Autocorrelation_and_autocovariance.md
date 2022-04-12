# Autocorrelation and autocovariance

<div class="contentLayout2">

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

Look at the speech signal segment to the right. On a large scale it is
hard to discern a structure, but on a small scale, the signal seems
continuous. Speech signals typically have such structure that samples
near in time to each other are similar in amplitude. Such structure is
often called short-term temporal structure.

More specifically, samples of the signal are *correlated* with the
preceding and following samples. Such structures are in statistics
measured by covariance and correlation, defined for zero-mean variables
x and y as

\\\[ \\begin{split} \\text{covariance:} & \\sigma\_{xy} = E\[xy\] \\\\
\\text{correlation:} & \\rho\_{xy} =
\\frac{E\[xy\]}{\\sqrt{E\[x^2\]E\[y^2\]}}, \\end{split} \\\]

where *E\[ \]* is the expectation operator.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

Short segment of speech

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

For a speech signal *x<sub>n</sub>*, where *k* is the time-index, we
would like to measure the correlation between two
time-indices *x<sub>n</sub>* and *x<sub>h</sub>*. Since the structure
which we are interested in appears when *n* and *h* are near each other,
it is better to measure the correlation
between *x<sub>n</sub>* and *x<sub>n-k</sub>*. The scalar *k* is known
as the *lag*. Furthermore, we can assume that the correlation is uniform
over all *n* within the segment. The self-correlation and -covariances,
known as the *autocorrelation* and *autocovariance* are defined as

\\\[ \\begin{split} \\text{autocovariance:} & r\_{k} =
E_n\[x_nx\_{n-k}\] \\\\ \\text{autocorrelation:} & c\_{k} =
\\frac{E_n\[x_nx\_{n-k}\]}{E_n\[x_n^2\]} = \\frac{r_k}{r_0}.
\\end{split} \\\]

The figure on the right illustrates the autocovariance of the above
speech signal. We can immediately see that the short-time correlations
are preserved - on a small scale, the autocovariance looks similar to
the original speech signal. The oscillating structure is also accurately
preserved. 

Because we assume that the signal is stationary, and as a consequence of
the above formulations, we can readily see that autocovarinaces and
-correlations are symmetric

\\\[ r_k = E_n\[x_nx\_{n-k}\] = E_n\[x\_{n+k}x\_{n+k-k}\] =
E_n\[x\_{n+k}x\_{n}\] = r\_{-k}. \\\]

This symmetry is clearly visible in the figure to the right, where the
curve is mirrored around lag 0.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

The autocovariance of a speech segment

<img src="attachments/149884819/149884843.png"
data-image-src="attachments/149884819/149884843.png"
data-unresolved-comment-count="0" data-linked-resource-id="149884843"
data-linked-resource-version="3" data-linked-resource-type="attachment"
data-linked-resource-default-alias="speech_segment_autoc.png"
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

The above formulas use the expectation operator *E\[ \]* to define the
autocovariance and -correlation. It is an abstract tool, which needs to
be replaced by a proper estimator for practical implementations.
Specifically, to estimate the autocovariance from a segment of length
*N*, we use

\\\[ r_k \\approx \\frac1{N-1} \\sum\_{k=1}^{N-1} x_n x\_{n-k}. \\\]

Observe that the speech signal *x<sub>n</sub>* has to be
[windowed](Windowing) before using the above formula.

We can also make an on-line estimate of the autocovariance for sample
position *n* with lag *k* as

\\\[ \\hat r_k(n) := \\alpha x_n x\_{n-k} + (1-\\alpha) \\hat r_k(n-1),
\\\]

where α is a small positive constant which determines how rapidly the
estimate converges.

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

It is often easier to work with vector notation instead of scalars,
whereby we need the corresponding definitions for autocovariances.
Suppose

\\\[ x =
\\begin{bmatrix}x_0\\\\x_1\\\\\\vdots\\\\x\_{N-1}\\end{bmatrix}. \\\]

We can then define the autocovariance matrix as

\\\[ R_x := E\[x x^T\] = \\begin{bmatrix}E\[x_0^2\] & E\[x_0x_1\] &
\\dots & E\[x_0x\_{N-1}\]\\\\E\[x_1x_0\] & E\[x_1^2\] & \\dots &
E\[x_1x\_{N-1}\]\\\\\\vdots&\\vdots&\\ddots&\\vdots\\\\E\[x\_{N-1}x_0\]
& E\[x\_{N-1}x_1\] & \\dots & E\[x\_{N-1}^2\]\\end{bmatrix} =
\\begin{bmatrix}r_0 & r_1 & \\dots & r\_{N-1}\\\\ r_1 & r_0 & \\dots &
r\_{N-2}\\\\\\vdots&\\vdots&\\ddots&\\vdots\\\\r\_{N-1} & r\_{N-1} &
\\dots & r_0\\end{bmatrix}. \\\]

Clearly *R<sub>x</sub>* is thus a symmetric
[Toeplitz](https://en.wikipedia.org/wiki/Toeplitz_matrix) matrix.
Moreover, since it is a product of *x* with itself, *R<sub>x</sub>* is
also [positive
(semi-)definite](https://en.wikipedia.org/wiki/Definiteness_of_a_matrix).

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

</div>

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[speech_segment.png](attachments/149884819/149884849.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[speech_segment_autoc.png](attachments/149884819/149884850.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[speech_segment.png](attachments/149884819/149884861.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[speech_segment_autoc.png](attachments/149884819/149884883.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[speech_segment.png](attachments/149884819/149884842.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[speech_segment_autoc.png](attachments/149884819/149884843.png)
(image/png)  

</div>
