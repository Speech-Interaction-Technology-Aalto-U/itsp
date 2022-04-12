# Computational models of human language processing

One area of research making use of speech technology is the study of
human language learning and processing. Language is a highly complex
phenomenon with physical, biological, psychological, social and cultural
dimensions. Therefore it is also studied across several disciplines,
such as linguistics, neuroscience, psychology, and anthropology. While
many of these fields primarily focus on empirical and theoretical work
on language, computational models and simulations provide another
important aspect to the research: capability to test theoretical models
in practice. Implementation of models capable of processing real speech
data requires techniques from speech processing and machine learning.
For instance, techniques for speech
[signal](Basic_representations_and_models)
[representation](Basic_representations_and_models) and
[pre-processing](Pre-processing) are needed to interface the models with
acoustic speech recordings. Different types of [classifiers and machine
learning algorithms](Modelling_tools_in_speech_processing) are needed to
implement learning mechanisms in the models or to analyze behavior of
the developed models. In addition, model training data may be generated
with [speech synthesizers](Speech_Synthesis) (e.g., Havard, Besacier &
Rosec, 2017), whereas linguistic reference data for model evaluation may
be extracted from speech recordings using [automatic speech
recognition](Speech_Recognition). 

The basic idea of computational modeling is to understand how humans
learn and process language by implementing human-like learning and
speech processing capabilities as computational algorithms. The models
are then exposed to inputs similar to what humans observe, and the model
behavior is then recorded and compared to human data (Fig. 1).
Computational models can focus on questions such as how adult speech
perception operates (e.g., the highly-influential TRACE model of speech
perception; McClelland & Elman, 1986), how language learning takes place
in young children (native language aka. L1 learners; e.g., Räsänen,
2012; Dupoux, 2018) or in second-language (L2) learners, or they may
study the emergence and evolution of language through communicative
coordination between multiple agents (see, e.g., Steels, 1997, or Kirby,
2002, for overviews).

  

  

<img src="attachments/159749086/180302220.png" class="image-center"
data-image-src="attachments/159749086/180302220.png"
data-unresolved-comment-count="0" data-linked-resource-id="180302220"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="basic_modeling_.schematic.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="159749086"
data-linked-resource-container-version="72" width="800" />**Figure 1:**
A high-level schematic view of a typical computational model development
and evaluation process.

### 1.1.1. Human cognition as a sensorimotor information processing system

