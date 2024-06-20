import torchaudio
import torch
import scipy

class PreProcessing(torch.nn.Module):
    def __init__(
        self,
        input_samplerate    = 16000,
        resample_samplerate = 16000,
        window_length_ms    = 30
    ):
        super().__init__()
        self.resample = torchaudio.transforms.Resample(orig_freq=input_samplerate, new_freq=resample_samplerate)
        n_fft = (2*window_length_ms * resample_samplerate) // 2000
        hop_length = n_fft // 2
        self.spec = torchaudio.transforms.Spectrogram(n_fft=n_fft,power=None,hop_length=hop_length)
        self.output_size = (n_fft+2)//2


    def forward(self, waveform: torch.Tensor) -> torch.Tensor:
        # Resample the input
        resampled = self.resample(waveform)

        # Convert to power spectrogram
        spec = self.spec(resampled).mT

        return spec

        

class PostProcessing(torch.nn.Module):
    def __init__(
        self,
        output_samplerate   = 16000,
        resample_samplerate = 16000,
        window_length_ms    = 30
    ):
        super().__init__()
        self.resample = torchaudio.transforms.Resample(orig_freq=resample_samplerate, new_freq=output_samplerate)
        n_fft = (2*window_length_ms * resample_samplerate) // 2000
        hop_length = n_fft // 2
        self.invspec = torchaudio.transforms.InverseSpectrogram(n_fft=n_fft,hop_length=hop_length)


    def forward(self, spec: torch.Tensor) -> torch.Tensor:
        # Convert to power spectrogram
        waveform = self.invspec(spec.mT)

        # Resample the output
        resampled = self.resample(waveform)

        return resampled


