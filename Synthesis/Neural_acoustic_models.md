(content:neuralacousticmodels)=
# Neural acoustic models

The acoustic model is the part of a synthesiser that converts text into acoustic features. Its input is a sequence of phonemes or characters from [text analysis](#content:synthesis), and its output is usually a mel spectrogram, which a [neural vocoder](#content:neuralvocoders) then converts into a waveform. This page describes the neural acoustic models that replaced statistical parametric synthesis between about 2017 and 2021. They are still widely used, because they are small and fast and need only a few hours of training data.

Every acoustic model must solve two problems:

- **Alignment.** The input has a few phonemes per second, but the output has around 100 frames per second. The model must decide how long each phoneme lasts, that is, which frames belong to which phoneme.
- **One-to-many mapping.** The same text can be spoken in many correct ways, with different rhythm, intonation and emphasis. A model trained to predict the most likely output tends to produce the *average* of these, which sounds flat and monotonous. This is often called *over-smoothing*.

The models below differ mostly in how they solve these two problems.

## From hidden Markov models to neural networks

The first neural acoustic models simply replaced the statistical model in [statistical parametric synthesis](#content:spss). A deep neural network predicted vocoder features from linguistic features, frame by frame, instead of a hidden Markov model with decision trees {cite}`zen2013statistical`. Better network designs {cite}`wu2015deep` and recurrent networks, which can model how features change over time, improved the result further. These systems still needed phoneme durations from a separate model and a classical vocoder. They were better than HMM-based systems, but the big change came when neural networks learned the whole mapping from text to spectrogram.

## Sequence-to-sequence models with attention

:::{admonition} Background: encoders, decoders and attention
:class: tip

A *sequence-to-sequence* model converts one sequence into another of a different length, for example text in one language into text in another. An *encoder* network reads the input sequence and produces a sequence of hidden vectors, one per input symbol. A *decoder* network then produces the output one step at a time. At each step, an *attention* mechanism computes a weight for each encoder vector, which tells the decoder which part of the input to use. The weights are learned from data, so the model finds the alignment between input and output by itself.

A *transformer* {cite}`vaswani2017attention` builds both the encoder and the decoder from attention alone. *Self-attention* lets each element of a sequence look at all other elements of the same sequence. Unlike a recurrent network, a transformer can process all elements of a sequence in parallel during training, which makes it much faster to train on large amounts of data.
:::

**Tacotron** {cite}`wang2017tacotron` was the first widely successful model that learned to map characters directly to a spectrogram, without a separate text analysis or duration model. Its decoder generates the spectrogram frame by frame, and attention decides which characters to read at each step. **Tacotron 2** {cite}`shen2018natural` predicted a mel spectrogram and used a WaveNet vocoder. In listening tests, it got a mean opinion score of 4.53, close to the 4.58 of the recordings. **Transformer TTS** {cite}`li2019neural` replaced the recurrent networks with a transformer, which made training faster.

These models are *autoregressive*: each frame is predicted from the previous ones, and the model also predicts when to stop. This makes them slow, because frames are generated one after another. A bigger problem is that the learned attention can fail. When it does, the model skips or repeats words, mumbles, or never stops. Such errors are rare for ordinary sentences, but they are common for long or unusual input, and they are hard to detect and fix.

## Non-autoregressive models with explicit durations

**FastSpeech** {cite}`ren2019fastspeech` solves the alignment problem with an explicit duration model, as in classical parametric synthesis. A duration predictor estimates the number of frames for each phoneme. A *length regulator* then repeats the encoder vector of each phoneme that many times ({numref}`fig:length_regulator`). After this, the input and output have the same length, and the decoder can generate all frames in parallel. This made generation of the mel spectrogram 270 times faster than with an autoregressive model. It also removed almost all skipped and repeated words. As a bonus, the speaking rate can be changed by scaling the durations.

```{figure} attachments/length_regulator.svg
:name: fig:length_regulator

The length regulator of FastSpeech. Each phoneme is repeated as many times as its predicted duration, measured in frames, so that the decoder gets one input vector for each output frame.
```

FastSpeech learned its durations from the attention of an autoregressive teacher model. **FastSpeech 2** {cite}`ren2021fastspeech` takes them instead from a forced aligner, a speech recogniser that finds the time boundaries of known phonemes {cite}`mcauliffe2017montreal`. More importantly, FastSpeech 2 also predicts the pitch and energy of each frame. During training, the model gets the true pitch, energy and durations measured from the recording. This gives it the information needed to choose one of the many possible realisations, which reduces over-smoothing. At synthesis time, it uses the predicted values, which can also be changed by hand (see [Expressive and controllable synthesis](#content:controllablesynthesis)). These extra predictors are called the *variance adaptor*. In effect, FastSpeech 2 brings back the duration and F0 models of classical parametric synthesis, but learns them with neural networks.

**Glow-TTS** {cite}`kim2020glow` removes the need for an external aligner. It searches for the most likely monotonic alignment between phonemes and frames with dynamic programming, in the same way as the Viterbi algorithm finds the best path through a hidden Markov model. The alignment and the model are learned together, and the durations found in training are used to train a duration predictor.

## Fully end-to-end models

The models above produce a mel spectrogram, and a separately trained vocoder produces the waveform. As described on the [neural vocoders](#content:neuralvocoders) page, the vocoder then gets inputs that differ from those it was trained on. An end-to-end model learns the whole path from phonemes to waveform at once.

**VITS** {cite}`kim2021conditional` combines several of the methods above in one model: the alignment search of Glow-TTS, a variational autoencoder whose hidden variables describe the variation that is not given by the text, a normalising flow, and a HiFi-GAN-style decoder that produces the waveform. Durations are predicted with a random element, so the same sentence can be spoken with different rhythms. In listening tests, VITS sounded better than two-stage systems built from the same data, and close to the recordings. It is widely used in open-source synthesisers, which are available for many languages, and small versions of it run in real time without a GPU.

**NaturalSpeech** {cite}`tan2024naturalspeech` developed this approach further. On one single-speaker test set, listeners found no statistically significant difference between its speech and the recordings. This shows that, for read speech in a single voice and style, the problem of natural-sounding synthesis is largely solved.

## Multi-speaker and multilingual models

A *multi-speaker* model is trained on many speakers at once. It gets a *speaker embedding*, a vector that describes the voice, as an extra input. The embedding can be learned for each speaker in the training data, or it can be computed from a recording by a separate network. If that network is trained for [speaker recognition](#content:recotasks), it gives embeddings for any voice, even one that was not in the training data. A model can then imitate a new voice from a few seconds of speech {cite}`jia2018transfer`. YourTTS {cite}`casanova2022yourtts` applied this to VITS, for several languages. Such early zero-shot systems captured the general character of a new voice, but the similarity was clearly lower than for voices seen in training.

A more reliable way to get a new voice is *adaptation*: a model trained on many speakers is fine-tuned with a few minutes of speech from the new speaker. Multilingual models share one model across languages, usually with a shared phoneme set such as the International Phonetic Alphabet. They make it possible to synthesise languages with little data, and to let a voice speak a language that its speaker never recorded.

## Sound examples

The same sentence, "Speech synthesis has changed more in the last ten years than in the forty years before", from three models trained on the same data, the LJ Speech corpus of one female reader. Tacotron 2 and FastSpeech 2 use the same HiFi-GAN vocoder. VITS produces the waveform directly. The models and licences are listed in [sounds/README.md](sounds/README.md).

| Model | Type | Listen |
|---|---|---|
| Tacotron 2 | autoregressive, attention | [Tacotron 2](sounds/acoustic_tacotron2.wav) |
| FastSpeech 2 | non-autoregressive, explicit durations | [FastSpeech 2](sounds/acoustic_fastspeech2.wav) |
| VITS | end-to-end | [VITS](sounds/acoustic_vits.wav) |

## Strengths and limits

The models on this page are the workhorses of practical speech synthesis. A good single-speaker voice needs roughly 10 to 25 hours of clean, consistently read speech. The models are small, often with a few tens of millions of parameters, so they run on phones and small computers without a GPU. Their behaviour is predictable, and the explicit durations make them robust.

Their limits are expressiveness and scale. With one voice and one reading style in the training data, they speak in one voice and one style. Prosody over longer stretches of text, such as a paragraph or a dialogue, is often monotonous, because the models see only one sentence at a time and still tend towards the average. Imitating new voices from short recordings works only moderately well. These limits are what the large-scale models described in [Large-scale and zero-shot synthesis](#content:zeroshotsynthesis) address.

## References

```{bibliography}
:filter: docname in docnames
```