Computational modeling research is based on the metaphor of human brain
as a computational information processing system. From an external
observer viewpoint, this system perceives the environment using a number
of input channels (senses), processes the information using some type of
processing steps (the nervous system), and creates outputs (motor
actions) based on the available sensory information and other internal
states of the system. This input/output-relationship is affected by
developmental factors and learning from earlier sensorimotor experience,
realized as changes in the connectivity and structure of the central
nervous system. Computational research attempts to understand the
components of this perception-action loop by replacing the human
physiology and neurophysiology with computational algorithms for sensory
(or sensorimotor) information processing. Typically the aim is not to
replicate information processing of the brain at the level of individual
neurons, but to focus on the *computational and algorithmic principles*
of the process, i.e., the *information representation*, *flow* and
*transformation* within the system (see [Marr's levels of
analysis](https://en.wikipedia.org/wiki/David_Marr_(neuroscientist)#Levels_of_analysis);
Marr, 1982). These processing steps could then be implemented in
infinitely many ways using different hardware (biological neurons,
silicon chips architectures, CPU instruction sets, quantum computing
etc.) or translations from computational description to
implementation-specific instructions (consider, e.g., different
programming languages with the same CPU instruction set). Despite the
implementation differences, the observed behavior of the system in terms
of inputs and the resulting outputs can still be similar.

To give an example, a model of adult spoken word recognition could focus
on explaining the acoustic, phonetic and/or other linguistic factors
that affect the process of word recognition. Such a model could focus on
the details of how word recognition process evolves over time when a
spoken word is heard, describing how alternative word candidates are
being considered or rejected during this process (see, e.g., Weber &
Scharenborg, 2012, or Magnuson et al., 2020, for examples). Even if the
model would not focus on modeling neurons of the human brain, it could
still explain how our minds decode linguistic information from speech
input. This explanation could include how the process is affected by
factors such as noisy environments, misprounciations, distributional
characteristics of the input, or non-native language background of the
listener—all useful information to understand both theoretical
underpinnings and practical aspects of speech communication.

Another central aspect of the modeling is the relationship between human
learning and computational methods trying to characterize the process.
According to the present understanding, *human language learning is
largely driven by* the interaction of *statistical regularities in the
sensory input* available to the learner (e.g., Werker & Tees, 1984;
Saffran et al., 1996; Maye et al., 2002; Saffran & Kirkham, 2008),
*innate mechanisms, constraints, and biases for perception and learning*
from such input, and *other mechanisms responsible for social,
communicative and exploratory needs* *o*f the learner. By extracting the
statistical regularities from their sensorimotor linguistic enviroment,
children are capable of learning any of the world's languages while
fundamentally sharing the same basic cognitive mechanisms. A central
topic in computational modeling of language acqusition is therefore to
understand how much of language structure can be learned from the input
data, and how much language-related prior knowledge needs to be built-in
to the hard-coded mechanisms of these models. Note that human
statistical learning is closely related to machine learning in
computers, as both aim to extract statistical regularities from data
using some sort of pre-specified learning principles. However, unlike
standard speech technology systems such as [automatic speech
recognition](Speech_Recognition), humans learners do not have access to
data labels or consistent reward signals. For instance, a computational
model of early infant word learning is essentially trying to find a
solution to unsupervised pattern discovery problem: how to learn words
from acoustic or multimodal input when there is no data labeling
available. By applying a combination of speech processing and machine
learning techniques to data representative of infant language
experiences, explanation proposals for such a process can be created.

#### 1.1.1.1. *Computational modeling versus cognitive computationalism*

Note that computational modeling and *representations* often studied in
the models should not be confused with classical
[computationalism](https://en.wikipedia.org/wiki/Computational_theory_of_mind).
The latter is loaded with certain assumptions regarding the nature of
the entities processed by the computational system (e.g., *content of
the representations, symbols*) and what are the basic computational
operations (e.g., *symbol manipulation* using Turing machines). In
contrast, computational models are simply descriptions of the studied
process in terms of the described assumptions, inputs, outputs, and
processing mechanisms without prescribing further *meaning* to the
components (unless otherwise specified). For instance, *representations*
of typical DSP and machine-learning -based models can simply be treated
as quantifiable states, such as artificial neuron/layer activations,
posterior distributions, neural layer weights, distribution parameters.
In other words, the representations are scalars, vectors, or matrices
that are somehow causally related to the inputs of the system. Behavior
of these representations can then be correlated and compared with
theoretical concepts regarding the phenomenon of interest (e.g.,
comparing selectivity of neural layer activations towards known phoneme
categories in the acoustic input to the model; see, e.g., Nagamine et
al., 2015) or comparing the overall model behavior to human behavior
with similar input (e.g., Räsänen & Rasilo, 2015). As long as the models
are able to explain the data or phenomena of interest, the *models are a
computational and hypothetical explanation* to the phenomenon without
loading the components with additional theoretical or philosophical
assumptions. Additional theoretical loading comes from the *data* and
*evaluation protocols* chosen to investigate the models and in terms of
how the modeling findings are interpreted.

### 1.1.2. Role of computational models in scientific research

Computational modeling has a role in scientific theory development and
hypothesis testing by providing the means to test high-level theories of
language processing with practical simulations (Fig. 2). This supports
the more traditional approaches to language research that include
collection of empirical data on human language processing, conducting
brain research, or running controlled behavioral experiments in the
laboratory or as real-world intervention studies. By implementing
high-level conceptual models of language processing using real
algorithms operating on real-world language data, one can test whether
the models scale up to complexity of real-world sensory data accessible
to human listeners. In addition to explaining already collected data on
human language processing, computational models can also lead to new
insights and hypotheses about the human processing to be tested in
behavioral experiments.

  

<img src="attachments/159749086/180300259.png" class="image-center"
data-image-src="attachments/159749086/180300259.png"
data-unresolved-comment-count="0" data-linked-resource-id="180300259"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="role_of_comp_mods.png"
data-base-url="https://wiki.aalto.fi"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="159749086"
data-linked-resource-container-version="72" width="600" />**Figure 2:**
Different aspects of human language processing research and how they
interact.  
Computational modeling uses data from empirical research to test and
inform high-level theories related to the given topic.

  

One potential advantage of computational modeling is its capability to
address multiple processing mechanisms and language phenomena
simultaneously. This is since *computational models can, and must,
explicitly address all aspects of the information processing chain* from
input data to the resulting behaviour. By first formulating theories of
language processing in terms of computational goals and operations, then
implementing them as functional signal processing and machine learning
algorithms, and finally exposing them to realistic sensory data
comparable to what real humans experience, ecological plausibility and
validity of the underlying theories can be explicitly tested (cf. Marr,
1982). In contrast, behavioral experiments with real humans—although
necessary for the advancement of our scientific understanding and for
general data collection—can usually focus on only one phenomenon at a
time due to the need for highly-controlled experimental setups. The
fragmentation of focus also makes it difficult to combine knowledge from
individual studies into holistic theoretical frameworks (e.g.,
understanding how phonemic, lexical, and syntactic learning are
dependent on each other in early language development). 

### 1.1.3. **Examples of computational modeling research**

***Computational models of child language development***: Computational
models of language learning aim at understanding how human children
learn to perceive and produce their native language. The basic idea is
to simulate the learning of a human child, either starting from "birth"
or from a specific stage of language development. Individual models
typically aim to answer questions such as: how phonemic categories are
learned, how word segmentation is achieved, how spoken words are
associated with their referential meanings, or how syntax can be
acquired? The grand challenge is to understand how the adult-like
understanding of language as a discrete, symbolic, and compositional
system can emerge from the exposure to noisy and inherently continuous
sensorimotor environment. Typical computational modeling research
questions include: 1) *to what extent are languages learnable from the
statistics of sensory experiences*, 2) *what type of learning mechanisms
or constraints are needed for the process*, and 3) *what kind of and how
much data* ("experiences") are required in the process (quality and
quantity of speech, uni- vs. multimodal input etc.). A broader view
takes into account the fact that the children are not just passive
receivers of sensory information but can interact with their caregivers
and their environment as active explorers and learners. Therefore it is
also of interest 4) *what type of additional interaction-related
mechanisms and dynamically created experiences are critica*l. The big
and yet unaswered question is what are the critical ingredients for
successful language learning, as all normally developing children with
very different language experiences, environments, and also somewhat
differing cognitive skills still manage to converge to a shared
communicative system of their native language.  
      As the short-term outcomes, models of language learning can test
