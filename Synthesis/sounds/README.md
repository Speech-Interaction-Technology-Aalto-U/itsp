# Sound examples of the speech synthesis chapter

All files were made with [generate_sound_examples.py](../generate_sound_examples.py) in November 2026. The level of active speech is normalised to −24 dBFS in all files, so that they can be compared at the same loudness.

The text of all synthetic examples is: *"Speech synthesis has changed more in the last ten years than in the forty years before."*

## Licence

The generated files are released under CC BY-SA 4.0, like the rest of the book. They contain or are derived from the following material:

- **CSTR VCTK Corpus 0.92** (Yamagishi, Veaux and MacDonald, University of Edinburgh, 2019, [doi:10.7488/ds/2645](https://doi.org/10.7488/ds/2645)), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Used for the files `vctk_*.wav` (trimmed and resampled to 24 kHz), the vocoder examples `vocoder_*.wav` (resynthesised from `vctk_p334_011_mic2.wav`), and as voice prompts for the files `zeroshot_*.wav` and `control_chatterbox_*.wav`. The corpus was recorded for research on speech synthesis and voice cloning. The copy used was the Hugging Face dataset `jspaulsen/vctk`, which contains the original 48 kHz recordings.
- **Models**, all with permissive licences. The models trained on LJ Speech speak with the voice of the LJ Speech reader; LJ Speech is in the public domain.

| Model | Revision | Licence | Training data | Used for |
|---|---|---|---|---|
| [speechbrain/tts-hifigan-libritts-22050Hz](https://huggingface.co/speechbrain/tts-hifigan-libritts-22050Hz) | 418850313160 | Apache 2.0 | LibriTTS | `vocoder_hifigan.wav` |
| [charactr/vocos-mel-24khz](https://huggingface.co/charactr/vocos-mel-24khz) | 0feb3fdd929b | MIT | LibriTTS | `vocoder_vocos.wav` |
| WORLD vocoder ([pyworld](https://github.com/JeremyCCHsu/Python-Wrapper-for-World-Vocoder) 0.3.5) | | modified BSD | none | `vocoder_world.wav` |
| Griffin–Lim ([librosa](https://librosa.org) 0.11.0) | | ISC | none | `vocoder_griffinlim.wav` |
| [speechbrain/tts-tacotron2-ljspeech](https://huggingface.co/speechbrain/tts-tacotron2-ljspeech) | d01e530d6d8e | Apache 2.0 | LJ Speech | `acoustic_tacotron2.wav` |
| [speechbrain/tts-fastspeech2-ljspeech](https://huggingface.co/speechbrain/tts-fastspeech2-ljspeech) | c50d854a2b3f | Apache 2.0 | LJ Speech | `acoustic_fastspeech2.wav`, `control_fastspeech2_*.wav` |
| [speechbrain/tts-hifigan-ljspeech](https://huggingface.co/speechbrain/tts-hifigan-ljspeech) | 17fbdc3aae35 | Apache 2.0 | LJ Speech | vocoder for the Tacotron 2 and FastSpeech 2 examples |
| [kakao-enterprise/vits-ljs](https://huggingface.co/kakao-enterprise/vits-ljs) | 3bcb8321394f | MIT | LJ Speech | `acoustic_vits.wav` |
| [ResembleAI/chatterbox](https://huggingface.co/ResembleAI/chatterbox) (chatterbox-tts 0.1.7) | 5bb1f6ee58e5 | MIT | not disclosed | `zeroshot_*.wav`, `control_chatterbox_*.wav` |

The Chatterbox examples contain an inaudible watermark (Perth), which the model adds to all its output.

## Files

| File | Content |
|---|---|
| `vctk_p334_011_mic2.wav` | Recording, VCTK speaker p334 (American English, male). Source for the vocoder examples. |
| `vctk_p247_016_mic2.wav` | Recording, VCTK speaker p247 (Scottish English, male). Voice prompt. |
| `vctk_p334_016_mic2.wav` | Recording, VCTK speaker p334. Voice prompt. |
| `vocoder_griffinlim.wav` | Griffin–Lim (64 iterations) from an 80-band mel spectrogram, 22.05 kHz, up to 8 kHz. |
| `vocoder_world.wav` | WORLD analysis and synthesis, 24 kHz. |
| `vocoder_hifigan.wav` | HiFi-GAN from the same mel spectrogram as Griffin–Lim. |
| `vocoder_vocos.wav` | Vocos from its own 100-band mel spectrogram, 24 kHz. |
| `acoustic_tacotron2.wav` | Tacotron 2 + HiFi-GAN. |
| `acoustic_fastspeech2.wav` | FastSpeech 2 + HiFi-GAN. |
| `acoustic_vits.wav` | VITS. |
| `control_fastspeech2_slow.wav`, `_fast.wav` | FastSpeech 2 with all durations multiplied by 1.35 and 0.75. |
| `control_fastspeech2_high.wav`, `_low.wav` | FastSpeech 2 with the pitch multiplied by 1.3 and 0.8. |
| `zeroshot_chatterbox_p247.wav` | Chatterbox, voice prompt `vctk_p247_016_mic2.wav`. |
| `zeroshot_chatterbox_p334.wav` | Chatterbox, voice prompt `vctk_p334_016_mic2.wav`. |
| `control_chatterbox_p334_expressive.wav` | Chatterbox, prompt p334, with stronger expression (exaggeration 1.0 instead of 0.5). |

## Checks

All synthetic files were transcribed with Whisper (`openai/whisper-small.en`), and all transcripts matched the intended text. The cosine similarity of ECAPA speaker embeddings (`speechbrain/spkrec-ecapa-voxceleb`) between each zero-shot example and its voice prompt was 0.86 (p247) and 0.80 (p334), and about 0.2 to the other speaker's prompt.
