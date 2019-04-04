#image processing using pillow package in python 

from PIL import Image
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-l', '--leftimage',help="path to left image", required=True)
ap.add_argument('-r', '--rightimage', help="path to right image", required=True)
ap.add_argument('-o', '--output', help="coordinates", required=True)
box=(0,400,400,400)
args =vars(ap.parse_args())

overlay = Image.open(args['leftimage'])
background = Image.open(args['rightimage'])
background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

background.paste(overlay, (int(args['output']),0), overlay)
background.show()
