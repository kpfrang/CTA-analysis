'''
Low level analysis one simtel file. Writes informations to hdf file.

Calibration, image cleaning, hillas parametrization. It does not
include any quality cuts.
'''


from ctapipe.io import event_source					# file reader
from ctapipe.calib.camera import CameraCalibrator   # calibration
from ctapipe.calib.camera.gainselection import pick_gain_channel
from ctapipe.image.cleaning import tailcuts_clean   # image cleaning
from ctapipe.image import hillas_parameters			# hillas parametrization
from ctapipe.io import HDF5TableWriter				# saving to file
from traitlets.config import Config  # configuration handeling

import argparse
import numpy as np
import sys
from datetime import datetime


# Thresholds for gain channel selection
pe_thresh = {
	"ASTRICam": 14,
	"LSTCam": 100,
	"NectarCam": 190}


# Thresholds for tail-cut cleaning for each camera
tail_thresholds = {
		"ASTRICam": (5, 7),
		"FlashCam": (12, 15),
		"LSTCam": (5, 10),
		"NectarCam": (4, 8),
		"DigiCam": (3, 6),
		"CHEC": (2, 4),
		"SCTCam": (1.5, 3)}

# basic quality cuts
quality_cuts = {
		"size": 50}

if __name__ == '__main__':
	start = datetime.now() # check runtime

	parser = argparse.ArgumentParser()
	parser.add_argument("--filepath", type=str, default=None,
						help="file to process")
	parser.add_argument("--outputfile", type=str, default=".",
						help="output directory")
	parser.add_argument("--tels_to_use", type=str, default="all",
						help="telescopes to use")
	parser.add_argument("--integrator", type=str, default=None,
						help="integrator")
	parser.add_argument("--cleaner", type=str, default=None,
						help="cleaner")

	args = parser.parse_args()

	file = args.filepath
	outputfile = args.outputfile
	tels_to_use = args.tels_to_use

	try:
		source = event_source(file)
	except FileNotFoundError:
		print("File {} not found.".format(file))
		sys.exit("exiting...")

	if tels_to_use != "all":
		# list of telescopes to use
		with open("{}".format(tels_to_use)) as f:
			telescope_list = f.read().splitlines()
			telescope_list = np.array(telescope_list, dtype=int)

	print("Telescopes to use: \n{}".format(telescope_list))

	# configuration for calibrator
	cfg_calib = Config()
	cfg_calib["ChargeExtractorFactory"]["product"] = args.integrator
	cfg_calib['WaveformCleanerFactory']['product'] = args.cleaner

	calibrator = CameraCalibrator(
		r1_product="HESSIOR1Calibrator", config=cfg_calib)

	cameras = []

	# writer for output
	with HDF5TableWriter(filename=outputfile,
						 group_name="hillas", overwrite=True) as writer:

		# start main loop
		#################
		for event in source:
			calibrator.calibrate(event) # calibrate event

			# loop over all telescopeswith data in it
			for tel_id in event.r0.tels_with_data: 
				# check if telescope is selected for analysis
				if (tel_id in telescope_list) | (tels_to_use == "all"):
 					pass
				else:
					continue

				camera = event.inst.subarray.tel[tel_id].camera
				image = event.dl1.tel[tel_id].image # in pe

				if not camera.cam_id in cameras:
					cameras.append(camera.cam_id) # all camera types analyzed

				if camera.cam_id in pe_thresh.keys():
					image, select = pick_gain_channel(image,
										pe_thresh[camera.cam_id], True)
				else:
					image = np.squeeze(image)

				# image cleaning
				mask = tailcuts_clean(
					camera, image,
					picture_thresh=tail_thresholds[camera.cam_id][1],
					boundary_thresh=tail_thresholds[camera.cam_id][0])

				if not any(mask):
					# no pixel has survived cleaning
					continue

				cleaned_image = np.copy(image)
				cleaned_image[~mask] = 0 # apply image cleaning
				params = hillas_parameters(camera, cleaned_image)

				if params.intensity < quality_cuts["size"]:
					# telescope didn't survive size cut
					continue

				# write r0, mc and params containers to file
				writer.write(camera.cam_id, [event.r0, event.mc, params])

	# write short summary to log file
	stop = datetime.now()
	duration = stop - start
	print("###################################")
	print(" Succefully analyzed {} events.".format(event.count))
	print(" Duration: {}".format(duration))
	print("###################################\n")
	print("Output written to {} \n".format(outputfile))
	print("Read using pandas.read_hdf('{}', 'hillas/cam_id') \n" \
		  "with cam_id in {}.".format(outputfile, cameras))