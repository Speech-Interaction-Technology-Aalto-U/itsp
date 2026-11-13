"""Make the sound examples of the speech synthesis chapter.

The examples are already in sounds/. This script documents how they were made,
so that they can be checked, regenerated or extended. Each step needs its own
optional packages; none of them is needed to build the book.

Steps (run in this order; each writes WAV files to sounds/ next to this script):

  prepare  <vctk>  Copy the source recordings from the CSTR VCTK Corpus 0.92.
                   <vctk> is either the folder of the original corpus or a
                   parquet file of a copy on Hugging Face (e.g. jspaulsen/vctk).
                   Needs: numpy, soundfile, librosa (and pyarrow for parquet).
  vocoders         Copy synthesis of one VCTK sentence with Griffin-Lim, WORLD,
                   HiFi-GAN and Vocos.
                   Needs: torch, torchaudio, speechbrain, vocos, pyworld, librosa.
  acoustic         One sentence with Tacotron 2, FastSpeech 2 and VITS, all
                   trained on LJ Speech.
                   Needs: torch, speechbrain, transformers, phonemizer + espeak.
  control          FastSpeech 2 with changed speaking rate and pitch.
                   Needs: as for acoustic.
  zeroshot         Zero-shot synthesis with Chatterbox, with VCTK voice prompts.
                   Needs: chatterbox-tts (best in its own environment).
  describe         Parler-TTS controlled by text descriptions.
                   Needs: parler-tts (best in its own environment).
                   NOT RUN YET: parler-tts depends on an unreleased version of
                   descript-audiotools, which is only available from GitHub.

The models, their licences and the exact settings are listed in sounds/README.md.
All neural models run on the CPU with a limited number of threads, so that the
computer stays usable while the script runs.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOUNDS = os.path.join(HERE, "sounds")
CACHE = os.environ.get("ITSP_MODEL_CACHE",
                       os.path.expanduser("~/.cache/itsp_models"))
THREADS = int(os.environ.get("ITSP_THREADS", "4"))

# Text used for all synthesis examples.
TEXT = ("Speech synthesis has changed more in the last ten years "
        "than in the forty years before.")

# Source recordings from VCTK (speaker, utterance, microphone).
VCTK_VOCODER = ("p334", "011", "mic2")   # American English, male
VCTK_PROMPTS = [("p247", "016", "mic2"),  # Scottish English, male
                ("p334", "016", "mic2")]  # American English, male


def vctk_name(spk, utt, mic):
    return f"vctk_{spk}_{utt}_{mic}.wav"


def save(name, x, sr):
    """Normalise the level of active speech and write a 16-bit WAV file."""
    import numpy as np
    import soundfile as sf
    x = np.asarray(x, dtype=np.float64).squeeze()
    frame = int(0.02 * sr)
    n = len(x) // frame
    rms = np.sqrt(np.mean(x[: n * frame].reshape(n, frame) ** 2, axis=1) + 1e-12)
    active = rms[rms > rms.max() * 10 ** (-30 / 20)]
    level = np.sqrt(np.mean(active ** 2))
    x = x * (10 ** (-24 / 20) / level)          # active speech at -24 dBFS
    peak = np.max(np.abs(x))
    if peak > 10 ** (-1 / 20):                  # keep peaks below -1 dBFS
        x = x * (10 ** (-1 / 20) / peak)
    os.makedirs(SOUNDS, exist_ok=True)
    path = os.path.join(SOUNDS, name)
    sf.write(path, x, sr, subtype="PCM_16")
    print(f"Wrote {path} ({len(x) / sr:.1f} s, {sr} Hz)")


def load(name, sr=None):
    import librosa
    x, fs = librosa.load(os.path.join(SOUNDS, name), sr=sr)
    return x, fs


def limit_threads():
    import torch
    torch.set_num_threads(THREADS)
    torch.manual_seed(0)


# --------------------------------------------------------------------------
def prepare(vctk):
    """Copy, trim and resample the VCTK recordings to 24 kHz."""
    import io
    import numpy as np
    import soundfile as sf
    import librosa

    wanted = [VCTK_VOCODER] + VCTK_PROMPTS
    found = {}
    if os.path.isdir(vctk):
        # Original corpus: wav48_silence_trimmed/<spk>/<spk>_<utt>_<mic>.flac
        for spk, utt, mic in wanted:
            path = os.path.join(vctk, "wav48_silence_trimmed", spk,
                                f"{spk}_{utt}_{mic}.flac")
            found[(spk, utt, mic)] = sf.read(path)
    else:
        import pyarrow.parquet as pq
        ids = {f"{s}_{u}_{m}": (s, u, m) for s, u, m in wanted}
        for row in pq.read_table(vctk).to_pylist():
            if row["id"] in ids:
                found[ids[row["id"]]] = sf.read(io.BytesIO(row["audio"]["bytes"]))
    for key in wanted:
        x, fs = found[key]
        x, _ = librosa.effects.trim(x, top_db=35)
        x = librosa.resample(x, orig_sr=fs, target_sr=24000)
        pad = np.zeros(int(0.15 * 24000))
        save(vctk_name(*key), np.concatenate([pad, x, pad]), 24000)


# --------------------------------------------------------------------------
def vocoders():
    """Copy synthesis: analyse a recording and resynthesise it with a vocoder."""
    import numpy as np
    import torch
    import librosa
    limit_threads()
    name = vctk_name(*VCTK_VOCODER)

    # Mel spectrogram as used by the HiFi-GAN model (22.05 kHz, 80 bands).
    from speechbrain.lobes.models.HifiGAN import mel_spectrogram
    from speechbrain.inference.vocoders import HIFIGAN
    x22, _ = load(name, sr=22050)
    mel = mel_spectrogram(audio=torch.tensor(x22, dtype=torch.float32),
                          sample_rate=22050, hop_length=256, win_length=None,
                          n_mels=80, n_fft=1024, f_min=0.0, f_max=8000.0,
                          power=1, normalized=False, norm="slaney",
                          mel_scale="slaney", compression=True)

    # Griffin-Lim from the same mel spectrogram.
    mag_mel = np.exp(mel.numpy())
    stft_mag = librosa.feature.inverse.mel_to_stft(
        mag_mel, sr=22050, n_fft=1024, power=1, fmin=0.0, fmax=8000.0,
        norm="slaney", htk=False)
    y = librosa.griffinlim(stft_mag, n_iter=64, hop_length=256, win_length=1024,
                           n_fft=1024, random_state=0)
    save("vocoder_griffinlim.wav", y, 22050)

    # HiFi-GAN trained on LibriTTS (other speakers than the test sentence).
    hifigan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-libritts-22050Hz",
                                   savedir=os.path.join(CACHE, "hifigan-libritts"))
    with torch.no_grad():
        y = hifigan.decode_batch(mel.unsqueeze(0)).squeeze().numpy()
    save("vocoder_hifigan.wav", y, 22050)

    # WORLD: F0, spectral envelope and aperiodicity.
    import pyworld
    x24, _ = load(name, sr=24000)
    x64 = x24.astype(np.float64)
    f0, sp, ap = pyworld.wav2world(x64, 24000)
    save("vocoder_world.wav", pyworld.synthesize(f0, sp, ap, 24000), 24000)

    # Vocos, from its own 100-band mel spectrogram at 24 kHz.
    from vocos import Vocos
    vocos = Vocos.from_pretrained("charactr/vocos-mel-24khz")
    with torch.no_grad():
        y = vocos(torch.tensor(x24, dtype=torch.float32).unsqueeze(0)).squeeze().numpy()
    save("vocoder_vocos.wav", y, 24000)


# --------------------------------------------------------------------------
def _speechbrain_ljspeech():
    from speechbrain.inference.vocoders import HIFIGAN
    return HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-ljspeech",
                                savedir=os.path.join(CACHE, "hifigan-ljspeech"))


def _fastspeech2():
    from speechbrain.inference.TTS import FastSpeech2
    return FastSpeech2.from_hparams(source="speechbrain/tts-fastspeech2-ljspeech",
                                    savedir=os.path.join(CACHE, "fastspeech2-ljspeech"))


def acoustic():
    """The same sentence with three acoustic models trained on LJ Speech."""
    import torch
    limit_threads()
    hifigan = _speechbrain_ljspeech()

    from speechbrain.inference.TTS import Tacotron2
    tacotron2 = Tacotron2.from_hparams(source="speechbrain/tts-tacotron2-ljspeech",
                                       savedir=os.path.join(CACHE, "tacotron2-ljspeech"))
    with torch.no_grad():
        mel, _, _ = tacotron2.encode_text(TEXT)
        y = hifigan.decode_batch(mel).squeeze().numpy()
    save("acoustic_tacotron2.wav", y, 22050)

    fastspeech2 = _fastspeech2()
    with torch.no_grad():
        mel, _, _, _ = fastspeech2.encode_text([TEXT], pace=1.0, pitch_rate=1.0,
                                               energy_rate=1.0)
        y = hifigan.decode_batch(mel).squeeze().numpy()
    save("acoustic_fastspeech2.wav", y, 22050)

    from transformers import VitsModel, AutoTokenizer
    model = VitsModel.from_pretrained("kakao-enterprise/vits-ljs")
    tokenizer = AutoTokenizer.from_pretrained("kakao-enterprise/vits-ljs")
    with torch.no_grad():
        y = model(**tokenizer(TEXT, return_tensors="pt")).waveform.squeeze().numpy()
    save("acoustic_vits.wav", y, model.config.sampling_rate)


def control():
    """FastSpeech 2 with explicit changes of speaking rate and pitch."""
    import torch
    limit_threads()
    hifigan = _speechbrain_ljspeech()
    fastspeech2 = _fastspeech2()
    # In SpeechBrain's FastSpeech 2, the durations are multiplied by pace,
    # so pace > 1 gives slower speech.
    settings = {"control_fastspeech2_slow.wav": dict(pace=1.35),
                "control_fastspeech2_fast.wav": dict(pace=0.75),
                "control_fastspeech2_high.wav": dict(pitch_rate=1.3),
                "control_fastspeech2_low.wav": dict(pitch_rate=0.8)}
    for name, s in settings.items():
        args = dict(pace=1.0, pitch_rate=1.0, energy_rate=1.0)
        args.update(s)
        with torch.no_grad():
            mel, _, _, _ = fastspeech2.encode_text([TEXT], **args)
            y = hifigan.decode_batch(mel).squeeze().numpy()
        save(name, y, 22050)


# --------------------------------------------------------------------------
def zeroshot():
    """Zero-shot synthesis with Chatterbox, prompted with VCTK recordings."""
    limit_threads()
    from chatterbox.tts import ChatterboxTTS
    model = ChatterboxTTS.from_pretrained(device="cpu")
    for spk, utt, mic in VCTK_PROMPTS:
        prompt = os.path.join(SOUNDS, vctk_name(spk, utt, mic))
        wav = model.generate(TEXT, audio_prompt_path=prompt,
                             exaggeration=0.5, cfg_weight=0.5)
        save(f"zeroshot_chatterbox_{spk}.wav", wav.squeeze().numpy(), model.sr)
    # Stronger expression with the same prompt (used on the control page).
    spk, utt, mic = VCTK_PROMPTS[1]
    prompt = os.path.join(SOUNDS, vctk_name(spk, utt, mic))
    wav = model.generate(TEXT, audio_prompt_path=prompt,
                         exaggeration=1.0, cfg_weight=0.3)
    save(f"control_chatterbox_{spk}_expressive.wav", wav.squeeze().numpy(), model.sr)


# --------------------------------------------------------------------------
DESCRIPTIONS = {
    "control_parler_calm.wav":
        "A female speaker with a low-pitched voice speaks slowly and calmly. "
        "The recording is of very high quality, with the speaker's voice "
        "sounding clear and very close up.",
    "control_parler_lively.wav":
        "A male speaker with a high-pitched voice delivers his words quickly "
        "and in an animated way, in a room with some background noise.",
}


def describe():
    """Parler-TTS: the voice and style are given as a text description."""
    import torch
    limit_threads()
    from parler_tts import ParlerTTSForConditionalGeneration
    from transformers import AutoTokenizer
    name = "parler-tts/parler-tts-mini-v1"
    model = ParlerTTSForConditionalGeneration.from_pretrained(name)
    tokenizer = AutoTokenizer.from_pretrained(name)
    for out, description in DESCRIPTIONS.items():
        torch.manual_seed(0)
        with torch.no_grad():
            audio = model.generate(
                input_ids=tokenizer(description, return_tensors="pt").input_ids,
                prompt_input_ids=tokenizer(TEXT, return_tensors="pt").input_ids)
        save(out, audio.squeeze().numpy(), model.config.sampling_rate)


if __name__ == "__main__":
    steps = {"vocoders": vocoders, "acoustic": acoustic, "control": control,
             "zeroshot": zeroshot, "describe": describe}
    if len(sys.argv) >= 3 and sys.argv[1] == "prepare":
        prepare(sys.argv[2])
    elif len(sys.argv) == 2 and sys.argv[1] in steps:
        steps[sys.argv[1]]()
    else:
        print(__doc__)
        sys.exit(1)
