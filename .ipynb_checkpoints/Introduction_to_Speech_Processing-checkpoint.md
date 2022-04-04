# Introduction to Speech Processing

<div class="contentLayout2">

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

------------------------------------------------------------------------

List of authors: Tom Bäckström, Okko Räsänen, Abraham Zewoudie, Pablo
Pérez Zarazaga, Liisa Koivusalo

Includes contributions from Sneha Das

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Table of contents

-   [Preface](Preface)

1.  [Introduction](Introduction)
    1.  [Why speech processing?](Why_speech_processing_)
    2.  [Speech production and acoustic
        properties](Speech_production_and_acoustic_properties)
    3.  [Speech
        perception](https://en.wikipedia.org/wiki/Speech_perception)
        (Wikipedia)
    4.  [Linguistic structure of
        speech](https://wiki.aalto.fi/display/ITSP/Linguistic+structure+of+speech)
    5.  [Speech-Language
        pathology](https://en.wikipedia.org/wiki/Speech-language_pathology)
        (Wikipedia)
    6.  [Applications and systems
        structures](Applications_and_systems_structures)
    7.  [Social and cognitive processes involved in human
        communication](http://pressbooks-dev.oer.hawaii.edu/messageprocessing/)
        (external)
2.  [Basic representations and
    models](Basic_representations_and_models)  
    1.  [Waveform](Waveform)
    2.  [Windowing](Windowing)
    3.  [Signal energy, loudness and
        decibel](Signal_energy_loudness_and_decibel)
    4.  [Spectrogram and the STFT](Spectrogram_and_the_STFT)
    5.  [Autocorrelation and
        autocovariance](Autocorrelation_and_autocovariance)
    6.  [Cepstrum and MFCC](Cepstrum_and_MFCC)
    7.  [Linear prediction](Linear_prediction)
    8.  [Fundamental frequency (F0)](Fundamental_frequency_F0_)
    9.  [Zero-crossing rate](Zero-crossing_rate)
    10. [Deltas and Delta-deltas](Deltas_and_Delta-deltas)
    11. [PSOLA](Pitch-Synchoronous_Overlap-Add_PSOLA_)
    12. [Jitter and shimmer](Jitter_and_shimmer)
        (also <a href="https://www.sltinfo.com/acoustic-measures-norms/"
        style="letter-spacing: 0.0px;">Jitter, shimmer, harmonicity etc</a>
        (external link))
    13. [Crest factor](https://en.wikipedia.org/wiki/Crest_factor)
        (Wikipedia)
3.  [Pre-processing](Pre-processing)
    1.  [Pre-emphasis](Pre-emphasis)
    2.  [Noise gate](https://en.wikipedia.org/wiki/Noise_gate)
        (Wikipedia)
    3.  [Dynamic Range
        Compression](https://en.wikipedia.org/wiki/Dynamic_range_compression)
        (Wikipedia)
    4.  [Voice activity detection (VAD)](Voice_activity_detection_VAD_)
    5.  [Speech enhancement](Speech_enhancement)
4.  [Modelling tools in speech
    processing](Modelling_tools_in_speech_processing)
    1.  [Linear regression](Linear_regression)
    2.  [Sub-space models](Sub-space_models)
    3.  [Vector quantization (VQ)](Vector_quantization_VQ_)
    4.  [Gaussian mixture model (GMM)](Gaussian_mixture_model_GMM_)
    5.  [Neural networks](Neural_networks)
    6.  [Non-negative Matrix and Tensor
        Factorization](Non-negative_Matrix_and_Tensor_Factorization)
5.  [Evaluation of speech processing
    methods](Evaluation_of_speech_processing_methods)
    1.  [Subjective quality evaluation](Subjective_quality_evaluation)
    2.  [Objective quality evaluation](Objective_quality_evaluation)
    3.  [Other performance measures](Other_performance_measures)
    4.  [Analysis of evaluation results](Analysis_of_evaluation_results)
6.  [Speech analysis](Speech_analysis)
    1.  [Fundamental frequency
        estimation](Fundamental_frequency_estimation)
    2.  Formant estimation and tracking
    3.  [Inverse filtering for glottal activity
        estimation](Inverse_filtering_for_glottal_activity_estimation)
7.  [Recognition tasks in speech
    processing](Recognition_tasks_in_speech_processing)  
    1.  [Voice activity detection (VAD)](Voice_activity_detection_VAD_)

    2.  [Keyword or wake-word spotting](Wake-word_and_keyword_spotting)

    3.  [Speech recognition](Speech_Recognition)

    4.  [Speaker recognition and
        verification](Speaker_Recognition_and_Verification)

    5.  [Speaker diarization](Speaker_Diarization)

    6.  [Paralinguistic speech
        processing](Paralinguistic_speech_processing)
8.  Natural language processing
9.  [Speech synthesis](Speech_Synthesis)
    1.  [Concatenative speech synthesis](Concatenative_speech_synthesis)
    2.  [Statistical parametric speech
        synthesis](Statistical_parametric_speech_synthesis)
10. [Transmission, storage and
    telecommunication](Transmission_storage_and_telecommunication)  
    1.  [Design goals](Design_goals)
    2.  [Basic tools](Basic_tools)
        1.  [Modified discrete cosine transform
            (MDCT)](Modified_discrete_cosine_transform_MDCT_)
        2.  [Entropy coding](Entropy_coding)
        3.  [Perceptual modelling in speech and audio
            coding](Perceptual_modelling_in_speech_and_audio_coding)
        4.  [Vector quantization (VQ)](Vector_quantization_VQ_)
        5.  [Linear prediction](Linear_prediction)
    3.  [Code-excited linear prediction
        (CELP)](Code-excited_linear_prediction_CELP_)
    4.  [Frequency-domain coding](Frequency-domain_coding)
11. [Speech enhancement](Speech_enhancement)
    1.  [Noise attenuation](Noise_attenuation)
    2.  [Echo cancellation](Echo_cancellation)
    3.  [Bandwidth extension (BWE)](Bandwidth_extension_BWE_)
    4.  Dereverberation
    5.  Source separation
    6.  [Beamforming](Multi-channel_speech_enhancement_and_beamforming)
12. [Voice and speech
    analysis](https://en.wikipedia.org/wiki/Voice_analysis) (wikipedia)
    1.  Measurements for medical applications
        1.  [Electroglottography](https://en.wikipedia.org/wiki/Electroglottograph)
            (Wikipedia)
        2.  Stroboscopy and
            [videokymography](https://en.wikipedia.org/wiki/Videokymography)
            (Wikipedia)
        3.  Highspeed camera
        4.  MRI
        5.  Rothenberg mask
        6.  [Glottal inverse filtering](Glottal_inverse_filtering)
    2.  [Forensic analysis](Forensic_analysis)
13. [Chatbots / Conversational
    design](https://landbot.io/blog/guide-to-conversational-design/)
    (external link)
14. [Computational models of human language
    processing](Computational_models_of_human_language_processing)
15. [Security and privacy in speech
    technology](Security_and_privacy_in_speech_technology)
16. [References](References)

  

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

</div>

<div class="cell normal" data-type="normal">

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## Licence

[<img src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png"
style="border-width: 0;" alt="Creative Commons License" />](http://creativecommons.org/licenses/by-sa/4.0/)  
This work is licensed under a [Creative Commons Attribution-ShareAlike
4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/).

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

<div class="columnLayout single" layout="single">

<div class="cell normal" data-type="normal">

<div class="innerCell">

  

</div>

</div>

</div>

</div>
