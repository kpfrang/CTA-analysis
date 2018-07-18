# Notebooks

This directory contains ipython notebooks with step by step explanations for the ctapipe analysis.

### Ipython Notebook

Anaconda comes with jupyter notebook. For a introduction to Ipython Notebooks see the [documentation](http://jupyter-notebook.readthedocs.io/en/stable/notebook.html#).

To start a jupyter notebook brows to a directory and execute `jupyter notebook` from a terminal. The dashboard will pop up showing the notebooks available in this directory. They can be opend by clicking their name or creating a new one with *New -> Python 3*. The complete notebook can be executed using *Cell -> Run All* or a single cell with the Keyboard shortcuts `Control + Enter`.


### Short description
If you have created a conda environment, you need to activate it before starting jupyter notebook.  
`source activate cta-dev`

- [mono_analysis](mono_analysis.ipynb): Low-level reconstructions. Focus on the mono analysis and direction reconstruction of events.  
<span style="color:red">**Important:**</span> To run this Notebook, you need to have at least one smitel file available. If you working locally you could use scp

`scp <usrname>@warp-zeuthen.desy.de:/lustre/fs21/group/cta/prod3b/prod3b-paranal20deg/gamma_onSource/
gamma_20deg_180deg_run1___cta-prod3_desert-2150m-Paranal-merged.simtel.gz ~/simtel_files`

- *Unter construction*: Notebook demonstrating the use of the classifier and energy regressor.