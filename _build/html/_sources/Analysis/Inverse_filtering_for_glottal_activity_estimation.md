# Inverse filtering for glottal activity estimation


### Motivation

The main source of speech sounds, where the acoustic signal is first
created, are the vocal folds, which oscillate in the airflow generated
by the lungs (for details, see [Speech production and acoustic
properties](Speech_production_and_acoustic_properties)). The opening
between the vocal folds is known as the *glottis* and the movements of
vocal folds as well and the corresponding airflow are jointly known as
glottal activity.

Since glottal activity is thus central to speech, it is also important
to understand how it works. What makes a "good" voice? If there is a
disruption to the vocal folds, how does that affect the voice? These are
often medical questions, but they have a large social and societal
impact. If you loose your voice, you can easily become isolated since
you loose an important mode of communication. If you are in a voice
profession such as teaching, sales, singing or acting, also your ability
to work relies on your voice such that any disturbance in the voice
impedes your ability to work. Studying the glottis is thus paramount.

The vocal folds are located in the neck, covered and surrounded by a
cartilage. Accessing them is therefore difficult. Putting a camera in
the throat is uncomfortable to say the least and even when it is
possible, it impedes normal speech, giving measurements a bias of
unknown size. Moreover, since the vocal folds oscillate with a
fundamental frequency that can go up to 400 Hz, we need a camera whose
frame rate is at least 4000 Hz to get 10 frames per period. In other
words, we would need a high-speed camera. While such cameras are today
readily available, they need a lot of light, which generates a lot of
heat, which is not compatible within the sensitive tissues inside the
throat. Imaging with other methods, X-rays or magnetic resonance
imaging, generally have a slower frame rate and some imaging like X-rays
also generate harmful radiation (esp. at high frame rates).

The cartilage surrounding the vocal folds also prevents ultrasound
measurements. The only usable direct measurement is [electroglottography
(EGG)](https://en.wikipedia.org/wiki/Electroglottograph), which measures
the impedance through the neck using electrodes. It measures
conductivity, which is highly dependent on the contact area of the vocal
folds, thus giving information about the position of the vocal folds.
However, this information is usually one-dimensional which limits the
usability of such measurements. It also sensitive to and requires
careful placement of electrodes.

What remains is the acoustic signal. With a microphone, we can record
the sound emitted from the mouth, and try to deduce the movements of the
vocal folds from the sound. It is minimally invasive, because we do not
need to insert any sensors inside or onto the the body. Airflow through
the glottis is closely related to the movements of the vocal folds; when
the vocal folds are open air can flow and when they are closed, airflow
is stopped. Airflow in turn is related to the acoustic signal; sound is
a variation in air pressure such that the gradient of airflow
approximately translates to the corresponding sound.

When sound is generated in the vocal folds, it is however acoustically
shaped by the vocal tract (for details, again, see [Speech production
and acoustic properties](Speech_production_and_acoustic_properties));
some frequencies are emphasised and others attenuated. To analyse
glottal activity, we therefore need to cancel the acoustic effect of the
vocal tract. Recall that the effect of the vocal tract can be
efficiently modelled by a linear predictive filter. We can thus estimate
a filter corresponding to the effect of the vocal tract, and then invert
the effect of that filter. This process is known as *inverse filtering*.


### Signal Model

In glottal inverse filtering, we follow the source-filter paradigm for
speech source modelling, where the acoustic speech signal is modelled as
an excitation signal filtered by the vocal tract. The assumption is that
these two components are independent. By assuming that we know the
effect of the vocal tract, we can therefore remove its effect by
inverting its effect. If we further model the vocal tract as a
tube-model, its effect corresponds to IIR filtering, such that the
inverse process is FIR filtering.

The main difficulty in of glottal inverse filtering is estimation of the
filter corresponding to the effect of the vocal tract. The task
resembles classical [linear predictive](Linear_prediction) modelling,
where the parameters of an IIR filter are uniquely estimated from the
autocorrelation of the signal. Covertly, this however assumes that the
excitation is uncorrelated white noise. However, in voiced speech, the
excitation is the glottal excitation, which resembles a half-wave
rectified sinusoid. That is, it is a fairly smooth curve with a
characteristic comb-structure in the spectrum, as well as a distinct
tilt with more energy at low frequencies. Though we know a lot about the
glottal excitation, it is hard to model. If we would have the glottal
excitation, then the vocal tract would be easy to estimate and vice
versa - a typical chicken-and-egg problem.

One of the most popular methods for glottal inverse filtering is
iterative adaptive inverse filtering (IAIF), where both the glottal
excitation and the vocal tract are modelled with linear predictive
filtering, and both filters are estimated in an alternating iteration.
Many improvements based on more advanced signal models as well as
machine learning have been proposed, but the question is far from
solved. A central problem in evaluation such methods is the ground
truth. We can estimate curves which look like glottal excitations, but
we would need to know the actual movements of the vocal folds to verify
the accuracy of the obtained curves. Since we do not have a satisfactory
direct method for observing glottal activity, which would not bias
results, we cannot verify our models.

