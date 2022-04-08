# Machine learning tasks in speech processing

Typical tasks in speech processing, where machine learning is often
applied include:

-   *Speech recognition*, which refers to converting an acoustic
    waveform of spoken speech to the corresponding text
    (speech-to-text).
-   [Speaker recognition and speaker verification](Recognition/Speaker_Recognition_and_Verification.md), which refer to,
    respectively, identifying the speaker (who is speaking?) and
    verifying whether the speaker is who he claims to be (is it really
    you?).
-   [Wake-word and keyword detection](Recognition/Wake-word_and_keyword_spotting.md), refers to the task where the
    purpose is to find single characterizing words from continuous
    speech. The idea is that by using a light-weight algorithm, we can
    extract useful information without a computationally complex speech
    recognizer. Specifically, wake-word detection refers to the waiting
    for the activation command, that is, the device sleeps until the
    wake-word is heard. Keyword detection can refer to similar task, or
    for example, the task of recognizing the topic of a conversation.
-   [*Voice activity detection* (VAD)](Recognition/Voice_activity_detection_VAD_.md),
    refers to the task of determining whether a signal contains speech
    or not (is someone speaking?). Many of the above tasks are
    resource-intensive operations, such that we would like to, for
    example, use speech recognition only when speech is present. We can
    therefore first use a simple VAD to determine whether a signal is
    speech or not, and only start the speech recognizer when speech is
    present.
-   [Speech diarisation](Recognition/Speaker_Diarization.md) is the process of segmenting a multi-speaker conversation into continuous single-speaker segments.
-   [Paralinguistic speech processing](Recognition/Paralinguistic_speech_processing.md)

