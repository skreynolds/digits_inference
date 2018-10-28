#! /usr/bin/env python3

import glob
from PIL import Image

def resize_image(input_image_path, output_image_path, size):

	# open image and store object
	original_image = Image.open(input_image_path)

	# store image dimensions
	width, height = original_image.size

	# print to terminal the size of the current image
	print('The original image size is {wide} wide x {height} '
			'high'.format(wide=width, height=height))

	# resize the image to the desired size
	resized_image = original_image.resize(size)

	# store new dimensions of resized image
	width, height = resized_image.size

	print('The resized image size is {wide} x {height} '
			'high'.format(wide=width, height=height))

	resized_image.save(output_image_path)


if __name__ == '__main__':

	###########################################
	# TEST IMAGE
	###########################################
	'''
	input_image_path = './test_image.jpg'
	output_image_path = './output_test_image.jpg'
	'''
	###########################################
	
	###########################################
	# RESIZE IMAGE
	###########################################

	# capture all of the file paths for each image
	#file_paths = glob.glob('./image_data/dirty_solar_panel/*')	# dirty solar panels
	#file_paths = glob.glob('./image_data/dusty_solar_panel/*')	# dusty solar panels
	#file_paths = glob.glob('./image_data/roof/*')	# roof
	file_paths = glob.glob('./image_data/rooftops/*')	# rooftops
	#file_paths = glob.glob('./image_data/solar_panel/*') 	# solar panels
	
	# set the size that we want to readjust the image to
	size = (256,256)

	# resize every image in a set file path
	for counter, path in enumerate(file_paths):
		
		# set the input file path
		input_image_path = path

		# set the output path
		#output_image_path = './image_data/dirty_solar_panel_resized/img_' + str(counter) + '.png'		# dirty solar panels
		#output_image_path = './image_data/dusty_solar_panel_resized/img_' + str(counter) + '.png'		# dusty solar panels
		#output_image_path = './image_data/roof_resized/img_' + str(counter) + '.png'		# roof
		output_image_path = './image_data/rooftops_resized/img_' + str(counter) + '.png'		# rooftops
		#output_image_path = './image_data/solar_panel_resized/img_' + str(counter) + '.png'	# solar panels
		
		# resize image
		try:
			resize_image(input_image_path, output_image_path, size)
		except Exception as err_msg:
			print(err_msg)

