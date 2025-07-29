(content:developers)=
# Instructions for Developers

## Getting started

1. Download the source material from [https://github.com/Speech-Interaction-Technology-Aalto-U/itsp](https://github.com/Speech-Interaction-Technology-Aalto-U/itsp). 
2. Install required packages with e.g. 

   ```bash
   pip install jupyter-book   
   ```
   ![]()
3. Many chapters require further packages, which you should install if you plan to compile the whole book (not always required).

    ```bash
    pip install numpy scipy matplotlib ipython ipywidgets jupyterlab
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    pip install itikz
    pip install librosa
    pip install speechbrain
    ```
    ![]()

   Texlive is also needed in some chapters. Observe that speechbrain is picky about the python version and 
    
5. The typical use case is that markdown (.md) and notebooks (.ipynb) are written with [JupyterLab](https://jupyter.org/), which can be started (in the folder of the project) by

    ```bash
    jupyter lab &
    ```
    ![]()

   The easiest way to start is to write static [Markdown files](https://jupyterbook.org/en/stable/file-types/markdown.html#file-types-markdown). This disadvantage is that then you cannot use live code-examples in your document. Upgrading from markdown to notebooks is however easy.
    
6. Once you are reasonably happy with your new content, compile the html-book (in the folder of the project) by

    ```bash
    jupyter-book build .
    ```
    ![]()    
    Verify that the html-book looks like intended - some elements might work slightly differently.
    
    
## Tips and tricks

### Audio

Recording with python/jupyter is a nightmare, but playing audio works like a dream when using [IPython](https://ipython.org/) and [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/). See [Vocoder](content:vocoder) for an example. 

### Interactive elements

Some demonstrations are best when readers get to modify parameters themselves and to observe the output. [IPython](https://ipython.org/) and [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/) allows doing that. Unfortunately, some of the more advanced interactive elements currently require a running jupyter/python kernel (i.e. have to run the notebook on a server).
For an example, check out [Representations/Spectrogram and the STFT](stft).

### Flow graphs and other static visualizations

[Tikz and PGF](https://tikz.dev/) is a combination powerful tool for visualizations inside [LaTeX](https://www.latex-project.org/) documents. These can be incorporated in jupyter notebooks through [itikz](https://pypi.org/project/itikz/). For examples, see [Security and Privacy](../Security_and_privacy.ipynb).

*Tip:* In some scenarios, characters will get messed up when having multiple itikz-elements in a single document. If you're having this issue, please see the solution at the [discussion on Itikz-github](https://github.com/jbn/itikz/issues/28).

### Hidden and removed codeblocks in Jupyter notebooks

Codeblocks can be used as pedagogical elements, but often there also codeblocks which are just to plot stuff, which is not very interesting for a reader. It is then recommended to *hide* the codeblock to avoid visual clutter. A button "*click to show*" button then appears where the reader can see how the backend works. 

An alternative is to *remove* the codeblock from the output entirely. This is best in cases where the codeblock does not have any pedagogic purpose, like when creating flowgraphs with *itikz* (see above). 

Both functions can be achieved with "*tags*" in the jupyter notebook. This can be found by clicking on the "*Property inspector*" logo at the far right side of the jupyter notebook. There it is possible to add either "*hide-input*" or "*remove-input*" for respective functions. For more information see [Jupyter-book/Hide or remove content](https://jupyterbook.org/interactive/hiding.html).

For an example of the use of both hidden and removed codeblocks, see [Enhancement/Noise attenuation](../Enhancement/Noise_attenuation.ipynb).

### References and citations

We use a bibtex based approach stored at [references.bib](../references.bib). For instructions, see e.g. [Jupyter-book/citations and references](https://jupyterbook.org/en/stable/content/citations.html). For an example, see [Computational_models_of_human_language_processing](../Computational_models_of_human_language_processing.md).


### Executing notebooks / MyBinder badge

To allow for the user to run the code in notebooks, there needs to be a jupyter server. Such a server can be installed locally (see [Using this document](Using_this_document.ipynb)), but importantly, there are public servers which can be used as well. The simplest approach is to use [mybinder.org](https://mybinder.org). To make it simple to use, please place a badge on top of the notebook, which directly runs the notebook on the server with the following steps:
1. Find the github url, folder and filename.
2. Enter the above in the form at [mybinder.org](https://mybinder.org).
3. This autogenerates a command to generate the badge; copy that code to the top of your jupyter notebook.
4. Be sure to test it by clicking the badge.
For an example of use, see the page [Noise attenuation](../Enhancement/Noise_attenuation.ipynb).
