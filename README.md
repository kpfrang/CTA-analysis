# CTA-analysis

## Starting with ctapipe

Ctapipe will be used for the low-level analysis and event reconstruction of CTA data. It’s not a ready framework yet but heavily under development in order to produce a reliable and stable analysis. This involves the implementation of further methods as well as minor and major changes of existing code. At the current stage, no baseline analysis was released.
The following page should help to give a smoother start working with ctapipe. 

### Installation

For installation see https://cta-observatory.github.io/ctapipe/getting_started/index.html. It is recommended to use ctapipe from the conda virtual environment as described in this page to avoid conflicts with other python packages. Afterwards, ctapipe will be usable from within the activated conda environment.

### Low-level Reconstruction

The Ipython Notebook [mono_analysis](Notebooks/mono_analysis.ipynb) gives a step by step example of the low-level analysis in ctapipe. Analysis tasks considered in this notebook are
- calibration
- image cleaning
- image parametrization
- direction reconstruction
- writing output to file

From those analysis results, a possible list of features might be extracted for training models for the classification of the primary particle IDs or the primaries’ energies. Further examples for specific tasks can be found within the ctapipe GitHub [repository](https://github.com/cta-observatory/ctapipe/tree/master/examples).

### Submitting jobs to the batch farm

The submission of the analysis jobs to the batch farm is done using qsub. In the following an exemplary analysis performing the low-level analysis until the Hillas parametrization is given. The results along with Monte Carlo information will be written to an HDF file which might be read using pandas or pytables.

The jobs are submitted using the python interface submit.py. A list of the options is given when executing it with the -h option. The MC files to analyze are specified in the run lists where each column represents the path to one simulation file. The telescope configuration is given by the tels_to_use option, which should direct to a file which contains one telescope ID per line. The directory for writing the log-files and output files is given with the odir option. For each run in the run lists, it will submit one job.
To activate the ctapipe conda environment the qsub_file.sh is called first. This file might need minor adaptions in case the environment was named differently than the default cta-dev. Furthermore, it starts analyse_file.py which performs the analysis of the files and writes the results to the output files. This file provides a basic analysis chain.