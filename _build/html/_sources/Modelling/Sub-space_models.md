# Sub-space models


In many cases, we can assume that signals are low-dimensional in the
sense that a high-dimensional observation  $ y\in{\mathbb
R}^{N\times 1} $ can be completely explained by a low-dimensional
representation  $ x\in{\mathbb R}^{M\times 1} $ such that with a
matrix  $ A\in{\mathbb R}^{N\times M} $ we have $ y = Ax $
with $N\>M$. This signal thus spans only a $M$-dimensional *sub-space*
of the whole $N$-dimensional space.


## Application with known sub-space

This representation comes in handy for example if we assume that we have
only a noisy observation of $y$. The desired signal lies in a sub-space,
so all the other dimensions have only noise in them and we can remove
them. We thus only need a mapping from the whole space to the sub-space.
It turns out that such a mapping is a projection to the sub-space
spanned by matrix $A$. In fact, the minimum mean square error (see
[Linear regression](Linear_regression)) solution is exactly the
[Moore-Penrose
pseudo-inverse](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse).
However, the downside with this approach is that here the matrix A needs
to be known in advance such that the pseudo-inverse can be formed.



## Estimation of unknown sub-space

In practical cases it is rather unusual that we would have access to the
matrix $A$, but instead, it must be estimated from available data. A
typical approach is based on a [singular value decomposition
(SVD)](https://en.wikipedia.org/wiki/Singular_value_decomposition) or
the [eigenvalue
decomposition](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix).
In short, we first estimate the covariance matrix of the signal and then
decompose it into uncorrelated components with the singular value
decomposition. Often, a small set of singular values make up most of the
energy of the whole signal. Thus if we discard the smallest singular
values, we do not loose much of the energy, but have a signal of a much
lower dimensionality. The singular value decomposition thus takes the
role of the sub-space mapping matrix $A$, and we can apply the model as
described above.



## Discussion

Sub-space models are theoretically appealing models, since their
analysis is straightforward. In terms of speech signals, the difficulty
lies in finding a representation which is actually low-rank. In other
words, it is not immediately clear in which domain we can apply analysis
such that speech signals can efficiently modelled by low-rank models. 

