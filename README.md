# Introduction to Speech Processing
--------------

### 2nd Edition


Authors: [Tom Bäckström](https://research.aalto.fi/en/persons/tom-b%C3%A4ckstr%C3%B6m), [Okko Räsänen](https://researchportal.tuni.fi/en/persons/okko-r%C3%A4s%C3%A4nen), [Abraham Zewoudie](https://research.aalto.fi/en/persons/abraham-zewoudie), Pablo Pérez Zarazaga, Liisa Koivusalo, Sneha Das


## Table of contents

1.  Forewords
    1. [Preface](Preface.md) <!-- checked -->
    2. [Background](Background.md)
1.  [Introduction](Introduction.md) <!-- checked -->
    1.  [Why speech processing?](Introduction/Why_speech_processing.md) <!-- checked -->
    2.  [Speech production and acoustic properties](Introduction/Speech_production_and_acoustic_properties.md) <!--checked -->
    3.  [Speech perception](https://en.wikipedia.org/wiki/Speech_perception) (Wikipedia)
    4.  [Linguistic structure of speech](Introduction/Linguistic_structure_of_speech.md) <!-- checked -->
    5.  [Speech-Language pathology](https://en.wikipedia.org/wiki/Speech-language_pathology) (Wikipedia)
    6.  [Applications and systems structures](Applications_and_systems_structures) <!-- checked -->
    7.  [Social and cognitive processes involved in human communication](http://pressbooks-dev.oer.hawaii.edu/messageprocessing/) (external)
2.  [Basic representations and models](Representations/Basic_representations_and_models.md)  
    1.  [Waveform](Representations/Waveform.ipynb) <!-- checked -->
    2.  [Windowing](Representations/Windowing.md)
    3.  [Signal energy, loudness and decibel](Representations/Signal_energy_loudness_and_decibel.md)
    4.  [Spectrogram and the STFT](Representations/Spectrogram_and_the_STFT.ipynb)
    5.  [Autocorrelation and autocovariance](Representations/Autocorrelation_and_autocovariance.md)
    6.  [Cepstrum and MFCC](Representations/Cepstrum_and_MFCC.md)
    7.  [Linear prediction](Representations/Linear_prediction.md)
    8.  [Fundamental frequency (F0)](Representations/Fundamental_frequency_F0_.md)
    9.  [Zero-crossing rate](Representations/Zero-crossing_rate.md)
    10. [Deltas and Delta-deltas](Representations/Deltas_and_Delta-deltas.md)
    11. [PSOLA](Representations/Pitch-Synchoronous_Overlap-Add_PSOLA_.md)
    12. [Jitter and shimmer](Representations/Jitter_and_shimmer.md)       
    13. [Crest factor](https://en.wikipedia.org/wiki/Crest_factor) (Wikipedia)
3.  [Pre-processing](Pre-processing.md)
    1.  [Pre-emphasis](Preprocessing/Pre-emphasis.md)
    2.  [Noise gate](https://en.wikipedia.org/wiki/Noise_gate) (Wikipedia)
    3.  [Dynamic Range Compression](https://en.wikipedia.org/wiki/Dynamic_range_compression) (Wikipedia)
    4.  [Voice activity detection (VAD)](Recognition/Voice_activity_detection_VAD_.md)
    5.  [Speech enhancement](Speech_enhancement.md)
4.  [Modelling tools in speech processing](Modelling_tools_in_speech_processing.md)
    1.  [Source and perceptual modelling](Modelling/Source_modelling_and_perceptual_modelling.md)
    1.  [Linear regression](Modelling/Linear_regression.md)
    2.  [Sub-space models](Modelling/Sub-space_models.md)
    3.  [Vector quantization (VQ)](Modelling/Vector_quantization_VQ_.md)
    4.  [Gaussian mixture model (GMM)](Modelling/Gaussian_mixture_model_GMM_.md)
    5.  [Neural networks](Modelling/Neural_networks.md)
    6.  [Non-negative Matrix and Tensor Factorization](Modelling/Non-negative_Matrix_and_Tensor_Factorization.md)
5.  [Evaluation of speech processing methods](Evaluation_of_speech_processing_methods)
    1.  [Subjective quality evaluation](Evaluation/Subjective_quality_evaluation.md)
    2.  [Objective quality evaluation](Evaluation/Objective_quality_evaluation.md)
    3.  [Other performance measures](Evaluation/Other_performance_measures.md)
    4.  [Analysis of evaluation results](Evaluation/Analysis_of_evaluation_results.md)
6.  [Speech analysis](Speech_analysis.md)
    1.  [Fundamental frequency estimation](Analysis/Fundamental_frequency_estimation.md)
    2.  Formant estimation and tracking
    3.  [Inverse filtering for glottal activity estimation](Analysis/Inverse_filtering_for_glottal_activity_estimation.md)
    12. [Voice and speech analysis](https://en.wikipedia.org/wiki/Voice_analysis) (wikipedia)
    1.  Measurements for medical applications
        1.  [Electroglottography](https://en.wikipedia.org/wiki/Electroglottograph) (Wikipedia)
        2.  Stroboscopy and [videokymography](https://en.wikipedia.org/wiki/Videokymography) (Wikipedia)
        3.  Highspeed camera
        4.  MRI
        5.  Rothenberg mask
        6.  [Glottal inverse filtering](Analysis/Glottal_inverse_filtering.md)
    2.  [Forensic analysis](Analysis/Forensic_analysis.md)
7.  [Recognition tasks in speech processing](Recognition_tasks_in_speech_processing.md)  
    1.  [Voice activity detection (VAD)](Recognition/Voice_activity_detection_VAD_.md)
    2.  [Keyword or wake-word spotting](Recognition/Wake-word_and_keyword_spotting.md)
    3.  [Speech recognition](Recognition/Speech_Recognition.md)
    4.  [Speaker recognition and verification](Recognition/Speaker_Recognition_and_Verification.md)
    5.  [Speaker diarization](Recognition/Speaker_Diarization.md)
    6.  [Paralinguistic speech processing](Recognition/Paralinguistic_speech_processing.md)
8.  Natural language processing
9.  [Speech synthesis](Speech_Synthesis.md)
    1.  [Concatenative speech synthesis](Synthesis/Concatenative_speech_synthesis.md)
    2.  [Statistical parametric speech synthesis](Synthesis/Statistical_parametric_speech_synthesis.md)
10. [Transmission, storage and telecommunication](Transmission_storage_and_telecommunication.md)  
    1.  [Design goals](Transmission/Design_goals.md)
    2.  [Basic tools](Transmission/Basic_tools.md)
        1.  [Modified discrete cosine transform (MDCT)](Transmission/Modified_discrete_cosine_transform_MDCT_.md)
        2.  [Entropy coding](Transmission/Entropy_coding.md)
        3.  [Perceptual modelling in speech and audio coding](Transmission/Perceptual_modelling_in_speech_and_audio_coding.md)
        4.  [Vector quantization (VQ)](Transmission/Vector_quantization_VQ_.md)
        5.  [Linear prediction](Transmission/Linear_prediction.md)
    3.  [Code-excited linear prediction (CELP)](Transmission/Code-excited_linear_prediction_CELP_.md)
    4.  [Frequency-domain coding](Transmission/Frequency-domain_coding.md)
11. [Speech enhancement](Speech_enhancement.md)
    1.  [Noise attenuation](Enhancement/Noise_attenuation.md)
    2.  [Echo cancellation](Enhancement/Echo_cancellation.md)
    3.  [Bandwidth extension (BWE)](Enhancement/Bandwidth_extension_BWE_.md)
    4.  Dereverberation
    5.  Source separation
    6.  [Beamforming](Enhancement/Multi-channel_speech_enhancement_and_beamforming.md)
13. [Chatbots / Conversational design](https://landbot.io/blog/guide-to-conversational-design/) (external link)
14. [Computational models of human language processing](Computational_models_of_human_language_processing.md)
15. [Security and privacy in speech technology](Security_and_privacy_in_speech_technology.md) <!-- checked -->




## Licence

[<img src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" style="border-width: 0;" alt="Creative Commons License" />](http://creativecommons.org/licenses/by-sa/4.0/)  
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

