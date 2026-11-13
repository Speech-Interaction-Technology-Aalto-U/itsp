(content:synthesis)=
# Speech Synthesis

Speech synthesis means producing speech with a computer. Most often, the input is written text, and the systems are then called text-to-speech (TTS) systems. Speech synthesis is used in

- screen readers and other tools for people with visual impairments or reading difficulties,
- voice assistants, navigation systems and other spoken interfaces,
- audiobooks, dubbing and speech-to-speech translation, and
- *voice banking*, where people who are about to lose their voice, for example because of a disease, record their speech so that a synthesiser can later speak with their own voice.

Related tasks use much of the same technology. In *voice conversion*, the input is speech, and the output is the same message spoken in a different voice. In *singing synthesis*, the input is lyrics and a musical score.

Speech synthesis has changed more in the last ten years than in the 40 years before. Until about 2016, the best systems joined together pieces of recorded speech, or they predicted the parameters of a classical vocoder with a statistical model. Today, almost all systems are based on neural networks. The newest systems are trained on tens of thousands of hours of speech, and they can imitate a new voice from a few seconds of recorded audio. This page gives an overview. The sub-pages describe each family of methods in more detail.

## The structure of a TTS system

A classical TTS system has three blocks ({numref}`fig:synthesis_pipelines`, second row):

