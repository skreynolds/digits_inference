#! /usr/bin/env python

import glob
from PIL import Image

def flip_image(input_path, output_path):

	# open the image and store it
	image_original = Image.open(input_path)

	image_flipped = image_original.transpose(Image.FLIP_LEFT_RIGHT)

	image_flipped.save(output_path)


if __name__ == '__main__':

	
	################################################
	# TEST IMAGE FLIP
	################################################
	'''
	input_path = './output_test_image.jpg'

	output_path = './output_test_image_flipped.jpg'

	flip_image(input_path, output_path)
	'''
	################################################
	
	# create a list of file that need to be flipped
	#file_paths = glob.glob('./image_data/dirty_solar_panel_resized/*')
	#file_paths = glob.glob('./image_data/dusty_solar_panel_resized/*')
	#file_paths = glob.glob('./image_data/roof_resized/*')
	#file_paths = glob.glob('./image_data/rooftops_resized/*')
	file_paths = glob.glob('./image_data/solar_panel_resized/*')

	for counter, path in enumerate(file_paths):

		# set input file path
		input_path = path

		# set output file path
		#output_path = './image_data/dirty_solar_panel_resized_flipped/' + str(counter) + '.png'
		#output_path = './image_data/dusty_solar_panel_resized_flipped/' + str(counter) + '.png'
		#output_path = './image_data/roof_resized_flipped/' + str(counter) + '.png'
		#output_path = './image_data/rooftops_resized_flipped/' + str(counter) + '.png'
		output_path = './image_data/solar_panel_resized_flipped/' + str(counter) + '.png'

		# flip image
		flip_image(input_path, output_path)