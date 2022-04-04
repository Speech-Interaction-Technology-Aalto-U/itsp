# Entropy coding

<div class="contentLayout2">

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

In transmission and storage of data, it is useful if we can minimize the
number of bits needed to uniquely represent the input. With *entropy
coding*, we refer to methods which use statistical methods to compress
data. The target is *lossless* encoding, where the original data can be
perfectly reconstructed from the compressed representation. With *lossy*
coding, similarly, we refer to compression where, for example, we have a
limited number of bits to use and we try to reproduce a signal as
similar as possible to the original, but not necessarily exactly the
same. In speech and audio, coding usually refers to lossy coding. The
objective is to compress the coded signal such that it remains
perceptually indistinguishable from the original or such that the
perceptual effect of quantization is minimized. Such coding is known as
*[perceptual coding](Perceptual_modelling_in_speech_and_audio_coding)*.
Often, perceptual coding is performed in two steps; 1) quantization of
the signal such that the perceptually degrading effect of quantization
is minimized and 2) lossless coding of the quantized signal. In this
sense, even if lossless and lossy coding are clearly different methods,
a lossless coding module is often included also in lossy codecs.

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

Entropy coding operates on an abstract level such that it can operate on
any set of symbols as long as we have information about the
probabilities of each symbol. For example, consider a integer-valued
scalar *x*, which can attain values -1, 0, and +1, with respecitve
probabilities 0.25, 0.5, 0.25. That is, if we repeatedly draw scalars
*x* from this distribution, then on average, 25% of them are -1's. It is
then irrelevant what the numerical values of *x* are, we can
equivalently name the distinct elements according to symbols of the
alphabet as *a, b* and *c.  
*The table on the right demonstrates a possible encoding of these
numbers. Clearly we need more than one bit to encode three symbols, and
hence this encoding uses 2 bits per symbol. Observe, however, that the
bit-string 11 is not used, which means that the encoding is inefficient.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

A naive encoding of a set of numbers, with 2 bits per symbol.

<div class="table-wrap">

|        |        |            |        |
|--------|--------|------------|--------|
| number | symbol | bit-string | length |
| -1     | a      | 00         | 2      |
|  0     | b      | 01         | 2      |
| +1     | c      | 10         | 2      |

</div>

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Vector coding

To take better use of all bits, we can instead of single symbols,
consider a vector of symbols \\( x_1,x_2,x_3 \\) . With 3 possible
symbols for each element, we have 3<sup>3</sup>=27 possible
combinations. To encode it we thus need \\(
{\\mathrm{ceil}}(\\log_2(27))=5 \\) bits, or 1.66 bits per sample. In
comparison to the original 2 bits per sample above, this is a clear
improvement. However, we still have 5 unused bit-strings, which shows
that this encoding is sub-optimal.

Note that there are immediate parallels with *[vector quantization
(VQ)](Vector_quantization_VQ_)* though the two methods are not the same.
In short, vector quantization is lossy coding, which finds the best
quantization with a given set of symbols, whereas vector coding is
lossless coding of vectors of symbols.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

A naive encoding of a set of numbers, with 2 bits per symbol.

<div class="table-wrap">

|            |         |            |        |
|------------|---------|------------|--------|
| numbers    | symbols | bit-string | length |
| -1, -1, -1 | aaa     | 00000      | 5      |
| -1, -1, 0  | aab     | 00001      | 5      |
| -1, -1, +1 | aac     | 00010      | 5      |
| -1, 0 -1   | aba     | 00011      | 5      |
| -1, 0, 0   | abb     | 00100      | 5      |
| ...        | ...     | ...        | ...    |
| +1, +1, +1 | ccc     | 11011      | 5      |

</div>

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Variable length and Huffman coding

A central concept in entropy coding *variable length* coding, where
symbols can be encoded with bit-strings of varying lengths. In our above
example, an optimal coding (i.e. optimal bit-strings) is listed in the
table on the right.

The average number of bits per symbol is then the sum of the length of
each bit-string multiplied with the corresponding probability, that is,

\\\[ E\[bits/symbol\] = \\sum\_{k\\in\\{a,b,c\\}}P_k L_k = 0.25\\times
2 + 0.5\\times 1 + 0.25\\times 2 = 1.5. \\\]

