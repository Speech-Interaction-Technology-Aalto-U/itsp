(content:neuralvocoders)=
# Neural vocoders

The vocoder is the last block of a speech synthesiser. It converts acoustic features into a speech waveform. Classical vocoders are based on the source-filter model of speech production (see [Vocoder](#content:vocoder)). Neural vocoders learn the conversion from data. They were the first part of the synthesis pipeline where neural networks clearly beat classical methods, and they are now used in almost all synthesis systems. They are also used in other tasks that produce speech, such as [speech enhancement](#content:enhancement) and voice conversion.

## The vocoder problem

In most neural synthesis systems, the input of the vocoder is a mel spectrogram (see [Mel-cepstrum](#content:melcepstrum) and [Spectrogram and the STFT](#stft)). A typical setting has 80 mel bands and a new frame every 10 to 12 ms. The waveform has, for example, 22 050 or 24 000 samples per second. The vocoder must therefore create a few hundred samples from each frame of 80 numbers.

The mel spectrogram leaves out much of the information in the waveform:

- it contains only the magnitude of the spectrum, not the phase,
- the mel bands are wide at high frequencies, so the fine harmonic structure is smoothed out, and
- the frames are long compared to the samples, so fast events, such as the start of a plosive, are blurred.

Many different waveforms therefore have the same mel spectrogram. The vocoder must pick one of them that sounds natural. If it gets the phase or the fine structure wrong, the speech sounds metallic, buzzy or "phasey". In the terms of machine learning, a vocoder is therefore a *generative model*: it learns the probability distribution of waveforms, given the features, and generates a sample from it. The families of neural vocoders below differ in how they model this distribution.

## Classical starting points

Two classical methods are useful as baselines.

The **Griffin–Lim algorithm** {cite}`griffin1984signal` estimates the phase from the magnitude spectrum by iteration. It alternates between the time domain and the STFT domain, and in each round it keeps the phase but replaces the magnitude with the target. It needs no training, but the result typically sounds phasey and reverberant. See [Griffin–Lim](../Modelling/griffinlim.ipynb).

**Source-filter vocoders**, such as STRAIGHT {cite}`kawahara1999restructuring` and WORLD {cite}`morise2016world`, describe speech with a fundamental frequency (F0), a spectral envelope and a measure of how noisy each frequency band is. They are fast and give direct control over pitch, which is why they were used in [statistical parametric synthesis](#content:spss). However, their simple model of the voice source makes speech sound buzzy and muffled.

## Autoregressive vocoders

An autoregressive model generates the waveform one sample at a time. Each new sample is predicted from the previous samples and from the acoustic features $c$:

$$
p(x) = \prod_{n=1}^{N} p(x_n \mid x_1, \dots, x_{n-1}, c).
$$

**WaveNet** {cite}`oord2016wavenet` was the first neural vocoder with clearly better quality than classical vocoders. It quantises each sample to 256 levels with μ-law companding, as in telephone speech, and predicts a probability for each level. To see a long history of samples, it uses *dilated causal convolutions*, where each layer skips over more and more samples. With WaveNet, synthetic speech was for the first time rated close to recorded speech {cite}`shen2018natural`.

The problem of autoregressive models is speed. A network must be evaluated once for every sample, that is, tens of thousands of times for each second of speech, and the evaluations cannot run in parallel. The first WaveNet was far too slow for real-time use. Later models made the network much smaller:

- **WaveRNN** {cite}`kalchbrenner2018efficient` uses a single recurrent layer with sparse weights and runs in real time on a mobile phone.
- **LPCNet** {cite}`valin2019lpcnet` combines a neural network with [linear prediction](#content:linearprediction). Linear prediction computed from the spectral envelope predicts the next sample, so the network only needs to model the part that linear prediction cannot predict, the excitation. This is the source-filter idea again: the classical filter does the easy part, and the network does the hard part. LPCNet is small enough to run on a phone CPU, and it has also been used for very low bitrate speech coding.

## Parallel vocoders

To be fast on modern hardware, a vocoder should generate all samples at once. Three types of generative models make this possible.

:::{admonition} Background: three types of generative models
:class: tip

All three types learn to turn random noise into realistic samples, here waveforms, given the acoustic features.

- A **generative adversarial network (GAN)** has two networks. The *generator* produces waveforms. The *discriminator* tries to tell generated waveforms from real ones. The two are trained against each other, so the generator learns to produce waveforms that the discriminator cannot tell from real speech.
- A **normalising flow** is a network that can be inverted. It is trained to map real waveforms to Gaussian noise. To generate speech, we draw noise and run the network backwards.
- A **diffusion model** is trained to remove a small amount of noise from a noisy waveform. To generate speech, we start from pure noise and remove noise step by step. More steps give better quality but take more time.
:::

### GAN vocoders

**MelGAN** {cite}`kumar2019melgan` showed that a GAN can turn a mel spectrogram into a waveform with good quality and much faster than real time. **Parallel WaveGAN** {cite}`yamamoto2020parallel` added a loss that compares the STFT of the generated and real speech with several frame lengths, which made training more stable. **HiFi-GAN** {cite}`kong2020hifigan` added a discriminator that looks at the waveform in segments of different periods. Speech is made of periodic signals, and this discriminator helps the generator get the periodic structure right. HiFi-GAN reached quality close to recorded speech, more than 100 times faster than real time on a GPU, and a small version runs faster than real time on a CPU.

Later GAN vocoders improve generalisation and speed. **BigVGAN** {cite}`lee2023bigvgan` is a large model trained on many speakers, languages and recording conditions. It works for voices and conditions that were not in its training data, which is why it is called a *universal* vocoder. **Vocos** {cite}`siuzdak2024vocos` does not generate the waveform directly. Instead, it predicts the magnitude and phase of the STFT for each frame and uses the inverse STFT to produce the waveform. The STFT does the upsampling from frames to samples, so the network is much faster than vocoders that work in the time domain.

GAN vocoders are the most common choice in current systems. Their main drawback is that GAN training can be unstable. In practice, the adversarial loss is therefore combined with simpler losses, such as the distance between the mel spectrograms of the generated and real speech.

### Flow-based vocoders

**WaveGlow** {cite}`prenger2019waveglow` is a normalising flow. It generates the waveform in one pass and is trained by maximising the likelihood of the training data, which is simpler than GAN training. However, flows need large networks, and they have mostly been replaced by GAN vocoders.

### Diffusion vocoders

**WaveGrad** {cite}`chen2021wavegrad` and **DiffWave** {cite}`kong2021diffwave` start from noise and refine the waveform in a number of steps, each conditioned on the mel spectrogram. The number of steps gives a direct trade-off between speed and quality. Diffusion vocoders are rarely used alone today, but diffusion and the related *flow matching* are central in recent acoustic models (see [Large-scale and zero-shot synthesis](#content:zeroshotsynthesis)).

## Vocoders with a signal model

Some neural vocoders keep an explicit model of speech production inside the network.

**Neural source-filter (NSF)** models {cite}`wang2020neural` generate a source signal from the F0, as a sum of sine waves for voiced speech and noise for unvoiced speech. A neural network then shapes this source into speech. Because the F0 is an explicit input, the pitch of the output can be changed directly, which is hard with other neural vocoders.

**Differentiable digital signal processing (DDSP)** {cite}`engel2020ddsp` builds classical signal processing blocks, such as oscillators and filters, so that a neural network can be trained to control them. The model was first developed for musical instruments. Because much of the structure is built in, such models need little data and few parameters.

These models are easier to interpret and to control than purely neural vocoders. The price is that their assumptions about speech, such as a single periodic source, do not always hold, for example in breathy or creaky voice.

## Comparison

The table summarises the main families. The statements are rough and depend on the model size and the hardware.

| Family | Examples | Speed | Quality | Explicit pitch control |
|---|---|---|---|---|
| Phase reconstruction | Griffin–Lim | fast, iterative | low: phasey | no |
| Source-filter | STRAIGHT, WORLD | very fast | medium: buzzy | yes |
| Autoregressive | WaveNet, WaveRNN, LPCNet | slow: one sample at a time | high | no (LPCNet: partly) |
| GAN | MelGAN, HiFi-GAN, BigVGAN, Vocos | very fast | high | no |
| Normalising flow | WaveGlow | fast on a GPU, large model | high | no |
| Diffusion | WaveGrad, DiffWave | depends on the number of steps | high | no |
| Signal model | NSF, DDSP | fast | medium to high | yes |

## Sound examples

The examples below are *copy synthesis*: a recording is analysed into acoustic features, and a vocoder turns the features back into a waveform. Any difference from the original is caused by the features and the vocoder. Griffin–Lim and HiFi-GAN start from the same 80-band mel spectrogram, which only covers frequencies up to 8 kHz. HiFi-GAN fills in the higher frequencies, Griffin–Lim cannot. The HiFi-GAN and Vocos models were trained on other speakers. Click a link to listen. The models and licences are listed in [sounds/README.md](sounds/README.md).

| Signal | Listen |
|---|---|
| Original recording (VCTK speaker p334) | [original](sounds/vctk_p334_011_mic2.wav) |
| Griffin–Lim | [Griffin–Lim](sounds/vocoder_griffinlim.wav) |
| WORLD (source-filter vocoder) | [WORLD](sounds/vocoder_world.wav) |
| HiFi-GAN (GAN vocoder) | [HiFi-GAN](sounds/vocoder_hifigan.wav) |
| Vocos (GAN vocoder in the STFT domain) | [Vocos](sounds/vocoder_vocos.wav) |

## Practical issues

**Mismatch between training and use.** A vocoder is usually trained on mel spectrograms computed from real speech. In a synthesiser, it gets mel spectrograms predicted by the acoustic model, which are smoother and contain errors. This mismatch causes artefacts. A common solution is to fine-tune the vocoder on spectrograms predicted by the acoustic model. End-to-end models avoid the problem by training both parts together (see [Neural acoustic models](#content:neuralacousticmodels)).

**Generalisation.** Early neural vocoders were trained for one speaker. Universal vocoders work for many speakers, but quality still drops for voices, languages and recording conditions that are far from the training data, and for signals that are not speech, such as singing or music.

**Neural audio codecs.** A neural audio codec, such as SoundStream {cite}`zeghidour2021soundstream` or EnCodec {cite}`defossez2022encodec`, has an encoder that compresses speech into a sequence of discrete codes, and a decoder that turns the codes back into a waveform. The decoder is a vocoder whose input is codes instead of a mel spectrogram, and it is usually trained in the same way as a GAN vocoder. Codecs are used for [transmission](#content:telecom), and they are a central part of codec language models for speech synthesis (see [Large-scale and zero-shot synthesis](#content:zeroshotsynthesis)).

## References

```{bibliography}
:filter: docname in docnames
```
