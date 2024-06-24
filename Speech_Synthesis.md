(content:synthesis)=
# Speech Synthesis

Speech synthesis systems aim at producing intelligible speech signals
from some type of input language representation. Synthesis systems are
also often referred to as text-to-speech (TTS) systems, as written text
is a natural way to instruct what type of utterances should be produced.

A typical TTS system consists of two basic processing modules: text
analysis module and a speech synthesis module. 

  

**Text analysis**

The first module of a TTS pipeline, the text analysis module, is
responsible for converting the incoming text into a linguistic
representation that encodes the information of how the input text should
be spoken.

As the first step, the module must process the text into a standardized
format by taking care of any special characters or other
inconsistencies. Then the text must be structurally analyzed to identify
syntactical components of the sentences. Any inconsistencies between the
written and spoken language (e.g., abbreviations and acronyms, proper
names, numbers) must be detected and converted into a correct format
(e.g., to map the string "100 sq ft" into "*one hundred* *square feet*",
not "*one-zero-zero sq ft*") .  

The second step consists of inferring the correct pronunciation of the
words, also known as grapheme-to-phoneme conversion. Since the
relationship between written and spoken language is not always
straightforward, the text analysis module must convert strings of input
letters into strings of phonemes based on the pronunciation conventions
of the given language. This involves resolving many ambiguities
prevalent in languages, such as how to deal with homographs, that is,
words with the same written form but different pronunciations. Foreign
language words and loan words have to be handled as well.

As the final stage, suprasegmental characteristics of the
speech-to-be-produced must be introduced to the linguistic
representation. Durations of the phonemes and intermediate pauses must
be defined, even though the information does not exist in the text. In
order to make the speech natural sounding and intelligible, the process
also includes introduction of any potential rhythmic structure, stress
patterns, and intonational cues to the linguistic representation. For
this purpose, the text analysis module must interpret syntactic
properties of the input text. For instance, the system must be able to
differentiate different sentence types such as questions from statements
and to infer which word should receive focus in the given sentential
context.  

  

**Synthesis algorithms**

The second key module consists of the speech synthesizer module. Input
to the synthesizer is the linguistic representation produced by the text
analysis block while the output consists of acoustic waveforms of
synthesized speech. There are several potential technical approaches to
the creation of a speech waveform from linguistic instructions.
Historically, methods such as formant synthesis or articulatory
synthesis have been utilized (where the latter is still used in speech
research). However, modern commercial speech synthesizers are based on
one of the two alternative techniques: [concatenative
synthesis](Synthesis/Concatenative_speech_synthesis.md) or [statistical parametric speech synthesis](Synthesis/Statistical_parametric_speech_synthesis.md). Both methods
are described in more detail in their respective sub-sections. 

![synthesis_basic_schematic](Synthesis/attachments/175517689.png)
**Figure 1:** The basic structure of a speech synthesis system.**  


  

In general, synthesis algorithms aim at speech output that maximally
resembles natural speech, is free of noise and artifacts, and has high
intelligibility. Other characteristics may include possibility to use
different speaker voices or to speaking styles to account for different
use contexts and user preferences. In practical use, computational
complexity of the system may also become a relevant design factor. This
is especially true if the system must support real-time speech
production and/or serve multiple users simultaneously. For instance,
speech synthesis used on a standard mobile device or in a car
entertainment system must operate with strict latency computational
complexity constraints.

Speech quality and intelligibility a speech synthesizer are typically
evaluated using [subjective listening
tests.](content:subjectiveevaluation)

  

**Further readings & material**

Simon King - Using Speech Synthesis to give Everyone their own Voice,
University of Edinburgh. Youtube video
([link](https://www.youtube.com/watch?v=xzL-pxcpo-E)). *Includes an
overview of unit selection and statistical parametric synthesis with
sound demonstrations.*

Kim Silverman - Speech synthesis lecture at ICSI, Berkeley. Youtube
video ([link](https://www.youtube.com/watch?v=7mjh0PSUv0M)).

Sai Krishna Rallabandi's on-line list of introductory resources for
speech synthesis
([link](http://www.cs.cmu.edu/~srallaba/Learn_Synthesis/intro.html))

  