From the bit-strings 00, 01 and 1, we can clearly decode the original
symbols; if the first bit is one, then the symbol is *b*, otherwise the
second bit determines whether the symbol is *a* or *c.*

Such variable length codes can be readily constructed when the
probabilities are negative powers of 2. This is a classic approach known
as [*Huffman* coding](https://en.wikipedia.org/wiki/Huffman_coding). It
is very simple to implement, which makes it an attractive choice when
probabilities are negative powers of 2. However, when the probabilities
of the symbols are arbitrary, then Huffman coding is no longer
applicable without approximations of probabilities, which make the
coding suboptimal.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

An illustrative encoding of a set of numbers, with 1.5 bits per symbol.

<div class="table-wrap">

|        |        |                             |            |                        |
|--------|--------|-----------------------------|------------|------------------------|
| number | symbol | probability *P<sub>k</sub>* | bit-string | length *L<sub>k</sub>* |
| -1     | a      | 0.25                        | 00         | 2                      |
|  0     | b      | 0.5                         | 1          | 1                      |
| +1     | c      | 0.25                        | 01         | 2                      |

</div>

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Arithmetic coding

To further improve on coding efficiency, we can combine vector coding
with Huffman coding in a method known as [*arithmetic
coding*](https://en.wikipedia.org/wiki/Arithmetic_coding). It uses the
probability of symbols to jointly encode a sequence symbols. For
example, consider the set of symbols 0....5 on the right with
corresponding occurrence probabilities *P<sub>k</sub>*. Further suppose
that we are supposed to encode the string "130". The first step is to
assign every symbol to a unique segment  \\( \[s_k,\\,s\_{k+1}\] \\) of
the interval \\( \[0,\\,1\] \\) such that the width of the segment
matches the probability of the symbol \\( P_k = s\_{k+1}-s_k \\) .

The first symbol is "1" whereby we are assigned to the interval 0.40 ...
0.67, which we will call the current interval. The central idea of
arithmetic coding is that next symbol is encoded inside the current
interval. That is, we shift and scale the *s<sub>k</sub>*'s such that
they perfectly fit within the current interval 0.40 ... 0.67. In
mathematical terms, if the current symbol is *h*, then the current
interval is *s<sub>h</sub> ... s<sub>h+1</sub>*, and the intervals of
the next symbol are shifted and scaled as

\\\[ s'\_k = s_h + s_k(s\_{h+1}-s_h) = s_h + s_kP_k. \\\]

The second symbol was "3", such that the current interval is 0.6133 ...
0.6349. For the third symbol, the intervals are then shifted and scaled
as

\\\[ s''\_k = s'\_3 + s'\_k(s_4-s_3) = 0.6133 + s'\_k\\times 0.08\\times
0.27. \\\]

The new intervals are listed on the right. The third symbol is "0" such
that the last current interval is 0.6133 ... 0.6219, which we will
denote as \\( s\_{left} ... s\_{right} \\) .

The remaining step is to translate the last interval into a string of
bits. Let us divide the whole interval 0 ... 1 into *2<sup>B</sup>*
quantization levels on a uniform grid. such that the *k*th level is \\(
k 2^{-B}. \\) We then find the largest *B* such that there is a *k* with
which *k2<sup>-B</sup>* is inside the last current segment \\( s\_{left}
... s\_{right} \\) that is, \\( s\_{left} \\leq k2^{-B} \\leq s\_{right}
\\) . Then *k* is the index to our quantization position, that is, it
uniquely describes the interval and thus uniquely describes the sequence
of symbols "130". Specifically, with *B=7*, we find that *k=79*,
fulfills the criteria

\\\[ s\_{left}=0.6133 \\leq k2^{-B} = 0.6172 \\leq s\_{right} = 0.6219.
\\\]

Decoding the sequence is then straightforward at the decoder.

A few additional points:

-   The average bit-rate is \\( -\\sum_k P_k \\log_2 P_k \\approx 2.2
    \\) bits per sample. In the example above we needed B=7 bits to
    encode 3 samples, which gives 2.3 bits per sample. The actual number
    of bits thus does not perfectly coincide with the average bit-rate.

-   In [a practical
    implementation](Implementation_of_an_Arithmetic_Coder) of a decoder,
    we need to either know the number of symbols or bits, transmit the
    number of symbols or bits separately, or we need to use a special
    symbol which signifies end-of-string.

-   Usually the last current segment does not exactly align with
    *k2<sup>-B</sup>* , which means that there are small unused spaces
    in between the bitstring and the last current segment. This is an
    inherent inefficiency of arithmetic coding. Heuristically it is easy
    to understand that we must send an integer number of bits, but the
    data might not be exactly an integer number of bits. The loss is
    always less than 1 bit for the whole string, which is acceptable
    when we send a large amount of symbols in a string.

-   Direct [implementation](Implementation_of_an_Arithmetic_Coder) of
    the above description would be cumbersome since the intervals
    rapidly become smaller than what can be expressed by discrete
    arithmetic (fixed or floating point). Usually therefore algorithms
    are designed to use an intermediate interval, from which we output
    bits once they become known. For example, in the above example,
    after the first symbol we already know that the interval is above
    0.5, such that the first bit has to be 1, corresponding to the
    interval 0.5 ... 0.1.

-   The specific [implementation](Implementation_of_an_Arithmetic_Coder)
    is rather involved and sensitive to errors.

-   Algorithmic complexity of an arithmetic coder is usually reasonable,
    provided that the probabilities *P<sub>k</sub>* are readily
    available. If the probabilities need to be calculated online
    (parametric probability model), then complexity increases
    considerably.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

Illustrative set of symbols and their corresponding probabilities.

<div class="table-wrap">

<table class="relative-table wrapped confluenceTable"
style="margin-left: auto;margin-right: auto;width: 48.6654%;">
<colgroup>
<col style="width: 17%" />
<col style="width: 22%" />
<col style="width: 29%" />
<col style="width: 31%" />
</colgroup>
<tbody>
<tr class="header">
<th class="confluenceTh"><p>symbol<br />
<em>k</em></p></th>
<th class="confluenceTh">probability <em>P<sub>k</sub></em></th>
<th class="confluenceTh"><p>interval<br />
<em>s<sub>k</sub> ... s<sub>k+1</sub></em></p></th>
<th class="confluenceTh">bits per symbol
<em>log<sub>2</sub>(P<sub>k</sub>)</em></th>
</tr>

<tr class="odd">
<td class="confluenceTd">0</td>
<td class="confluenceTd">0.40</td>
<td class="confluenceTd">0.00 ... 0.40</td>
<td class="confluenceTd">1.32</td>
</tr>
<tr class="even">
<td class="confluenceTd">1</td>
<td class="confluenceTd">0.27</td>
<td class="confluenceTd">0.40 ... 0.67</td>
<td class="confluenceTd">1.89</td>
</tr>
<tr class="odd">
<td class="confluenceTd">2</td>
<td class="confluenceTd">0.12</td>
<td class="confluenceTd">0.67 ... 0.79</td>
<td class="confluenceTd">3.05</td>
</tr>
<tr class="even">
<td class="confluenceTd">3</td>
<td class="confluenceTd">0.08</td>
<td class="confluenceTd">0.79 ... 0.87</td>
<td class="confluenceTd">3.64</td>
</tr>
<tr class="odd">
<td class="confluenceTd">4</td>
<td class="confluenceTd">0.07</td>
<td class="confluenceTd">0.87 ... 0.94</td>
<td class="confluenceTd">3.84</td>
</tr>
<tr class="even">
<td class="confluenceTd">5</td>
<td class="confluenceTd">0.06</td>
<td class="confluenceTd">0.94 ... 1.00</td>
<td class="confluenceTd">4.06</td>
</tr>
</tbody>
</table>

</div>

  

The intervals of the second symbol.

<div class="table-wrap">

<table class="relative-table wrapped confluenceTable"
style="margin-left: auto;margin-right: auto;width: 46.954%;">
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<tbody>
<tr class="header">
<th class="confluenceTh"><p>symbol<br />
<em>k</em></p></th>
<th class="confluenceTh"><p>interval<br />
<em>s<sub>k</sub>' ... s<sub>k+1</sub>'</em></p></th>
</tr>

<tr class="odd">
<td class="confluenceTd">0</td>
<td class="confluenceTd">0.4000 ... 0.5080</td>
</tr>
<tr class="even">
<td class="confluenceTd">1</td>
<td class="confluenceTd">0.5080 ... 0.5809</td>
</tr>
<tr class="odd">
<td class="confluenceTd">2</td>
<td class="confluenceTd">0.5809 ... 0.6133</td>
</tr>
<tr class="even">
<td class="confluenceTd">3</td>
<td class="confluenceTd">0.6133 ... 0.6349</td>
</tr>
<tr class="odd">
<td class="confluenceTd">4</td>
<td class="confluenceTd">0.6349 ... 0.6538</td>
</tr>
<tr class="even">
<td class="confluenceTd">5</td>
<td class="confluenceTd">0.6538 ... 0.6700</td>
</tr>
</tbody>
</table>

</div>

  

The intervals of the third symbol.

<div class="table-wrap">

<table class="relative-table wrapped confluenceTable"
style="margin-left: auto;margin-right: auto;width: 46.8317%;">
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<tbody>
<tr class="header">
<th class="confluenceTh"><p>symbol<br />
<em>k</em></p></th>
<th class="confluenceTh"><p>interval<br />
<em>s<sub>k</sub>'' ... s<sub>k+1</sub>''</em></p></th>
</tr>

<tr class="odd">
<td class="confluenceTd">0</td>
<td class="confluenceTd">0.6133 ... 0.6219</td>
</tr>
<tr class="even">
<td class="confluenceTd">1</td>
<td class="confluenceTd">0.6219 ... 0.6278</td>
</tr>
<tr class="odd">
<td class="confluenceTd">2</td>
<td class="confluenceTd">0.6278 ... 0.6304</td>
</tr>
<tr class="even">
<td class="confluenceTd">3</td>
<td class="confluenceTd">0.6404 ... 0.6321</td>
</tr>
<tr class="odd">
<td class="confluenceTd">4</td>
<td class="confluenceTd">0.6321 ... 0.6336</td>
</tr>
<tr class="even">
<td class="confluenceTd">5</td>
<td class="confluenceTd">0.6336 ... 0.6439</td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Parametric coding

In the examples above, we used a table to list the probabilities of each
symbol. That leads to a rigid system, which cannot adapt to changes in
the signal. If we want to, for example, use a perceptual model to choose
the quantization accuracy of different samples, we need the ability to
adapt quantization bin widths and consequently, to adapt the
probabilities of each quantization bin. A simple approach is to model
the probability distribution of the signal and calculate probabilities
of each symbol on-line. We thus use a parametric model of the
probability distribution and correspondingly, we call a coding with
parametric models a *parametric coding*.

In speech coding, parametric coding is typically used in
frequency-domain coding to encode individual spectral components. We can
then assume that spectral components follow a Laplacian distribution and
derive the probabilities *P<sub>k</sub>* using that distribution. More
refined alternatives include for example [Gaussian mixture models
(GMMs).](Gaussian_mixture_model_GMM_)

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

## Algebraic coding

Suppose we would like to encode a string like "00010000", where "0"s
happen with a high likelihood and there is only a single "1". We could
then use arithmetic and parametric coding to encode the probabilities of
0's and 1's to develop an output string. It quickly becomes awfully
complex, when it would be much simpler to just encode the position of
the single "1". In this case, if the first position is 0, then the
single "1" is at position 3. There are a total of 8 positions, such that
we need 3 bits to encode the position. Very simple.

This approach can be readily extended to encompass for example both +1
and -1's. Just encode the sign with a single extra bit. There exists
straightforward algorithms to include multiple non-zero elements as
well, as long as the number of non-zeros is small.

Such encoding algorithms are known as *algebraic coding*, where we use
an algebraic rule or explicit algorithms to encode strings. This is one
type of vector coding, since it encodes jointly a string of symbols.
Usually algebraic coding is fixed bitrate coding, since the number of
bits is decided in advance.

Algebraic coding works efficiently when there are a low number of
non-zeros and the number of quantization levels is very low.
Unfortunately these methods become increasingly complicated when higher
accuracy is required. Moreover, for higher accuracy quantization, it
becomes increasingly difficult to find the best quantization of a given
vector *x*. Still, due to its simplicity and efficiency at low bitrates,
algebraic coding is so popular in speech coding that the most commonly
used codec type is known as [Algebraic code-excited linear prediction
(ACELP)](Code-excited_linear_prediction_CELP_), since it uses algebraic
coding to encode the residual signal.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

</div>
