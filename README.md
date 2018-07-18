# CTA-analysis

## Starting with ctapipe

Ctapipe will be used for the low-level analysis and event reconstruction of CTA data. It’s not a ready framework yet but heavily under development in order to produce a reliable and stable analysis. This involves the implementation of further methods as well as minor and major changes of existing code. At the current stage, no baseline analysis was released.
The following page should help to give a smoother start working with ctapipe.

### Installation

For installation see https://cta-observatory.github.io/ctapipe/getting_started/index.html. It is recommended to use ctapipe from the conda virtual environment as described in this page to avoid conflicts with other python packages. Afterwards, ctapipe will be usable from within the activated conda environment.

### Low-level Reconstruction

The Ipython Notebook [mono_analysis](Notebooks/mono_analysis.ipynb) gives a step by step example of the low-level (mono) analysis in ctapipe. Analysis tasks considered in this notebook are
- calibration
- image cleaning
- image parametrization
- direction reconstruction (*stereo*)
- writing output to file

From those analysis results, a possible list of features might be extracted for training models for the classification of the primary particle IDs or the primaries’ energies. Further examples of specific tasks can be found within the ctapipe GitHub [repository](https://github.com/cta-observatory/ctapipe/tree/master/examples).

### Submission of jobs to DESY cluster
A basic example of a submission of ctapipe jobs to the DESY cluster is given in [Submit_batch_farm](Examples/Submit_batch_farm). For each simulation file specified in the runlist a job will be specified running the mono analysis and saving the output to HDF files.


### Event reconstruction
*under construction*
- Prediction of energy and primary particle type.