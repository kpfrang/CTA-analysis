# Notebooks

This directory contains ipython notebooks with step by step explanations for the ctapipe analysis.

### Ipython Notebook

Anaconda comes with jupyter notebook. For a introduction to Ipython Notebooks see the [documentation](http://jupyter-notebook.readthedocs.io/en/stable/notebook.html#).

To start a jupyter notebook brows to a directory and execute `jupyter notebook` from a terminal. The dashboard will pop up showing the notebooks available in this directory. They can be opend by clicking their name or creating a new one with *New -> Python 3*. The complete notebook can be executed using *Cell -> Run All* or a single cell with the Keyboard shortcuts `Control + Enter`.

If you have created a conda environment and want to use `ctapipe` within the notebook, you need to activate the environment in your shell before starting the jupyter notebook

`source activate cta-dev`


### Short description

- [mono_analysis](mono_analysis.ipynb): Low-level reconstructions. Focus on the mono analysis and direction reconstruction of events.<br><br>
**_Important_:** To run this Notebook, you need to have at least one smitel file available. If you working locally you could use scp <br><br>
`scp <usrname>@warp-zeuthen.desy.de:/lustre/fs21/group/cta/prod3b/prod3b-paranal20deg/gamma_onSource/gamma_20deg_180deg_run1___cta-prod3_desert-2150m-Paranal-merged.simtel.gz ~/simtel_files`

- [coordinate transformations and array plotting](coordinates.ipynb): Example of demonstrating how to converte between different coordinate transformations. Additionally it shows an example of how to run produce a plot of the array layout. At the same time, a selection of a subarray is performed and the resulting Hillas parameters are plotted into the layout as well.

- *Under construction*: Notebook demonstrating the use of the classifier and energy regressor.