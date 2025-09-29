
### pixelate_images.py
```python
import argparse
from PIL import Image
import os
from multiprocessing import Pool, cpu_count

def pixelate_image(args):
    filename, input_folder, output_folder, pixel_size = args
    supported_extensions = (".png", ".jpg", ".jpeg")
    if filename.lower().endswith(supported_extensions):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"pixel_{filename}")
        
        try:
            # Open image
            img = Image.open(input_path)
            # Apply pixelation
            small_img = img.resize((img.width // pixel_size, img.height // pixel_size), Image.NEAREST)
            pixelated_img = small_img.resize((small_img.width * pixel_size, small_img.height * pixel_size), Image.NEAREST)
            # Save result
            pixelated_img.save(output_path)
            print(f"Processed: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Pixelate images in a folder using multiprocessing.")
    parser.add_argument('--input_folder', required=True, help='Path to the input folder containing images')
    parser.add_argument('--output_folder', required=True, help='Path to the output folder for pixelated images')
    parser.add_argument('--pixel_size', type=int, default=16, help='Pixelation factor (default: 16)')

    args = parser.parse_args()

    # Create output folder if it doesn't exist
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    # Get list of supported files
    supported_extensions = (".png", ".jpg", ".jpeg")
    files = [f for f in os.listdir(args.input_folder) if f.lower().endswith(supported_extensions)]

    # Prepare arguments for multiprocessing
    process_args = [(f, args.input_folder, args.output_folder, args.pixel_size) for f in files]

    # Use multiprocessing pool
    num_processes = cpu_count()
    with Pool(processes=num_processes) as pool:
        pool.map(pixelate_image, process_args)

    print(f"All images processed! Output folder: {args.output_folder}")

if __name__ == '__main__':
    main()