1. **Text analysis** converts the text into a description of how it should be spoken: a sequence of phonemes, with information about stress, phrasing and intonation.
2. **The acoustic model** converts this description into acoustic features, such as a spectral envelope and the fundamental frequency (F0) for each frame of speech.
3. **The vocoder** converts the acoustic features into a speech waveform. See also [Vocoder](#content:vocoder).

Over time, these blocks have been merged and replaced. Unit selection systems replace the acoustic model and vocoder by choosing and joining pieces of recorded speech. Neural two-stage systems keep the structure, but use neural networks for both the acoustic model and the vocoder. The features between them are then usually a mel spectrogram (see [Mel-cepstrum](#content:melcepstrum)). End-to-end systems learn the whole path from phonemes or characters to the waveform as one network. Codec language models describe speech as a sequence of discrete *tokens*, much like words in text, and generate them with the same type of model that is used for text.

```{figure} Synthesis/attachments/synthesis_pipelines.svg
:name: fig:synthesis_pipelines

The structure of different types of speech synthesis systems. Grey blocks are rule-based or retrieve recorded speech, blue blocks are statistical or neural models that predict features, and red blocks generate the waveform. The labels on the arrows show the data passed between blocks.
```

## Text analysis

Text analysis converts the input text into a representation that tells the later blocks how the text should be spoken. It has three main tasks.

**Text normalisation.** First, the text is cleaned and converted to a standard form. Written and spoken language differ: abbreviations, acronyms, numbers, dates, units and symbols must be expanded into words. For example, "100 sq ft" should be read as "one hundred square feet", not "one-zero-zero sq ft". This is harder than it looks. "Dr." can mean "doctor" or "drive", and "1/2" can be a date or a fraction. The correct reading depends on the context.

**Grapheme-to-phoneme conversion.** Next, the system decides how each word is pronounced, that is, it converts letters (graphemes) into phonemes (see [Phonemes](#content:phonemes)). How hard this is depends on the language. Finnish spelling follows pronunciation closely, so simple rules work well. English spelling does not, so English systems need large pronunciation dictionaries and models that guess the pronunciation of unknown words. *Homographs*, words that are written the same but pronounced differently, must be resolved from context, such as "read" in "I read books" and "I read it yesterday". Names and loan words from other languages are a common source of errors.

**Prosody prediction.** Finally, the system adds information that is not written in the text: where to pause, which syllables are stressed, which word is in focus, and how the intonation should go. For example, the system must tell questions from statements, and it must find the word that should be emphasised in each sentence.

In classical systems, each of these tasks is a separate module, made with rules, dictionaries and small statistical models. In neural systems, much of this work moves into the acoustic model. Many end-to-end systems take characters or subword tokens as input and learn pronunciation and prosody from data. Even so, most practical systems still normalise the text first, and many still convert it to phonemes. Phonemes make it possible to fix the pronunciation of a single word, and they help when there is little training data, such as for languages with few speakers. Errors in text normalisation are still among the most common errors of modern systems.

## A short history

{numref}`fig:synthesis_timeline` shows the main families of methods over time.

```{figure} Synthesis/attachments/synthesis_timeline.svg
:name: fig:synthesis_timeline

Approximate timeline of speech synthesis methods, with some milestones. Grey: methods based on rules or on joining recorded speech. Blue: statistical and neural models. Red: large-scale generative models.
```

- **Formant and articulatory synthesis** generate speech from a model of speech production. Formant synthesisers control the resonances of the vocal tract with hand-made rules {cite}`klatt1980software`. The result is intelligible but sounds clearly artificial. Articulatory synthesis, which models the movements of the tongue, lips and other articulators, is still used in speech research.
- **Concatenative synthesis** joins pieces of recorded speech. Early systems used a small set of short units, such as diphones. *Unit selection* {cite}`hunt1996unit` chooses the best units from hours of recorded speech. It can sound very natural, but only in the voice and style of the recordings. See [Concatenative speech synthesis](#content:concatenative).
- **Statistical parametric speech synthesis (SPSS)** predicts the parameters of a vocoder with a statistical model, first hidden Markov models (HMMs) and later neural networks {cite}`zen2009statistical`. It is flexible and needs less data, but the classical vocoder makes the speech sound muffled and buzzy. See [Statistical parametric speech synthesis](#content:spss).
- **Neural synthesis** started with WaveNet in 2016 {cite}`oord2016wavenet`, a neural network that generates the waveform one sample at a time. In 2018, Tacotron 2 combined a neural acoustic model with a WaveNet vocoder and was rated almost as natural as recorded speech {cite}`shen2018natural`. See [Neural vocoders](#content:neuralvocoders) and [Neural acoustic models](#content:neuralacousticmodels).
- **Large-scale and zero-shot synthesis** applies methods from large language models and image generation to speech. Models are trained on tens of thousands of hours of speech from many speakers. They can imitate a new voice from a short recording, without further training {cite}`chen2025neural`. See [Large-scale and zero-shot synthesis](#content:zeroshotsynthesis).

## What makes a good synthesiser?

The main goals of speech synthesis are speech that is

- **natural**: it sounds like a human speaker,
- **intelligible**: listeners understand every word,
- **similar to a target speaker**, when the system should speak with a particular voice, and
- **expressive and controllable**: it can use different speaking styles and emotions, and users can control them (see [Expressive and controllable synthesis](#content:controllablesynthesis)).

There are also practical requirements:

- **Robustness.** The system must read every input correctly, including rare words, long sentences and unusual punctuation. It should never skip or repeat words.
- **Latency.** In a dialogue, the user should hear the first sound within a fraction of a second. Systems that can start playing before the whole sentence is generated are called *streaming* systems.
- **Computational cost and model size.** Synthesis on a phone or in a car must run on limited hardware. A service with many users must keep the cost per user low.
- **Data.** A classical single-speaker system needs a few hours of carefully recorded speech. Large-scale systems need tens of thousands of hours, which brings questions of data quality, licences and consent (see [Data for speech synthesis](#content:synthesisdata)).

These goals often conflict. Large models sound better but are slower, and fast models may sound worse. Systems that imitate any voice are also easier to misuse.

## Evaluating synthetic speech

The quality of synthetic speech is best measured with [listening tests](#content:subjectiveevaluation). Listeners rate the naturalness of each sample on a scale from 1 to 5, and the average is the *mean opinion score* (MOS). In a comparison test (CMOS), listeners compare two versions of the same sentence. To measure speaker similarity, listeners rate how similar a sample is to a recording of the target speaker. Intelligibility can be tested by asking listeners to write down what they hear. Since 2005, the yearly Blizzard Challenge has compared systems built from the same data with the same listening test {cite}`black2005blizzard`. It has made it possible to follow the progress of the field over time {cite}`king2014measuring`.

Listening tests are slow and expensive, so research papers also report [objective measures](#content:objectiveevaluation):

- the *word error rate* of a speech recogniser that transcribes the synthetic speech, as a measure of intelligibility (see [Recognition tasks](#content:recotasks)),
- the similarity of *speaker embeddings*, vectors that describe the voice, between the synthetic speech and the target speaker, and
- MOS predicted by a neural network that has been trained on the results of earlier listening tests, such as UTMOS {cite}`saeki2022utmos`.

These measures must be used with care. The best systems now get MOS ratings close to those of recorded speech, so small differences become hard to measure. Objective measures can also be fooled. For example, speech with exaggerated articulation can get a low word error rate even though it sounds unnatural. Results are only comparable when the test sentences, voice prompts and listening test are the same.

## Misuse, consent and safeguards

Modern systems can imitate a voice from a few seconds of recorded speech. This makes useful applications possible, such as voice banking and dubbing in the original actor's voice. It also makes misuse easy: synthetic speech has been used in phone scams, to fool voice-based authentication, and to put false statements in the mouths of public figures. Such fake recordings are often called *deepfakes*.

The main safeguards are

- **consent**: a person's voice should only be cloned with their permission, and the data used to train a system should be collected with the consent of the speakers,
- **watermarking**: the system hides a signal in the generated speech that cannot be heard but can be detected later {cite}`sanroman2024proactive` (see the example in [Large-scale and zero-shot synthesis](#content:zeroshotsynthesis)), and
- **detection**: classifiers that tell synthetic speech from real speech. The ASVspoof challenges have compared such methods since 2015 {cite}`wang2020asvspoof`. Detection is an arms race, because detectors must also work for synthesis methods that did not exist when they were trained.

See also [Security and privacy](#privacy).

## Pages in this chapter

- [Concatenative speech synthesis](#content:concatenative)
- [Statistical parametric speech synthesis](#content:spss)
- [Neural vocoders](#content:neuralvocoders)
- [Neural acoustic models](#content:neuralacousticmodels)
- [Large-scale and zero-shot synthesis](#content:zeroshotsynthesis)
- [Expressive and controllable synthesis](#content:controllablesynthesis)
- [Data for speech synthesis](#content:synthesisdata)

## Further reading

- Xu Tan, *Neural Text-to-Speech Synthesis* {cite}`tan2023neural`. A textbook on neural TTS, from text analysis to vocoders.
- Paul Taylor, *Text-to-Speech Synthesis* {cite}`taylor2009text`. A textbook on classical TTS, with a thorough treatment of text analysis.
- Xie et al., *Towards controllable speech synthesis in the era of large language models* {cite}`xie2025controllable`. A survey of recent systems, with a focus on how to control them.
- Simon King, *Using Speech Synthesis to give Everyone their own Voice*, University of Edinburgh. Video ([link](https://www.youtube.com/watch?v=xzL-pxcpo-E)). An overview of unit selection and statistical parametric synthesis, with sound examples, and of voice banking.

```{bibliography}
:filter: docname in docnames
```
