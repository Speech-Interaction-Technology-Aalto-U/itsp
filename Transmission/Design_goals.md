# Design goals


In short, the aim of speech coding methods is primarily to enable
natural and efficient spoken communication over a geographical distance,
given constraints on available resources. In other words, we want to be
able to talk with a distant person with the aid of technology. Usually
distance refers to location, but speech coding can be (and is often)
used for storing speech signals (such that distance refers to distance
in *time*). {cite:p}`backstrom2017speech`

In particular, aspects of quality which can be included in our design
goals are for example:

-   *Acoustic quality* in the sense that the reproduced acoustical
    signal should be similar to the original signal (measured for
    example in terms of signal to noise ratio or a perceptually weighted
    variant thereof).
-   *Perceptual transparency* refers to a property of high-accuracy
    coding systems, where a human listener cannot perceive a difference
    between the original and reconstructed signals. When discussing
    transparency, we however need to accurately define the methodology
    with which we measure transparency. Namely, if we compare small
    segments of an original and reconstructed signals, we can easily
    hear minute differences, which would never be perceived in a
    realistic use-case.
-   *Intelligibility* such that a listener can interpret the linguistic
    meaning of the reproduced signal.
-   *Delay* in the communication path, end-to-end, should be within
    reasonable limits (e.g. below 150 ms). A higher delay can impede the
    naturalness of a dialogue.
-   *Noisiness* caused by low-accuracy quantization and background
    noises should be minimized.
-   *Distortions* refers to the amount the speech signal is perceived
    to be changed by the processing.
-   *Naturalness* of the speech signal refers to how natural vs.
    non-natural a speech signal sounds. For example, some types of
    non-natural speech signals could be such which sound robotic,
    metallic or muffled.
-   *Listening effort* refers to the effort a listener needs to use a
    telecommunications system, and it should be minimized. Effort can be
    both due to properties of the user-interface, but importantly also,
    the listener might have to exert effort to understand a distorted
    speech signal.
-   *Annoyance* is closely related to listening effort, in that a signal
    which is intelligible can have so severe distortions, noisiness or
    transmission delays that it is really annoying. Usually annoyance
    thus also increases listening effort.
-   *Perception of distance* is the feeling that the participant has
    of the distance between participants. The main contributor to the
    perception of distance is probably room acoustics, such that if the
    distance between speaker and microphone is large, then the listener
    feels distant to the speaker. It affects for example the intimacy of
    a discussion, such that it is hard to feel intimate if the distance
    is large.

It is clear that different types of quality are prominent at different
levels of coding-accuracy, which in turn is a function of available
bitrate (bandwidth). As a rough characterization, with classic signal processing (non-neural) codecs, the quality-issues we optimize at different bitrates are:

-   At extremely low bitrates (below 1 kbit/s), classic codecs cannot hope to encode speech at high quality. At best, we can hope to retain *intelligibility* sufficient only for military applications.
-   At very low bitrates (1-2 kbit/s), intelligibility can usually be preserved, but speech signals can still be distorted and noisy, such that we want to minimize *listening effort*.
-   At low rates (3-8 kbit/s), we often have to balance between avoiding noisiness, distortions, annoyance and naturalness. In other words, we can often reduce noisiness by making the signal more muffled, but that would reduce naturalness. It is then very much a question of individual taste to choose which balance of distortions is best.
-   At medium rates (8-16 kbit/s), speech signals can already be coded with a high quality such that we can try to minimize the number of audible (perceivable) distortions. At these rates telecommunication systems can often, in practice, be transparent in the sense that users are not actively aware of any distortions, even if they would clearly notice distortions in a comparison with the original signal.
-   At high rates (above 16 kbit/s), it should in general be possible to encode speech signals at a perceptual transparent level. However, if computational resources are limited and in applications which require extremely low delay, distortions can still be audible.

With neural speech codecs, the quality trade-offs are somewhat different {cite:p}`zeghidour2021soundstream,defossez2022encodec,kumar2023dac`:
- Even at very low bitrates, 0.5-2 kbit/s, the sound quality can be relatively good such that the output sounds like the same speaker as the input. However, *intelligibility* can be compromised, especially in the presence of background noises. The issue is that, because quantization happens at a higher abstraction level, the errors caused are also on a higher abstraction level. So rather than a distorted sound, we may have distorted phonemes. 
- At a bitrate around 6 kbit/s, the sound quality can be expected to reach toll-quality, that is, usable in everyday applications without particular restrictions. 

Performance of a codec is however always a compromise between quality and resources. By increasing the amount of computational resources (or bandwidth) we can improve quality ad infinitum. The most important
limited resources are

-   Bandwidth, that is, the bit-rate at which we can transmit data. It
    is limited by 
    -   physical constraints such as available radio channels,
    -   power consumption (battery, ecology and price) and
    -   infrastructure capacity (investment, complexity, power).
