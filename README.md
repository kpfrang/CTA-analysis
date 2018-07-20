# CTA-analysis

## Starting with ctapipe

`ctapipe` will be used for the low-level analysis and event reconstruction of CTA data. It’s not a ready framework yet but heavily under development in order to produce a reliable and stable analysis. This involves the implementation of further methods as well as minor and major changes of existing code. At the current stage, no baseline analysis was released.
The following page should help to give a smoother start working with ctapipe.

### Installation

For installation see https://cta-observatory.github.io/ctapipe/getting_started/index.html. It is recommended to use ctapipe from the conda virtual environment as described in this page to avoid conflicts with other python packages. Afterwards, ctapipe will be usable from within the activated conda environment.

The scripts in this repository assume a conda environment called `cta-dev`, as well as the anaconda python added to the path in your `~/.zshrc`.

#### Troubleshooting

- It happend that when installing `pyhessio` (python module for reading the simtel files) on warp the following error message appears when trying to import into python or running pytest from the ctapipe repository.  <br><br>
```E   OSError: /lib64/libc.so.6: version `GLIBC_2.14' not found (required by /lustre/fs19/group/cta/users/kpfrang/anaconda3/envs/cta-dev/lib/python3.6/site-packages/pyhessio/pyhessioc.cpython-36m-x86_64-linux-gnu.so)```  <br><br>
See also this [issue](https://github.com/cta-observatory/pyhessio/issues/65). I have been able to work around this by removing `pyhessio` from the activated environment `conda remove pyhessio` and building it from source `python setup.py develop`.

***

### Notebooks

#### Low-level Reconstruction

The Ipython Notebook [mono_analysis](Notebooks/mono_analysis.ipynb) gives a step by step example of the low-level (mono) analysis in ctapipe. Analysis tasks considered in this notebook are
- calibration
- image cleaning
- image parametrization
- direction reconstruction (*stereo*)
- writing output to file

From those analysis results, a possible list of features might be extracted for training models for the classification of the primary particle IDs or the primaries’ energies. Further examples of specific tasks can be found within the ctapipe GitHub [repository](https://github.com/cta-observatory/ctapipe/tree/master/examples). An basic example of a low level analysis chain can be found in the Notebook and [analyse_file.py](Examples/Submit_batch_farm/analyse_file.py)

***

### Examples

#### Runlists and Arrays
- Template runlists with one line file stored on lustre per line
- Template array configuration. Each line represents one telescope ID

#### Submission of jobs to DESY cluster
A basic example of a submission of ctapipe jobs to the DESY cluster is given in [Submit_batch_farm](Examples/Submit_batch_farm). For each simulation file specified in the runlist a job will be submitted running the mono analysis and saving the output to HDF files.

***

### Under construction

#### Event reconstruction
- Prediction of energy and primary particle type
