#! /usr/bin/env python

import glob
import shutil

if __name__ == '__main__':

	# consolidate files - dirty solar panels
	'''
	file_paths = (glob.glob('./image_data/dirty_solar_panel_resized/*')
					+ glob.glob('./image_data/dirty_solar_panel_resized_flipped/*')
					+ glob.glob('./image_data/dusty_solar_panel_resized/*')
					+ glob.glob('./image_data/dusty_solar_panel_resized_flipped/*'))
	'''

	# non-solar panels
	'''
	file_paths = (glob.glob('./image_data/roof_resized/*')
					+ glob.glob('./image_data/roof_resized_flipped/*')
					+ glob.glob('./rooftops_resized/*')
					+ glob.glob('./rooftops_resized_flipped/*'))
	
	'''
	# clean solar panels
	
	file_paths = (glob.glob('./image_data/solar_panel_resized/*')
					+ glob.glob('./image_data/solar_panel_resized_flipped/*'))
	

	for counter, path in enumerate(file_paths):

		input_path = path

		#output_path = './image_data_final/solar_dirty/' + str(counter) + '_image.png'
		#output_path = './image_data_final/solar_none/' + str(counter) + '_image.png'
		output_path = './image_data_final/solar_clean/' + str(counter) + '_image.png'

		shutil.copy(input_path, output_path)