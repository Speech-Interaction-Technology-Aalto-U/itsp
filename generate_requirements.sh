#!/bin/bash

#conda install pipreqs nbconvert
jupyter nbconvert --output-dir="./reqs" --to script *.ipynb */*.ipynb */*.py
cd reqs
rm requirements.txt
pipreqs
cd ..
#mv reqs/requirements.txt .
