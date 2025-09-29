# Image Pixelator

This is a Python script to pixelate images in a specified folder using the Pillow (PIL) library. It processes images in parallel using multiprocessing for efficiency.

## Features
- Pixelate images by resizing them to a smaller grid and back up.
- Supports PNG, JPG, and JPEG formats.
- Multi-processing to utilize multiple CPU cores.
- Automatically creates the output folder if it doesn't exist.

## Requirements
- Python 3.x
- Pillow (pip install pillow)

## Usage
Run the script from the command line:

```bash
python pixelate_images.py --input_folder path/to/input --output_folder path/to/output --pixel_size 16
