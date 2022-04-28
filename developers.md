# Instructions for Developers

## Getting started

1. Download the source material from [https://gitlab.com/speech-interaction-technology-aalto-university/itsp](https://gitlab.com/speech-interaction-technology-aalto-university/itsp). 
2. Install required packages with e.g. [conda/anaconda](https://www.anaconda.com/products/distribution)

   ```bash
   conda install jupyter-book   
   ```
   ![]()
3. Many chapters require further packages, which you should install if you plan to compile the whole book (not always required).

    ```bash
    conda install numpy scipy matplotlib ipython ipywidgets jupyterlab   
    pip install itikz
    ```
    ![]()
    
4. The typical use case is that markdown and notebooks are written with [JupyterLab](https://jupyter.org/), which can be started (in the folder of the project) by

    ```bash
    jupyter lab &
    ```
    ![]()
    
5. Once you are reasonably happy with your new content, compile the html-book (in the folder of the project) by

    ```bash
    jupyter-book build .
    ```
    ![]()    
    Verify that the html-book looks like intended - some elements might work slightly differently.
    
    
## Tips and tricks

### Audio

Recording with python/jupyter is a nightmare, but playing audio works like a dream when using [IPython](https://ipython.org/) and [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/). See [Enhancement/Noise attenuation](Enhancement/Noise_attenuation.ipynb) for an example. 

### Interactive elements

Some demonstrations are best when readers get to modify parameters themselves and to observe the output. [IPython](https://ipython.org/) and [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/) allows doing that. Unfortunately, some of the more advanced interactive elements currently require a running jupyter/python kernel (i.e. have to run the notebook on a server).
For an example, check out [Representations/Spectrogram and the STFT](Representations/Spectrogram_and_the_STFT.ipynb).

### Flow graphs and other static visualizations

[Tikz and PGF](https://tikz.dev/) is a combination powerful tool for visualizations inside [LaTeX](https://www.latex-project.org/) documents. These can be incorporated in jupyter notebooks through [itikz](https://pypi.org/project/itikz/). For examples, see [Security and Privacy](Security_and_privacy.ipynb).

### Hidden and removed codeblocks in Jupyter notebooks

Codeblocks can be used as pedagogical elements, but often there also codeblocks which are just to plot stuff, which is not very interesting for a reader. It is then recommended to *hide* the codeblock to avoid visual clutter. A button "*click to show*" button then appears where the reader can see how the backend works. 

An alternative is to *remove* the codeblock from the output entirely. This is best in cases where the codeblock does not have any pedagogic purpose, like when creating flowgraphs with *itikz* (see above). 

Both functions can be achieved with "*tags*" in the jupyter notebook. This can be found by clicking on the "*Property inspector*" logo at the far right side of the jupyter notebook. There it is possible to add either "*hide-input*" or "*remove-input*" for respective functions. For more information see [Jupyter-book/Hide or remove content](https://jupyterbook.org/interactive/hiding.html).

For an example of the use of both hidden and removed codeblocks, see [Enhancement/Noise attenuation](Enhancement/Noise_attenuation.ipynb).

### References and citations

We use a bibtex based approach stored at [references.bib](references.bib). For instructions, see e.g. [Jupyter-book/citations and references](https://jupyterbook.org/en/stable/content/citations.html). For an example, see [Computational_models_of_human_language_processing](Computational_models_of_human_language_processing.md).