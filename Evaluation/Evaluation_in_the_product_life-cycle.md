(content:evaluationlifecycle)=
# Evaluation in the product life-cycle

There is no single "right" way to evaluate a speech processing method. The best choice depends on where we are in the life-cycle of a product. Early in development, we need answers within minutes, so we accept tests that are rough and biased. Before a product goes to market, we need results that we can trust, so we accept tests that are slow and expensive. After the product is in use, we need to keep watching that it still works.

Evaluation therefore changes along the way, from fast, cheap and biased tests, to slow, costly tests that are close to real users. The figure and table below give an overview. The sections after them describe each stage. The overall workflow of a project is described in [Design of experiments and projects](#content:design). Here we focus on how evaluation changes between its stages.

```{figure} attachments/evaluation_lifecycle.svg
:name: fig:evaluationlifecycle

Evaluation over the life-cycle of a product. The blue bars are *gates*: milestones where we decide whether to continue. The size of each dot shows the scale of the test, that is, the number of listeners or the amount of data.
```

| Stage | Purpose | Subjective evaluation | Objective evaluation | Feedback time | Statistics |
|---|---|---|---|---|---|
| Algorithm development | Find what works, catch bugs | Informal listening by the developer: 1 expert, few sounds | Metrics on a development set: cheap and repeatable, but biased | Minutes to hours | Possible for metrics; none for listening |
| **Gate: algorithm milestone** | Decide whether the idea is worth pursuing | Small expert test (e.g. MUSHRA with about 6–10 colleagues), small set of sounds | Metrics on a held-out test set | Days | Reasonable |
| Product development | Track progress, catch regressions | Rarely | Automatic periodic (e.g. nightly) tests | Overnight | Confidence tests recommended |
| **Gate: product milestone** (market, standard) | Show quality to users or a standards body | Large test with naïve listeners (e.g. P.800), in a lab or crowdsourced; more sounds | Large-scale metrics | Weeks | Essential |
| Monitoring after deployment | Catch faults; follow changing user needs | Periodic tests, user feedback | Continuous or periodic small tests, often without a reference signal | Continuous | Detect trends and changes |

Why have so many steps? Because a problem found late costs much more to fix than one found early. A bug caught by the developer's own ears costs a few minutes. The same bug found in a large listening test costs weeks and the price of the test. Found by customers, it can cost the product. The cheap tests early on exist so that the expensive tests at the gates rarely fail.

## Before development: set the requirements

Evaluation starts before the first line of code. When we [specify a project](#content:design), we should decide

- the target quality, for example "at least as good as the current product",
- the references to compare against, such as the current version or competing products,
- the test design and metrics for each gate, and
- the pass criteria for each gate.

Fixing these in advance avoids a common trap: once we see the results, it is tempting to pick the test or metric that makes our method look best. Deciding beforehand keeps the evaluation honest.

## Algorithm development

While developing an algorithm, we need fast feedback, so that we can try an idea, see the result, and try again.

- **Informal listening.** The developer listens to the output. This is the fastest feedback there is, and it catches a large share of bugs, since programming errors often cause loud and obvious distortions. However, it uses only one listener, who is an expert and also biased: the developer knows exactly what to listen for and wants the method to work. Only a few sounds can be checked, and there is no statistical validation.
- **[Objective metrics](#content:objectiveevaluation).** Metrics such as PESQ, STOI or the word error rate can be computed automatically. They are cheap and repeatable, and we can apply [statistical tests](#content:analysisofresults) to them. How fast they give feedback depends on the size of the dataset. However, they only *approximate* what listeners would say, so they are biased in their own way.

## Gate: algorithm milestone

At the end of algorithm development, we decide whether the method is good enough to build a product on. The evidence should now be more reliable than one person's opinion.

- **Small expert listening test.** Colleagues act as expert listeners, for example in a [MUSHRA](#content:subjectiveevaluation) test with about 6–10 listeners. With expert listeners, statistical validation is reasonable even with this small number. The test takes a few days, and it still uses a small set of sounds.
- **Objective metrics.** These are the low-hanging fruit: we already have them from development, so it is easy to include them. They should now be computed on a *held-out* test set, that is, data that was not used during development. Statistical validation is reasonable, and the results come quickly.

## Product development

During product development, the algorithm is turned into a product: optimised, integrated with other parts, and ported to its target platform. The main risk is now that changes break something that used to work.

- **Periodic objective tests.** Automatic tests, run for example every night, track progress and catch bugs (*regression tests*). Statistical confidence tests help to tell real changes from random variation.
- **Subjective tests** are rarely needed in this stage, unless a change is expected to affect quality.

## Gate: product milestone

Before the product goes to market, or before a method is accepted into a standard, we need the strongest evidence.

- **Large subjective test with naïve listeners.** Naïve listeners, for example in a [P.800](#content:subjectiveevaluation) test, match the intended users, so the results are not biased by expert hearing. On the other hand, naïve listeners are untrained, so their ratings vary a lot. We therefore need many listeners and a larger set of sounds, and statistical confidence tests are very important.
- **Crowdsourced tests.** Instead of a listening lab, tests can be run online with listeners recruited through a crowdsourcing platform. ITU-T Recommendation [P.808](https://www.itu.int/rec/T-REC-P.808) describes how to do this {cite}`naderi2020p808`. Crowdsourced tests are cheaper and faster than lab tests, but noisier, because we cannot control the listeners' equipment or surroundings. They suit this gate and also periodic monitoring.
- **Large-scale objective metrics** on a large test set. Here too, statistical confidence tests are very important.
- **Tests on real devices.** For a phone or a headset, the sound also depends on the microphones, loudspeakers and the acoustics of the device. Standards such as 3GPP TS 26.131 and TS 26.132 define requirements and test methods for the acoustics of mobile terminals.
- **Conformance tests.** For a standardised method, such as a speech codec, every implementation must give the same result. Standards therefore come with fixed *test vectors*: input files and the exact outputs that a correct implementation must produce.

## Monitoring after deployment

After the product is in use, evaluation continues.

- **Continuous or periodic small objective tests** catch problems such as software bugs, failing hardware or changes in the network.
- **No reference signal.** In the field, we usually do not have the clean original signal, only the output. We then need *non-intrusive* (also called *no-reference* or *single-ended*) metrics, which estimate quality from the output alone. Examples are ITU-T P.563 {cite}`malfait2006p563`, DNSMOS {cite}`reddy2021dnsmos` and NISQA {cite}`mittag2021nisqa`.
- **User feedback.** Some services ask users to rate their experience, for example "How was the call quality?" after a call. Such ratings are noisy, but they come from real users in real situations.
- **A/B tests.** Two versions of the product are given to different groups of users, and their ratings or behaviour are compared. This shows how a change works in real use.
- **Periodic subjective tests** show how user preferences and needs change over time. What sounded good ten years ago may not be good enough today. These findings feed back into new ideas for development.
- **Privacy.** We usually cannot record users' speech to evaluate it. Monitoring must then run on the user's device, be based on the user's consent, or use only data that does not contain speech, such as packet-loss statistics. See [Security and privacy](#privacy).

## Things to watch at every stage

### Overfitting to the metric

If developers tune a method against one objective metric for months, the method can learn to please the metric instead of the listener. This is known as *Goodhart's law*: when a measure becomes a target, it stops being a good measure {cite}`goodhart1984problems,strathern1997improving`. The same happens if a metric is used as the loss function when training a neural network. That metric can then no longer be used to evaluate the network.

To reduce this risk,

- keep a held-out test set that is not used during development,
- use more than one metric, and
- check the metrics against listening tests at each gate (see below).

### Check that metrics still agree with listeners

An objective metric is only useful if it agrees with what listeners hear. Metrics are designed and tested for certain types of distortion, and they can fail for others. For example, PESQ was not designed for distortions caused by processing in the spectral domain, and classical metrics can give misleading results for the sounds produced by neural codecs and generative models {cite}`manocha2022audio`. At each gate, we should therefore use the results of the subjective test to check that the objective metrics still follow the listeners' ratings.

### Coverage of the test material

A test is only as good as the sounds that are in it. A method that works well for adult speakers of one language in a quiet room may fail for children, for other languages or accents, for unusual voices, or in noisy places. Larger tests, in particular at the product gate, should cover all the intended user groups and conditions of use. This is also a question of fairness: a product should work equally well for everyone who uses it. See also [Speech data](#content:data).

### Other performance measures

[Other performance measures](#content:otherperformance), such as computational complexity, memory use and latency, follow the same path. During development, they are estimated, for example by counting operations (WMOPS). At the product gate, they are measured on the target hardware.
