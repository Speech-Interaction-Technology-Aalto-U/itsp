(content:synthesisdata)=
# Data for speech synthesis

A speech synthesiser can only be as good as the data it learns from. It copies the voice, the speaking style, the pronunciation and also the faults of its training data, such as noise, reverberation and mispronunciations. This page describes what data speech synthesis needs, what is available, how data is prepared, and what is missing. For general questions of data quality and bias, see [Speech data and experiment design](#content:data). A table of open corpora for speech synthesis is in [Corpora for speech synthesis](#content:ttscorpora).

## What the data must contain

The needs depend on the type of synthesiser, and they have changed a lot.

**Classical and small neural systems** need one speaker, recorded in a studio, reading in a consistent style, with exact transcripts. Unit selection needs several hours and good coverage of all diphones of the language, and every segment must be labelled (see [Concatenative speech synthesis](#content:concatenative)). Statistical parametric and [neural acoustic models](#content:neuralacousticmodels) need roughly 1 to 25 hours. A typical example is LJ Speech {cite}`ito2017lj`: 24 hours of a single speaker reading audiobooks.

**Multi-speaker systems** use hundreds of speakers with less data each, so that the model learns what is common to all voices and what differs between them. Read audiobooks are the most common source, because they come with a text, and many are in the public domain. LibriTTS {cite}`zen2019libritts` was made from audiobook data originally collected for speech recognition, by choosing segments that are suitable for synthesis.

**Large-scale and zero-shot systems** use tens or hundreds of thousands of hours from thousands of speakers. At this scale, no one records data for the purpose. Instead, the data is "found" speech from audiobooks, podcasts, talk shows and videos, and the transcripts are made by a speech recogniser. Libri-Light {cite}`kahn2020librilight` (about 60 000 hours of audiobooks) and Emilia {cite}`he2025emilia` (over 100 000 hours of spontaneous speech in six languages) are examples.

There is a trade-off between clean and small and noisy and large. Large models can learn from data with noise, reverberation and errors in the transcripts, and they gain a much wider range of voices and styles. But they also learn to reproduce the noise, and a zero-shot model copies the recording conditions of its voice prompt. A small model trained on clean studio speech gives clean output, but only in one voice and style.

## Preparing data

Raw recordings must be processed before they can be used for training. The main steps are

- **cutting** long recordings into utterances, typically of a few seconds to a few tens of seconds, at pauses,
- **text normalisation and checking the transcripts**, so that the text matches what was actually said, including numbers and abbreviations (see [Text analysis](#content:synthesis)),
- **alignment**: a forced aligner finds the start and end of each phoneme or word {cite}`mcauliffe2017montreal`. Durations from the aligner are needed by models with explicit duration predictors, such as FastSpeech 2,
- **level normalisation and resampling** to a common loudness and sampling rate, typically 22.05 or 24 kHz, or 44.1 or 48 kHz for high-quality systems, and
- **removing** utterances with music, overlapping speakers, strong noise, or transcripts that do not match.

For found data, these steps must be automatic. A typical pipeline separates speech from music, removes noise with [speech enhancement](#content:enhancement), splits the recordings by speaker with speaker diarisation, transcribes the speech with a speech recogniser (see [Recognition tasks](#content:recotasks)), and finally removes utterances of low quality, for example by predicting their MOS with a neural network (see [Evaluating synthetic speech](#content:synthesis)). Speech enhancement can also be used to improve existing corpora. LibriTTS-R {cite}`koizumi2023librittsr` is LibriTTS processed in this way, and models trained on it sound clearly cleaner.

## Available data

The open corpora fall into a few groups (see the table in [Corpora for speech synthesis](#content:ttscorpora)):

- **Single-speaker studio or audiobook recordings**, such as CMU ARCTIC {cite}`kominek2004cmu` and LJ Speech, for classical and small neural systems.
- **Multi-speaker read speech**, such as VCTK {cite}`yamagishi2019cstr`, LibriTTS and Hi-Fi TTS {cite}`bakhturina2021hifi`, for multi-speaker models.
- **Large-scale data**, such as Libri-Light, Multilingual LibriSpeech {cite}`pratap2020mls` and Emilia, for large-scale and zero-shot models.
- **Other languages**, such as CSS10 {cite}`park2019css10`, which has single-speaker audiobook data for ten languages, and Common Voice {cite}`ardila2020common`, which has read speech in over 100 languages. Common Voice is recorded by volunteers at home with varying equipment, so it suits speech recognition better than synthesis.
- **Expressive speech**, such as ESD {cite}`zhou2022emotional`, with acted emotions, and Expresso {cite}`nguyen2023expresso`, with read and improvised speech in many styles.

Test sets matter too. Zero-shot systems are usually compared on a few test sets, for example selected sentences of LibriSpeech {cite}`panayotov2015librispeech` with fixed voice prompts. Results are only comparable when the test sentences, the prompts and the evaluation method are the same.

## What is missing

Despite the large amount of data, many needs are not met.

**Languages with little data.** Most open data is in English or Mandarin. Many languages have no open corpus that is suitable for speech synthesis, and even for languages with millions of speakers the available data may be small. Finnish is a typical example. The open Finnish synthesis data consists mainly of about 10 hours of audiobooks read by one speaker in CSS10. Finnish has large corpora of spontaneous speech, such as the 3 600 hours of Lahjoita puhetta {cite}`moisio2023lahjoita`, collected from over 20 000 speakers. But such corpora were made for speech recognition and research on spoken language, and their recording quality varies too much for most synthesis systems.

**Spontaneous and conversational speech.** Most synthesis data is read speech, and read speech sounds different from conversation. Fillers, hesitations, laughter, overlapping speech and turn-taking are rare in the data, which limits synthesis for spoken dialogue.

**Expressive speech with labels.** Data with reliable labels of emotion and style, or with natural-language descriptions of how something is said, is scarce and mostly acted (see [Expressive and controllable synthesis](#content:controllablesynthesis)).

**Under-represented speakers.** Children, older people, speakers of dialects and non-native accents, and people with speech disorders are rare in the data. Synthesis then works worse for them. This matters especially for voice banking, where people with a progressive disease want a synthetic voice that sounds like their own.

**Clear licences and consent.** Much of the large-scale data is published for non-commercial use only, or collected from the internet without asking the speakers. With voice cloning, the voices in training data can be imitated, so the consent of the speakers matters more than for other speech tasks (see [Misuse, consent and safeguards](#content:synthesis)).

**Shared benchmarks.** There are few fixed, openly available test sets and listening-test protocols for zero-shot, expressive and conversational synthesis, so results from different papers are hard to compare.

## References

```{bibliography}
:filter: docname in docnames
```