-   CPU, that is, the amount of operations per second that can be
    performed, which is further limited by
    -   investment cost and
    -   power consumption (battery, ecology and price).
-   Memory, that is, the amount of RAM and ROM which is needed for the
    system, which are limited by
    -   investment cost and
    -   power consumption (battery, ecology and price).

Furthermore, the use-case of the intended speech (and audio) codec has
many important effects on the overall design. For example, the systems
configuration can be one of the following:

-   *One-to-one*; the classic telephony conversation, where two phones
    transmit speech between them. 
-   *One-to-many*; could be applicable for example in a setting like a
    radio-broadcast or in a storage application, where we encode once
    and have potentially multiple receivers/decoders. Since there are
    many receivers, we would then prefer that decoding the signal does
    not require much resources. In practice that means that the sender
    side (encoder) can use proportionally more resources.
-   *Many-to-many*; the typical teleconferencing application, often
    implemented with a cloud-server, such that merging of individual
    speakers can be done centrally, such that bandwidth to the many
    receivers can be saved.
-   *Many-to-one*; could be a distributed sensor-array scenario, where
    multiple devices in a room jointly record speech. Since we then have
    many encoders, they should be very simple and a majority of the
    intelligence and computational resources should be at the receiver
    end.

The overall design is also influenced by the type of transmission link.
In particular, the first few generations of digital mobile phones
operated with
[circuit-switched](https://en.wikipedia.org/wiki/Circuit_switching)
networks, where a fixed amount of bandwidth is allocated to every
connection. Newer networks are however based on
[packet-switched](https://en.wikipedia.org/wiki/Packet_switching)
designs, where data is transmitted essentially over the internet and
capacity and routing is optimized on the fly. Packet-switched networks
can in practice be much better optimized for overall cost and
performance. However, a packet-switched network cannot guarantee a
steady flow of packets, such that the receiver has to tolerate both
delayed or missing packets as well as packets which arrive in the wrong
order. Clearly this has an impact on both overall transmission delay of
the system, as well as increases the computational complexity of the
receiver. The costs are however usually balanced by the savings gained
in network optimization.

A further important related aspect are assumptions about lost packets in
general. In many storage and broadcast applications we can assume that
packets are not lost and that all data is available at the receiver. It
however much more common that we must assume that some packets are lost.
Among the most important consequences of lost packets for the design is
that in decoding the signal, we cannot assume that we have access to
previous packets. Specifically, if decoding of the current packet
depends on the previous packet, then a single lost packet would make us
unable to decode any of the following packets. Clearly such sensitivity
to lost packets is unacceptable in most real-world transmission systems.
However, we could encode speech with much higher efficiency, if we were
allowed to use previous packets to predict the current packet. The
likelihood of lost packets thus dictates the compromise between
sensitivity to lost packets and coding (compression) efficiency.

Observe that the usefulness of very low rates, below roughly 5-7 kbit/s, is narrower than the 7-32 kbit/s range. The bottleneck is caused by the *fixed* overheads in the transmission layer, where every packet carries regardless of its payload size: a typical RTP/UDP/IP header stack adds around 40 bytes per packet for IPv4 (RTP 12 bytes + UDP 8 bytes + IP 20 bytes), before any link-layer framing is even added. With 20 ms steps between windows, we have 50 windows per second; if each packet carries only one window, a codec running at 5.9 kbit/s contributes only around 15 bytes of payload per packet - so roughly 70% of every packet is header, not speech data. Lowering the codec bitrate further barely reduces the bandwidth actually used, since the packet is already dominated by fixed overhead, and the marginal benefit of further compression all but disappears.

The only way to recover further bandwidth savings below this point is to amortize the header cost over several frames per packet, by increasing the delay between transmissions - the same delay-versus-efficiency tradeoff as above, just applied at the low-bitrate end rather than at the packet-size limit. This pattern appears in other low-rate speech RTP formats too: [RFC 3558](https://www.rfc-editor.org/rfc/rfc3558) (EVRC/SMV) and [RFC 4788](https://www.rfc-editor.org/rfc/rfc4788), for instance, define bundled or interleaved packet formats specifically to amortize the RTP header over more than one speech frame.

Rates below roughly 5-6 kbit/s are thus not very useful in everyday, low-delay use cases without such frame bundling, but remain relevant in special applications that can tolerate the extra delay or where bandwidth is severely constrained, such as military and satellite communication, as well as storage. Another potential application is cases where some other information is transmitted in the same packets, such as multi-channel audio or multimedia. The sanity can however again be contested, as the single-channel quality might not be sufficiently high to warrant multi-channel audio, and transmission of video requires several orders of magnitude larger capacity anyway, so greedy optimization of speech compression brings only very marginal benefit in the total budget.


## References
```{bibliography}
:filter: docname in docnames
```