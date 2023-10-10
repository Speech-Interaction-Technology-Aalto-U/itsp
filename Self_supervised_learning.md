# Self-supervised learning

Self-supervised learning (SSL) refers to a family of machine learning algorithms that are used  to learn useful signal representations from data without any supporting information, such as task-specific data labels. Instead of extracting manually specified signal features, such as MFCCs (see REF), SSL algorithms *learn the features* by taking statistical properties of the input data into acocunt.  The word *useful* refers to signal representations that can act as informative features in a downstream task or a variety of tasks. Alternatively, a pre-trained SSL model can be used as a starting point for model development for a downstream task, such as augmenting the SSL model with a classification layer (or layers) and then fine-tuning the model to a particular speech processing task of interest. 

In general, SSL algorithms belong to the family of unsupervised learning algorithms and they are practically implemented as deep neural networks. The reason they are referred to as *self-supervised* comes from the optimization criterion used to train the models. Classical unsupervised learning operates by performing unsupervised data clustering using a heuristic algorithm (as in k-means) or by modeling the data distribution directly with a generative model (as in Gaussian mixture models, hidden-Markov models, or autoencoders). SSL algorithms, on the other hand, can be viewed as regression models (or classifiers) that try to perform regression from the input data to representations derived from the same input data. For instance, in case of speech data, one such a regression task is to predict the spectral envelope of future speech observations, given access to a series of past observations up to present time. When a deep neural network is tasked with this prediction problem and optimized to solve it, the network has to learn higher-level properties of the data in order to solve the problem adequately. Note  that the task has to be difficult enough, so that it cannot be solved by trivial means (e.g., linear interpolation from the observed values). Fig. X illustrates a self-supervised speech prediction task, as it is implemented in Autoregressive Predictive Coding (APC) algorithm (REF).   

![APC basic schematic](attachments/SSL/APC_schematic.pdf)

**Figure 1:** A schematic view of APC model for self-supervised learning. Speech signal is first represented by log-Mel spectral envelope features **y**(t). APC encoder, usually implemented as a multilayer perceptron (MLP), processes each spectral frame one-by-one and transforms them into latent representations **z**(t). The history of **z**(t) values up to present time $t_0$ is processed by a context model (e.g., a RNN, Transformer or CNN), producing a context embedding **c**($t_0$). The context embedding is then projected linearly to produce a prediction  **y***(${t_0}+k$) of a future log-Mel frame **y**(${t_0}+k$) at the given prediction distance *k*. Mean absolute error between the predicted and true future frame is then used as the loss function, and minimized during training. After the training, latent vectors **z**(t) or context vectors **c**(t) can be used as inputs to a downstream task.


The advantage of SSL methods is that they do not require labeled data to operate, which allows their training on much larger datasets than what is typically available for a speech processing problem. For instance, there may only be a few hours of representative speech data with emotion labels to train a speech emotion classifier for a specific language, but there might be thousands of hours of unlabeled data available in the same language. By first learning the general characteristics of the speech in that particular language with SSL, and then using the SSL model or its features as the starting point for an emotion classifier, much more powerful models can be developed. In practice, SSL pre-training has turned out to be so useful that a large proportion of modern speech applications, such as automatic speech recognition, nowadays make use of it as an integral part of system development (ref).

## Two basic types of SSL models for speech
 
- Prediction: APC and CPC.
- Masking: Wav2Vec2.0.

## Combining SSL with downstream tasks

Once an SSL model is trained in a self-supervised manner without data labels,  ... SUPERB ref.

## References

APC
Wav2Vec2.0
HuBERT
CPC
Data2Vec2.0

