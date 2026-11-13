(content:zeroshotsynthesis)=
# Large-scale and zero-shot synthesis

Around 2023, speech synthesis took up two ideas from other areas of machine learning. From large language models (LLMs) for text, it took the idea of training one large model on a huge amount of data and then steering it with a *prompt*. From image generation, it took diffusion models and their relatives. Together, they changed what a synthesiser can do.

The first change is the scale of the data. The [neural acoustic models](#content:neuralacousticmodels) of the previous page are trained on tens of hours of carefully recorded speech. The new models are trained on tens or hundreds of thousands of hours of speech from audiobooks, podcasts and videos, with transcripts made by a speech recogniser (see [Data for speech synthesis](#content:synthesisdata)).

The second change is *zero-shot* synthesis: the model can speak with a voice that it has never heard in training, given only a short recording of that voice, often 3 to 10 seconds. No further training is needed. The recording, called the *voice prompt*, tells the model not only how the speaker sounds, but also the speaking style, the emotion and the acoustic environment. The model continues "in the same way", much like a text LLM continues a text in the style of its prompt. This is called *in-context learning*.

This page describes the main families of such models. The field changes quickly, so the focus is on the ideas, not on the details of particular systems. Recent surveys give more detail {cite}`xie2025controllable,mousavi2025discrete`.

## Speech as tokens

A text language model works on *tokens*, such as words or parts of words, taken from a fixed vocabulary. To use the same methods for speech, we must first turn speech into a sequence of tokens. This is done with a neural audio codec {cite}`zeghidour2021soundstream,defossez2022encodec`.

A codec has three parts. An encoder network turns the waveform into a sequence of vectors, for example 75 per second. A quantiser replaces each vector by the index of the nearest vector in a codebook (see [Vector quantization](#content:vq)). A decoder network, trained like a [GAN vocoder](#content:neuralvocoders), turns the quantised vectors back into a waveform. A single codebook cannot describe speech accurately with a reasonable size, so codecs use *residual vector quantisation*: a first codebook quantises the vector, a second codebook quantises the remaining error, a third the error that is still left, and so on. Each frame is therefore described by several tokens, one per codebook. For example, with 75 frames per second, 8 codebooks and 1024 entries (10 bits) per codebook, the bitrate is 75 × 8 × 10 = 6 000 bits per second.

Tokens from a codec are called *acoustic tokens*. They describe everything in the signal, including the voice and the background noise. Another type, *semantic tokens*, is made by clustering the features of a [self-supervised](../Modelling/Self_supervised_learning.md) model such as HuBERT {cite}`hsu2021hubert`. Semantic tokens mostly describe what is said and how, with less information about the voice and the recording conditions. AudioLM {cite}`borsos2023audiolm` showed that a model can first generate semantic tokens, which give the content a coherent structure, and then acoustic tokens, which give the audio quality. Many current systems use some form of this two-level structure.

## Neural codec language models

:::{admonition} Background: language models
:class: tip

A *language model* predicts the next token in a sequence from the tokens before it. It is trained on a large amount of data simply by trying to predict each token of the training data. To generate new data, it predicts a probability for each possible next token, chooses one at random according to these probabilities, adds it to the sequence, and repeats. Most current language models are transformers. The [autoregressive vocoders](#content:neuralvocoders) WaveNet and WaveRNN work in the same way, but with waveform samples instead of tokens.
:::

**VALL-E** {cite}`chen2025neural` treats speech synthesis as language modelling ({numref}`fig:codec_language_model`). Its input is the phoneme sequence of the prompt transcript and the new text, followed by the codec tokens of a 3-second voice prompt. A transformer then generates the tokens of the first codebook for the new text, one frame at a time. A second, non-autoregressive model generates the tokens of the remaining codebooks for all frames at once, and the codec decoder turns them into a waveform. VALL-E was trained on 60 000 hours of English audiobooks {cite}`kahn2020librilight`. Its speech kept the voice, emotion and even the acoustic environment of the prompt much better than earlier zero-shot systems.

```{figure} attachments/codec_language_model.svg
:name: fig:codec_language_model

A codec language model such as VALL-E. The tokens of a voice prompt (grey) are given. The model generates the first codebook for the new speech one token at a time (blue), and then the other codebooks for all frames at once (red).
```

Codec language models have the strengths of text LLMs: natural and varied prosody, in-context learning, and the possibility to stream the output while it is being generated. They also have the weaknesses of autoregressive models. They generate one frame at a time, which is slow. Because tokens are chosen at random, the same input gives a different output each time, and occasionally the model skips or repeats words, or produces noise, much like the attention errors of Tacotron. Later systems reduce these problems, for example by starting from a pre-trained text LLM, by using semantic tokens that are learned to agree with the text, or by generating several tokens per step.

## Diffusion and flow matching

:::{admonition} Background: diffusion and flow matching
:class: tip

A *diffusion model* {cite}`ho2020denoising` learns to remove noise. In training, we add a random amount of noise to real data, and the network learns to predict the noise. To generate, we start from pure noise and remove a little of it in each of many steps, until clean data remains.

*Flow matching* {cite}`lipman2023flow` is a simpler relative. It learns a *velocity*: the direction in which a noisy sample should move to get closer to the data. In the common variant, the path from noise to data is a straight line. Generation then follows these velocities from noise to data. Straight paths can be followed in fewer steps, so flow matching is usually faster than diffusion.

Unlike language models, both work on continuous values, such as mel spectrograms, and they generate the whole utterance at once in each step.
:::

**Grad-TTS** {cite}`popov2021gradtts` used diffusion to generate the mel spectrogram, with durations from an aligner as in Glow-TTS. **Matcha-TTS** {cite}`mehta2024matcha` replaced diffusion with flow matching and became both smaller and faster. Both are trained for one or a few speakers, like the models on the previous page.

The large-scale models use the same methods on far more data. **NaturalSpeech 2** {cite}`shen2024naturalspeech` generated the continuous hidden vectors of a codec with diffusion, trained on 44 000 hours of speech and singing, with a voice prompt. **Voicebox** {cite}`le2023voicebox` is trained with flow matching to fill in a missing part of a recording, given the text and the surrounding audio. The same model can then do zero-shot synthesis (fill in a whole new sentence after a prompt), edit a word in a recording, or remove noise. It was trained on over 50 000 hours, and it was more intelligible and up to 20 times faster than VALL-E. **NaturalSpeech 3** {cite}`ju2024naturalspeech` splits speech into separate token streams for content, prosody, voice and acoustic details, so that each can be generated or replaced separately.

**E2 TTS** {cite}`eskimez2024e2` and **F5-TTS** {cite}`chen2025f5tts` showed how simple such a system can be. The input characters are padded with filler symbols to the length of the speech, and the model learns the alignment by itself. There is no phoneme conversion, no duration model and no aligner. Only the total length of the speech must be given, for example estimated from the number of characters and the speaking rate of the prompt.

Diffusion and flow-matching models generate all frames at once, so they rarely skip or repeat words, and they are well suited to editing. Their drawbacks are that the total length must be known in advance and that streaming is harder, because the whole utterance is generated together.

## Hybrid and masked models

Many of the best current systems combine the two families. A language model first generates tokens that describe the content and prosody. A diffusion or flow-matching model then generates a mel spectrogram from these tokens and the voice prompt, and a vocoder produces the waveform. The language model gives natural prosody, and the second model gives high audio quality and a close match to the voice. Seed-TTS {cite}`anastassiou2024seedtts` and CosyVoice 2 {cite}`du2024cosyvoice` are examples. CosyVoice 2 is designed for streaming, so that the first sound can be played before the whole sentence is generated.

*Masked generative models* such as MaskGCT {cite}`wang2025maskgct` take a third route. They start from a sequence in which all tokens are hidden, and in each of a few steps they predict all hidden tokens and keep the most confident ones. Like diffusion, this generates all frames in parallel. Like a language model, it works with discrete tokens.

## Comparison

| Family | Examples | Output | Generation | Strengths | Weaknesses |
|---|---|---|---|---|---|
| Codec language model | VALL-E | discrete tokens | one frame at a time | natural prosody, in-context learning, streaming | slow, random errors such as skipped or repeated words |
| Diffusion and flow matching | NaturalSpeech 2, Voicebox, F5-TTS | continuous features | whole utterance, several steps | robust, editing, fast with few steps | total length must be given, streaming is harder |
| Masked generative model | MaskGCT | discrete tokens | whole utterance, several steps | parallel, no aligner | total length must be given |
| Hybrid | Seed-TTS, CosyVoice 2 | tokens, then mel spectrogram | language model, then diffusion or flow matching | high quality, streaming | large and complex |

## Sound examples

The examples below were made with Chatterbox, an open zero-shot model that combines a language model over speech tokens with a flow-matching decoder. The model gets the text and a voice prompt of about five seconds from the VCTK corpus. It was not adapted to these speakers in any other way. The models and licences are listed in [sounds/README.md](sounds/README.md).

| Speaker | Voice prompt | Synthesised: "Speech synthesis has changed more in the last ten years than in the forty years before." |
|---|---|---|
| VCTK p247 (Scottish English) | [prompt](sounds/vctk_p247_016_mic2.wav) | [synthesis](sounds/zeroshot_chatterbox_p247.wav) |
| VCTK p334 (American English) | [prompt](sounds/vctk_p334_016_mic2.wav) | [synthesis](sounds/zeroshot_chatterbox_p334.wav) |

The objective measures described in [Evaluating synthetic speech](#content:synthesis) confirm what we hear. A speech recogniser transcribed both examples without errors. The cosine similarity between the speaker embeddings of each example and its prompt was 0.86 for p247 and 0.80 for p334, while the similarity to the other speaker's prompt was only about 0.2.

Chatterbox also hides a watermark in everything it generates. A detector for this watermark gave a score of 1.00 for both examples, and 0.00 for the real recordings and for the VITS example on the previous page. This is one of the safeguards described in [Misuse, consent and safeguards](#content:synthesis).

## How good are they, and what remains?

On read speech, the best zero-shot systems now get listening-test ratings and word error rates close to those of the real recordings in their test sets. Several report that listeners cannot reliably tell their speech from the recordings. Such results must be read with care. They are measured on short, read sentences, with test sets and prompts chosen by the authors (see [Evaluating synthetic speech](#content:synthesis)).

Open problems include

- **robustness**: hard sentences, such as tongue twisters, repeated words, numbers and names, still cause errors,
- **long and conversational speech**: keeping prosody coherent over paragraphs and producing natural spontaneous speech, with hesitations, laughter and turn-taking,
- **languages**: most models cover a few languages with much data, while most of the world's languages have none (see [Data for speech synthesis](#content:synthesisdata)),
- **cost**: models with hundreds of millions to billions of parameters need GPUs, while many applications need small models on devices, and
- **misuse**: the better the imitation of voices, the greater the risk of fraud and deepfakes (see [Misuse, consent and safeguards](#content:synthesis)).

## Outlook: speech language models

The same methods are now used to build *speech language models*, which both understand and generate speech {cite}`cui2025recent,arora2025landscape`. Such models can answer a spoken question with spoken output directly, without converting the speech to text and back. Some can listen and speak at the same time, which allows natural turn-taking, interruptions and short feedback such as "mm-hm" in a conversation. In these systems, speech synthesis is no longer a separate module but one ability of a larger model. The basic building blocks, such as speech tokens, codecs, language models and flow matching, are the ones described on this page.

## References

```{bibliography}
:filter: docname in docnames
```
