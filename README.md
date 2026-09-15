# RLE Image Decompression

This project implements run-length encoding (RLE) decompression for a binary silhouette image.

The program:
- reads RLE data from a binary file,
- reconstructs the image using column-major order,
- displays the decompressed image,
- compares storage size for 32-bit and 1-bit pixel representations.

## Files

- `rle_image_decoder.py` — Python implementation
- `rle.bin` — run-length encoded image data

## Requirements

- Python
- NumPy
- Matplotlib
