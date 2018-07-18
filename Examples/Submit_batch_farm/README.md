# Submitting jobs to the DESY batch farm

This example demonstrates how to submit a list (or optional two) of runs to the batch farm. For each event in the Monte Carlo file, the low-level analysis will be performed using ctapipe and the resulting Hillas parameters and the MC information will be written to an HDF file.

### Submission of events

The submission is performed using [submit.py](submit.py). It takes one or two run lists as input which will be read. For each file in the run lists, one job will be submitted using qsub. It is called by

`python submit.py --listGAMMA runlist1 --listPROTON runlist2 --odir output_directory --tels_to_use telescope_list`

The parameter `--odir` specifies the output directory. The telescope configuration to use for the analysis is given by `--tels_to_use`. It should be either `all` or the path to a list of telescope_ids with one ID per line.

After extracting parameters like runnumber, zenith angle etc, the [qsub_file.sh](qsub_file.sh) is called. It sets the correct environment variables by sourcing `$HOME/.zshrc` and activating the conda environment `cta-dev`. Sourcing `.zshrc` should ensure that the correct python version is used. Therefore it should add your anaconda installation to the `PATH`. In case of different naming or an installation without the virtual environment, this might need minor adaptions in order to run for you.

With the correct environment [analyse_file.py](analyse_file.py) is started which performs the low-level reconstruction. For details of the single steps see this [Notebook](../../Notebooks/mono_analysis.ipynb) or the ctapipe [repository](https://github.com/cta-observatory/ctapipe). The output will be written to h5 files in the `odir` directory and might be read back in using `pandas.read_hdf()` (see the LOG files).

##### List of tasks covered in analysis
- Read file
- Select telescopes
- Calibration
- Image cleaning
- Hillas parametrization
- Size cut
- Save result to HDF file