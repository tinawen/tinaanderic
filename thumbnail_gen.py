import os, sys
from PIL import Image
from os.path import isfile, join
import argparse

size = (125, 125)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Generate thumbnails for files in directory')
	parser.add_argument('--in_dir', required=True, 
		help='The directory from which we are generating thumbnails')
	parser.add_argument('--out_dir', required=True, 
		help='The directory to where the generated thumbnails go')
	args = parser.parse_args()

	#validate input dir
	if not os.path.isdir(args.in_dir):
		print "Input directory isn't a directory"
		sys.exit()
	else:
		if len(os.listdir(args.in_dir)) == 0:
			print "Input directory is empty. No images to generate thumnails on"
			sys.exit()

	# validate output dir
	if os.path.isdir(args.out_dir):
		if len(os.listdir(args.out_dir)) > 0:
			print "Output directory isn't empty"
			sys.exit()
	else:
		os.makedirs(args.out_dir)

	files = [ f for f in os.listdir(args.in_dir) if isfile(join(args.in_dir, f)) ]
	for index, file in enumerate(files):
		infile = os.path.join(args.in_dir, file)
		if not file.startswith('.') and isfile(infile):
			file_name = os.path.basename(infile)
			outfile_name = os.path.splitext(file_name)[0] + "_thumbnail.jpg"
			outfile = os.path.join(args.out_dir, outfile_name)
			if infile != outfile:
				try: 
					im = Image.open(infile)
					im.thumbnail(size)
					im.save(outfile, "JPEG")
				except IOError:
					print "cannot create thumbnails for ", infile

