import torch
from frontend import PreProcessing, PostProcessing


class SimpleEnhancer(torch.nn.Module):
    def __init__(
        self,
        input_samplerate    = 16000,
        resample_samplerate = 16000,
        window_length_ms    = 30,
        device              = 'cpu'
    ):
        super().__init__()
        self.device       = device
        self.preprocessor = PreProcessing(
            input_samplerate    = input_samplerate, 
            resample_samplerate  = resample_samplerate, 
            window_length_ms     = window_length_ms
        )
        self.postprocessor = PostProcessing(
            output_samplerate   = input_samplerate, 
            resample_samplerate = resample_samplerate, 
            window_length_ms    = window_length_ms
        )

        self.GRU = torch.nn.GRU(
            input_size  = self.preprocessor.output_size,
            hidden_size = 24,
            device=device
        )
        self.dense_output = torch.nn.Sequential(
            torch.nn.Linear(
                self.GRU.hidden_size,
                self.preprocessor.output_size,
                device = device),
            torch.nn.Sigmoid()
        )
        


    def forward(self, waveform: torch.Tensor, smoothing:torch.Tensor=None) -> torch.Tensor:
        input_spec = self.preprocessor(waveform).to(self.device)
        input_features = input_spec.abs()

        _,state = self.GRU(input_features)
        hidden,_ = self.GRU(input_features,state)
        gains = self.dense_output(hidden) 

        estimated_spec = input_spec * gains

        reconstructed = self.postprocessor(estimated_spec.to('cpu'))
        return reconstructed

    def pass_through(self, waveform: torch.Tensor) -> torch.Tensor:
        input_spec = self.preprocessor(waveform)
        reconstructed = self.postprocessor(input_spec)
        return reconstructed



if 0:
    # sanity check

    dataset = NoisySpeech(path,device=device)
    noisy_audio,clean_audio,input_samplerate = dataset.__getitem__(0)
    
    preprocessor = PreProcessing(input_samplerate=input_samplerate)
    postprocessor = PostProcessing(output_samplerate=input_samplerate)    
    enhancer = SimpleEnhancer(
        input_samplerate=input_samplerate,
        device=device
    )

    clean_resampled = postprocessor.resample(preprocessor.resample(clean_audio))
    reconstructed = enhancer(noisy_audio)


class NoiseModelEnhancer(torch.nn.Module):
    def __init__(
        self,
        input_samplerate    = 16000,
        resample_samplerate = 16000,
        window_length_ms    = 30,
        enhancer_size       = 48,
        noise_model_size    = 24,
        device              = 'cpu'
    ):
        super().__init__()
        self.device = device
        self.preprocessor = PreProcessing(
            input_samplerate=input_samplerate, 
            resample_samplerate=resample_samplerate, 
            window_length_ms=window_length_ms
        )
        self.postprocessor = PostProcessing(
            output_samplerate=input_samplerate, 
            resample_samplerate=resample_samplerate, 
            window_length_ms=window_length_ms
        )

        self.noise_model = torch.nn.GRU(
            input_size = self.preprocessor.output_size,
            hidden_size = noise_model_size,
            device=device
        )
        self.enhancer = torch.nn.GRU(
            input_size = self.preprocessor.output_size + noise_model_size,
            hidden_size = enhancer_size,
            device=device
        )
        self.dense_output = torch.nn.Sequential(
            torch.nn.Linear(
                self.enhancer.hidden_size,
                self.preprocessor.output_size,
                device=device),
            torch.nn.Sigmoid()
        )
        


    def forward(self, waveform: torch.Tensor, smoothing:torch.Tensor=None) -> torch.Tensor:
        input_spec = self.preprocessor(waveform).to(self.device)
        input_features = input_spec.abs()

        noise_estimate,_ = self.noise_model(input_features)        
        enhancer_features = torch.cat((input_features, noise_estimate),dim=1)

        hidden,_ = self.enhancer(enhancer_features)
        gains = self.dense_output(hidden) 

        estimated_spec = input_spec * gains

        reconstructed = self.postprocessor(estimated_spec.to('cpu'))
        return reconstructed

    def pass_through(self, waveform: torch.Tensor) -> torch.Tensor:
        input_spec = self.preprocessor(waveform)
        reconstructed = self.postprocessor(input_spec)
        return reconstructed

if 0:
    # sanity check

    dataset = NoisySpeech(path,device=device)
    noisy_audio,clean_audio,input_samplerate = dataset.__getitem__(0)
    
    enhancer = NoiseModelEnhancer(
        input_samplerate=input_samplerate,
        device=device
    )

    clean_resampled = enhancer.pass_through(clean_audio)
    reconstructed = enhancer(noisy_audio)


class VADNoiseModelEnhancer(torch.nn.Module):
    def __init__(
        self,
        input_samplerate=16000,
        resample_samplerate=16000,
        window_length_ms = 30,
        enhancer_size = 48,
        noise_model_size = 24,
        vad_model_size = 24,
        device='cpu'
    ):
        super().__init__()
        self.device = device
        self.preprocessor = PreProcessing(
            input_samplerate=input_samplerate, 
            resample_samplerate=resample_samplerate, 
            window_length_ms=window_length_ms
        )
        self.postprocessor = PostProcessing(
            output_samplerate=input_samplerate, 
            resample_samplerate=resample_samplerate, 
            window_length_ms=window_length_ms
        )

        self.VAD = torch.nn.GRU(
            input_size = self.preprocessor.output_size,
            hidden_size = vad_model_size,
            device=device
        )
        self.VAD_output = torch.nn.Linear(vad_model_size,1,device=device)
        
        self.noise_model = torch.nn.GRU(
            input_size = self.preprocessor.output_size + vad_model_size,
            hidden_size = noise_model_size,
            device=device
        )
        
        self.enhancer = torch.nn.GRU(
            input_size = self.preprocessor.output_size + noise_model_size + vad_model_size,
            hidden_size = enhancer_size,
            device=device
        )
        self.dense_output = torch.nn.Sequential(
            torch.nn.Linear(
                self.enhancer.hidden_size,
                self.preprocessor.output_size,
                device=device),
            torch.nn.Sigmoid()
        )
        


    def forward(self, waveform: torch.Tensor, smoothing:torch.Tensor=None) -> torch.Tensor:
        input_spec = self.preprocessor(waveform).to(self.device)
        input_features = input_spec.abs()

        vad_estimate,_ = self.VAD(input_features)
        vad_output = self.VAD_output(vad_estimate)

        noise_estimate,_ = self.noise_model(torch.cat(
            (input_features,
             vad_estimate),
            dim=1))
        hidden,_ = self.enhancer(torch.cat(
            (input_features,
             noise_estimate, 
             vad_estimate),
            dim=1))
        gains = self.dense_output(hidden) 

        estimated_spec = input_spec * gains

        reconstructed = self.postprocessor(estimated_spec.to('cpu'))
        return reconstructed

    def pass_through(self, waveform: torch.Tensor) -> torch.Tensor:
        input_spec = self.preprocessor(waveform)
        reconstructed = self.postprocessor(input_spec)
        return reconstructed

if 0:
    # sanity check

    dataset = NoisySpeech(path,device=device)
    noisy_audio,clean_audio,input_samplerate = dataset.__getitem__(0)
    
    enhancer = VADNoiseModelEnhancer(
        input_samplerate=input_samplerate,
        device=device
    )

    clean_resampled = enhancer.pass_through(clean_audio)
    reconstructed = enhancer(noisy_audio)
 