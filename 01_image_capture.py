#!/usr/bin/env python3

from google_images_download import google_images_download

if __name__ == '__main__':

	response = google_images_download.googleimagesdownload()

	arguements = {"keywords":"clean solar panels", "limit":100, "print_urls":True}

	paths = response.download(arguements)

	print(paths)