and propose different hypotheses for different aspects of language
learning. They also produce functional algorithms for processing
acoustic or multimodal language data in low-resource settings, where
access to data labels is limited (e.g., Kakouros & Räsänen, 2016; Kamper
et al., 2017; Räsänen et al., 2018). Long-term outcomes from language
acquisition modeling contribute to both basic science and practice. In
terms of basic science, the research tries to answer the question of how
one of the most advanced aspects of human cognition, i.e., language,
operates. Long-term practical goals include understanding the impact of
external factors in language development and how to ensure equally
supportive environments for children in different social settings,
understanding different types of language-related disorders and how to
best respond to them, but also how to develop autonomous AI systems
capable of human-like language learning and understanding without
supervised training, i.e.., development of systems ultimately capable of
*understanding the intentions and meaning in communication*.   
     Computational modeling of early language acquisition is closely
related to zero-resource speech processing (see
<http://www.zerospeech.com/>) that aims at algorithms capable of
unsupervised language learning from speech data.

***Models of spoken word recognition**:* Another widely studied topic is
speech perception in adults. Computational models developed for this
purpose attempt to explain how the brain processes incoming speech in
order to recognize words in the input. Models in this area may focus on
explaining the interaction between sub-word and word-level units in
perception, on how words compete with each other during the recognition
process, or, e.g., on how the speech perception is affected by noise in
native and non-native listeners. Since word recognition is essentially a
temporal process, particular attention is typically paid to the
evolution of the recognition process as a function of time (or
proportion of input word or utterance perceived).  
    For an overview, see Weber and Scharenborg (2012). For some examples
of models, see McClelland and Elman (1986), Norris (1994), or Magnuson
et al. (2020).

***Models of speech production**: *This line of research attempts to
explain how human speech production works in terms of articulators and
their motor control. Some studies also focus on the acquisition of
speech production skills. Typical speech production models involve an
articulatory [speech synthesizer](Speech_Synthesis)—an algorithm capable
of producing audible speech signals by modeling the physical
characteristics of the vocal apparatus—and some type of motor control
algorithms that are responsible for phonation and articulator movements.
Sometimes hearing system is simulated as well. These models have various
uses from general understanding of the articulatory basis of speech to
understanding speech pathologies, articulatory learning in childhood or
adulthood, or special types of sound production such as singing.  
    For classical and more recent examples of articulatory models of
speech production, see, e.g., Maeda (1988), Birkholz (2005; in German),
or Birkholz and Martin (2015). For models of infant learning of speech
production, see, e.g., Tourville and Guenther (2011), Howard and Messum
(2014), or Rasilo and Räsänen (2017).

***Multi-agent models of language learning, evolution and
communication:*** Languages are essentially cultural conventions based
on social activity, enabled by genetically coded cognitive and
physiological mechanisms, and learned through interactions between
people. One branch of computational modeling focuses on understanding
how languages emerge, evolve, and are learned through multi-agent
communication and interaction. These simulations, sometimes referred to
as *language games* or *iterated learning* (see Kirby, 2002), focus on
non-linear dynamical systems that result from the interaction of
multiple communicative computational agents. These agents can be purely
based on simulation, or they can be based on physical robots interacting
in a shared  physical environment. By providing the agents with
different types of innate goals, mechanisms, learning skills and
environmental conditions, one can study the extent that language-like
signaling systems (as a social system) or language skills (as subjective
capabilities) can emerge from such conditions.  
    For overviews, see Steels (1997) or Kirby (2002).

### 1.1.4. **References and further reading**

Birkholz, P. (2005). *3D-Artikulatorische Sprachsynthese*. Logos Verlag,
Berlin
\[[pdf](http://www.vocaltractlab.de/publications/birkholz-2005-dissertation.pdf)\]
(in German)

Birkholz, P., & Martin, L. (2015). The contribution of phonatioc type to
the perception of vocal emotions in german: An articulatory synthesis
study. *The Journal of the Acoustical Society of America*, 137,
1503–1512.

Dupoux, E. (2018). Cognitive science in the era of artificial
intelligence: A roadmap for reverse-engineering the infant
language-learner. *Cognition*, 173,
43–59. <a href="https://arxiv.org/abs/1607.08723"
rel="nofollow">https://arxiv.org/abs/1607.08723</a>

Havard, W., Besacier, L., & Rosec, O. (2017). SPEECH-COCO: 600k visually
grounded spoken captions aligned to MSCOCO data set. *Proc.
International Workshop on Grounding Language Understanding (GLU-2017)*,
pp. 42-46, DOI: 10.21437/GLU.2017-9.

Howard, I., & Messum, P. (2014). Learning to pronounce first words in
three languages: an investigation of caregiver and infant behavior using
a computational model of an infant. PLoS ONE, 9,  e110334.
<https://doi.org/10.1371/journal.pone.0110334>

Kakouros S., & Räsänen O. (2016). 3PRO - An unsupervised method for the
automatic detection of sentence prominence in speech. *Speech
Communication*, 82, 67–84.

Kamper, H., Jansen, A., & Goldwater, S. (2017). A segmental framework
for fully-unsupervised large-vocabulary speech recognition. *Computer
Speech & Language*, 46, 154–174.

Kirby, S. (2002). Natural language from artificial life. *Artificial
Life*, 8, 185–215.

Marr, D. (1982). *Vision: A computational approach*. San Francisco,
Freeman & Co.

Magnuson, J., You, H., Luthra, S., Li, M., Nam, H., Escabí, M., Brown,
K., Allopenna, P., Theodore, R., Monto, N., & Rueckl, J. (2020).
EARSHOT: A minimal neural network model of incremental human speech
recognition. *Cognitive Science*, 44, e12823.
<https://doi.org/10.1111/cogs.12823>

McClelland, J., & Elman, J. (1986). The TRACE model of speech
perception. *Cognitive Psychology*, 18, 1–86.

Maeda, S. (1988). Improved articulatory model. *Journal of the
Acoustical Society of America*, 84, Sup. 1, S146.

Maye, J., Werker, J., & Gerken, L. (2002). Infant sensitivity to
distributional information can affect phonetic discrimination.
*Cognition*, 82, B101–111.

Nagamine, T., Seltzer, M. L., & Mesgarani, N. (2015). Exploring how deep
neural networks form phonemic categories. *Proc. Interspeech-2015*,
Dresden, Germany, pp. 1912–1916.

Norris, D. (1994). Shortlist: a connectionist model of continuous speech
recognition. *Cognition*, 52, 189–234.

Oudeyer, P-Y., Kachergis, G., & Schueller, W. (2019). Computational and
robotic models of early language development: a review.
https://arxiv.org/abs/1903.10246 .

Räsänen O. (2012). Computational modeling of phonetic and lexical
learning in early language acquisition: existing models and future
directions. *Speech Communication*, 54, 975–997.

Räsänen, O., & Rasilo, H. (2015). A joint model of word segmentation and
meaning acquisition through cross-situational learning. *Psychological
Review*, 122, 792–829.

Rasilo H., & Räsänen O. (2017). An online model of vowel imitation
learning. *Speech Communication*, 86, 1–23.

Räsänen, O., Doyle, G., & Frank, M. C. (2018). Pre-linguistic
segmentation of speech into syllable-like units. *Cognition*, 171,
130–150.

Saffran, J. R., Aslin, R. N., & Newport, E. L. (1996). Statistical
learning by 8-month-old infants. *Science*, 274, 1926–1928.

Saffran, J. & Kirkham, N. (2018). Infant statistical learning. *Annual
Review of Psychology*, 69, 181–203.

Steels, L. (1997). The synthetic modeling of language origins.
*Evolution of Communication*, 1, 1–34.

Tourville, J.A. and Guenther, F.H. (2011). [The DIVA model: A neural
theory of speech acquisition and
production.](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3650855/)
*Language and Cognitive Processes,* 25, 952—981.

Weber, A. and Scharenborg, O. (2012). Models of processing: lexicon.
*WIREs Cognitive Science*, 3, 387–401. doi: 10.1002/wcs.1178.

Werker, J. F., & Tees, R. C. (1984). Cross-language speech perception:
Evidence from perceptual reorganization during the first year of life.
*Infant Behavior and Development*, 7, 49–63.

Birkholz, P.: VocalTractLab: <http://www.vocaltractlab.de/> \[for work
on articulatory synthesis\]

Dupoux, E. et al.: Zero Resource Speech Challenge:
<http://www.zerospeech.com/> \[a challenge on unsupervised speech
pattern learning\]

  

  

**  
**

  

  

  

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[role_of_comp_mods.png](attachments/159749086/180300259.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[basic_modeling\_.schematic.png](attachments/159749086/180302220.png)
(image/png)  

</div>
