# Implementation of an Arithmetic Coder

<div class="contentLayout2">

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Numerical accuracy

The basic idea of an arithmetic coder is not particularly difficult to
comprehend and this can give the deceptive expectation that also
implementation would be easy. It is not easy. The crux of error-free
implementation is that arithmetic coding is based on a recursive
algorithm, which in principle requires infinite numerical accuracy,
which is obviously impossible. Implementation on a practical devices
requires that all intermediate operations are performed with
fixed-accuracy operations.

To further complicate the issue, it is paramount that the coder works
*exactly* the same at both the encoder and decoder. Since we are working
with "infinite accuracy", any small deviation, a single incorrect bit
somewhere, would corrupt the whole remaining bitstream. Different CPUs
have often different accuracy in their floating-point operations and
low-cost CPUs often do not even feature floating-point operations, such
that floating-point computations are usually not applicable. The
remaining choice is [fixed-point
arithmetic](https://en.wikipedia.org/wiki/Fixed-point_arithmetic), where
we use integer operations only, such that the decimal comma is at a
pre-determined location.

Many modern CPUs feature 64-bit integer operations, but we usually need
to implement algorithms such that they work also on low-cost CPUs and
therefore choose to use 32-bit operations only. However, since the
output of a multiplication of two N-bit values will have 2N bits, the
range of input values must be 16 bits on a 32-bit CPU. To allow for
signed integers, we reduce that to 15 bits. In some rare cases,
behaviour in overflow situations or rounding of the least significant
bit will differ across CPUs, such that we need to avoid also those and
reduce the effective length of representations to 14 bits. In other
words, all input values to an arithmetic coder must remain in the
interval 0 to (2^14)-1 = 16383. As we shall see, there will be some
further restrictions down the line, put on the difference between
adjacent values.

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

## Encoder

Recall that arithmetic coding is based on range-coding, where the
likelihood of a symbol corresponds to the width of the corresponding
range. A particular symbol is thus encoded by any number which falls
into the range assigned to that symbol. For example, if we have three
symbols, *a, b* and *c*, with likelihoods 0.22, 0.55 and 0.23, then we
can choose that all number in the range 0 to 0.22 correspond to symbol
*a*, all numbers in 0.22 to 0.77 to *b* and 0.77 to 1.0 to *c*. Notice
that the width of each range thus corresponds to the corresponding
likelihood.

These ranges must however be represented as fixed-point values. Since
all numbers are within the interval 0 to 1.0, we can map these numbers
to integer values in the range 0 to 16384 (note that 16384 has in fact
15 bits, but since it signifies a border value, this does not cause
problems). The three ranges are thus rounded to 0 to 3604, 3604 to
12616, and 12616 to 16384.

If we would start by encoding a symbol *a*, then the remaining range is
0 to 3604. If we would continue encoding within that range, then the
numerical accuracy would be much smaller than 14 bits (effectively only
log2(3604)=11 bits). The first key idea here is to scale up the
numerical range by encoding bits which are already known. If the range 0
to 16384 is split into two, such that the two ranges are \\( 0 \\leq x
\< 8192 \\) and \\( 8192 \\leq x \< 16384 \\) we can encode a first bit
with 0 and 1, respectively. Once we have encoded the first bit, we map
the interval back to 0 to 16384. That is, if first bit is 0, then we
remap \\( x:=2x \\) , otherwise \\( x:=2(x-8192) \\) . In our case, the
range 0 to 3604 is below 8192, we encode a 0 and the range is mapped to
0 to 7208. This is still below 8192, so we encode a second 0 and remap
again to get a range 0 to 14416. The numerical range is now less than
the full 14 bits, but it is the best we can do with a 14 bit
representation for a range which is not aligned with a power of 2.

Similarly, if we would want to encode a symbol *c*, we would have the
remaining range 12616 to 16384, encode a 1 and remap to 8838 to 16384,
encode a second 1 and remap to 1312 to 16384.

If we however encode a symbol *b*, the remaining range is 3604 to 12616,
where the lower limit is below 8192 and the upper limit is above 8192,
so we cannot encode a bit directly, but should continue to encoding the
next symbol.

We then need to remap the ranges of the three symbols, from 0, 3604,
12616, 16384 to the range 3604 to 12616. To map the borders
*b<sub>0</sub>*, to *b<sub>N</sub>*, to the range \\( \[r_0,\\,r_1\] \\)
we use the formula

\\\[ b_k' := r_0 + \\left\\lfloor \\frac{b_k (r_1-r_0)}{b_N-b_0}
\\right\\rceil \\\]

such that the new intervals are 3604, 5586, 10543, 12616 and where the
brackets \\( \\lfloor\\cdot\\rceil \\) signify rounding to nearest
integer. Observe that 16384 = 2^14, such that the division can be
replaced by a right-shift of 14 steps, for a large reduction in
computation time.

We can then proceed to encoding the second symbol:

-   If second symbol is *a*, then the new range is 3604 to 5586, we
    encode a 0, and remap to 7208 to 11172.
-   If second symbol is *b*, then the new range is 5585 to 10543.
-   If second symbol is *c*, then the new range is 10543 to 12616, we
    encode a 1, and remap to 4702 to 8848.

In all three cases, we cannot proceed further, since the remaining range
includes the mid-point 8192. However, in all three cases, the width of
the range is now rather small (respectively, 3964, 4957 and 4146), such
that if we remap the next symbols into that range, then their accuracy
would be significantly reduced. In fact, we can readily find examples
where the range diminishes so much that we do not have unique ranges for
all the symbols any more, such that the string of symbols cannot be
decoded any more.

We therefore need an additional option, in addition to encoding a 0 or
1, which allows extending the current range to maintain numerical
accuracy. A practical solution is to find a new category of "postponed
bits", where some bits are stored into a queue, whose value is
determined only later.

Specifically, let the current range be \\( \[r_0,\\,r_1\] \\) and the
upper limit of numerical range be *R*. If \\( r_0 \> R/4 \\) , and \\(
r_1 \< 3R/4 \\) , then we postpone one bit and remap the range as

\\\[ r_k':=2(r_k-N/4). \\\]

In essence, we discard the quarters at the left and right ends, and
extend the middle of the range to cover the whole available range.

All postponed bits get encoded when we next time get a bit to encode.
Specifically, if the number of postponed bits is p, and the next bit to
encode is 0, then we encode a 0 and p 1's. Similarly, if the next bit to
encode is a 0, then we encode a 1 and p 0's.

With these rules we can encode any string of symbols. However, as the
string of symbols comes to an end, the remaining range still contains
information which is not encoded to the bit stream. We thus have to
flush the range with the smallest of number bits. We achieve this as
follows. Suppose the remaining range is \\( \[r_0,\\,r_1\] \\) . By
necessity, the range must include the mid-point *R/2*, where *R* is the
upper limit of the numerical range. We would like to encode the shortest
bitstream which uniquely identifies this range. Out of the ranges \\(
\[r_0,\\,R\] \\) and \\( \[R,\\,r_1\] \\) , we therefore choose to
encode the range which is larger (=more likely);

-   If \\( R-r_0 \> r_1-R \\) , then we encode a 0 and the new current
    range is 0 to *2r<sub>0</sub>*.

-   If \\( R-r_0 \<= r_1-R \\) , then we encode a 1 and the new current
    range is *2(r<sub>1</sub>-R/2)* to 1.

We continue encoding bits iteratively with this rule until the current
range covers the whole interval 0 to *R*.

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

## Decoder

At the decoder we in principle revert the operations of the encoder.
However, as was demonstrated with flushing of the bitstream, which is
required as the last step of encoding, the current range includes
information about symbols which have not yet been written into the
bitstream. We therefore have to decode the bits corresponding to the
steps in the encoder, but also metaphorically, flush the bitstream for
every iteration, to decode the information left in the range. In
pseudo-code, the algorithm can be stated as

1.  As long as there are bits left  
    1.  Save current state of the bitstream
    2.  Decode as many bits as required to determine current symbol
    3.  Restore state of the bitstream
    4.  Repeat the range-remapping steps of the encoder and remove the
        corresponding number of bits from the bitstream

As an example, consider the same example as above, where the intervals
for *a,b* and *c* are 0, 3604, 12616, 16384 and the first symbol is *b*.
At the encoder, we did not encode any bits for *b* but the range was
updated to 3604 and 12616. At the decoder, the initial range is 0 to
16384 and we therefore have to decode several bits until we can
determine that the symbol is *b*. However, to make sure that we have
exactly the same coder state as at the encoder, we then restore the bits
to the bitstream, and proceed as we would not have decoded any bits when
decoding the second symbol from range 3604 to 12616.

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

</div>
