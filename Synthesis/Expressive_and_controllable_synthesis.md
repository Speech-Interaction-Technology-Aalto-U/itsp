(content:controllablesynthesis)=
# Expressive and controllable synthesis

The same sentence can be spoken in many ways. "You did that?" can sound surprised, angry, impressed or amused. The difference lies in the *prosody*: the pitch contour, the timing and pauses, the loudness, and the voice quality (see [Speech production](#content:speechproduction)). Prosody signals which word is important, whether a sentence is a question, how the speaker feels, and when a speaker has finished their turn.

For neutral read speech in many languages, synthesis is now close to human quality. Expressive speech is not: an audiobook narrator who gives each character a voice, a game character who shouts in anger, or a voice assistant that sounds sympathetic when the user is upset. Two questions arise. How can a model produce the full range of prosody, instead of an average? And how can a user tell the model which prosody they want? A recent survey covers this area in detail {cite}`xie2025controllable`.

## The one-to-many problem

The text does not say how it should be spoken, so there are many correct outputs for each input. A model trained to minimise the distance between its output and the recording learns to produce the average of all the ways the sentence was spoken in the training data. The average of many intonation contours is a flat contour, so the result sounds monotonous.

There are two main solutions:

- **Give the model more information.** If the model is told the pitch, energy and durations, or a description of the style, the output is no longer ambiguous. FastSpeech 2 does this in training, with values measured from the recording (see [Neural acoustic models](#content:neuralacousticmodels)).
- **Use a generative model.** Variational autoencoders (as in VITS), diffusion and flow matching, and language models all learn the *distribution* of possible outputs and draw one sample from it, instead of predicting the average (see [Large-scale and zero-shot synthesis](#content:zeroshotsynthesis)). Each sample is one plausible way of speaking the sentence.

The second solution produces varied and natural prosody, but not necessarily the prosody that the user wants. For that, we need control.

## Control by reference audio

The most direct way to describe a speaking style is to give an example. A *reference encoder* computes a vector from a reference recording, and the synthesiser uses this vector as an extra input. Trained this way, a Tacotron model could transfer the prosody of a reference recording to a different sentence, or to a different voice {cite}`skerryryan2018towards`. *Global style tokens* {cite}`wang2018style` learn a small set of style vectors without any labels. The style of a recording is described as a weighted combination of these tokens, and the weights can also be set by hand to produce a new style.

In zero-shot systems, the voice prompt plays this role. The model copies the voice, emotion and speaking style of the prompt, and also its recording conditions. This is both a strength and a weakness. To get angry speech in a given voice, we need an angry recording of that voice. Some zero-shot systems add a simple control on top of the prompt. With the same voice prompt, the Chatterbox model can be asked for [ordinary](sounds/zeroshot_chatterbox_p334.wav) or [more expressive](sounds/control_chatterbox_p334_expressive.wav) speech (the prompt is in [Large-scale and zero-shot synthesis](#content:zeroshotsynthesis)). Some systems split speech into separate parts, such as content, prosody and voice, so that the voice can be taken from one prompt and the prosody from another {cite}`ju2024naturalspeech`.

## Control by explicit parameters

Models with explicit pitch, energy and duration predictors, such as FastSpeech 2, let the user change these values directly. We can raise the pitch on one word to emphasise it, slow down a phrase, or make the whole utterance louder. Signal-model vocoders, such as neural source-filter models, give the same kind of control over pitch at the vocoder level (see [Neural vocoders](#content:neuralvocoders)). This control is precise and easy to understand, but it is low-level. Getting a convincing emotion by editing pitch and timing by hand takes a lot of work, and large changes cause artefacts.

The examples below change the predicted durations and pitch of FastSpeech 2 (the models and licences are listed in [sounds/README.md](sounds/README.md)):

| Change | Listen |
|---|---|
| none | [original](sounds/acoustic_fastspeech2.wav) |
| all durations × 1.35 | [slower](sounds/control_fastspeech2_slow.wav) |
| all durations × 0.75 | [faster](sounds/control_fastspeech2_fast.wav) |
| pitch × 1.3 | [higher](sounds/control_fastspeech2_high.wav) |
| pitch × 0.8 | [lower](sounds/control_fastspeech2_low.wav) |

Emotion can also be given as a label, such as "happy" or "sad", sometimes with an intensity. This requires training data labelled with emotions, usually acted by professional speakers. The ESD database, for example, contains the same sentences spoken with five emotions by 20 speakers {cite}`zhou2022emotional`.

In commercial systems, users often control the output with markup in the input text. The Speech Synthesis Markup Language (SSML) {cite}`w3c2010ssml` is a standard way to mark pauses, emphasis, speaking rate, pitch and the pronunciation of single words.

## Control by natural-language descriptions

The newest systems take a description in ordinary language, such as "a calm, low female voice, speaking slowly in a large room", or an instruction, such as "say this as if you were telling a secret". PromptTTS {cite}`guo2023prompttts` and InstructTTS {cite}`yang2024instructtts` were early examples. Such systems can also design a new voice from a description alone, without any reference recording.

The main difficulty is data. Training needs recordings paired with descriptions of how they are spoken, and few such recordings exist. Writing descriptions by hand for thousands of hours is too expensive. One solution is to compute simple properties automatically, such as gender, average pitch, speaking rate and the amount of noise, and to turn them into sentences with a text language model {cite}`lyth2024natural`. Such *synthetic annotations* describe the voice and recording well, but say little about emotion or intent.

## Evaluating expressive speech

Expressiveness is harder to evaluate than naturalness, because there is no single correct answer. Listening tests can ask whether listeners recognise the intended emotion, or whether the speech matches a description. Objective measures include emotion classifiers and statistics of pitch and timing. All of these capture only part of what makes speech expressive. A sentence can have the "right" emotion and still sound wrong in context. Evaluation of expressive and controllable synthesis is therefore still an open research problem, together with the lack of suitable training data (see [Data for speech synthesis](#content:synthesisdata)).

## References

```{bibliography}
:filter: docname in docnames
```
