#!/bin/python
import os
import sys

def print_help():
    print("Name the extension you want. (last 3 letters of the image.png)")
    print("                                                          ^^^")
    print("example usage: image_converter jpg # converts the images to jpg")

# get the extension from first argument, else default to png
try:
    if sys.argv[1]:
        mode = sys.argv[1]

    else:
        mode = "png"

except IndexError:
    mode = "png"

if mode == "help":
    print_help()
    exit()

directory = f"{os.getcwd()}/"
items = os.listdir(directory)
pictures = []

for item in items:
    if item[-3:] in ["jpg", "png"]:
        pictures.append(item)

os.system("mkdir -p converted")

print(pictures)

for picture in pictures:
    print(f"Converting {picture}")
    os.system(f'ffmpeg -i "{directory + picture}" "{directory + "converted/" + picture[:-3]}{mode}"')

print("Converted pictures. Check the converted folder.")
