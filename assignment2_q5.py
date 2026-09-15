import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# Read the run-length encoded binary file
# ---------------------------------------------------------

A = np.fromfile('/Users/hananw/Documents/CPBS_7620/ass2/rle.bin', dtype='<u4')

# The first two values give the image dimensions
rows = int(A[0])
cols = int(A[1])

# Everything after that contains the run lengths
runs = A[2:]

print("Number of rows:", rows)
print("Number of columns:", cols)
print("Number of runs:", len(runs))

# ---------------------------------------------------------
# Decompress the run-length encoded data
# ---------------------------------------------------------

# Total number of pixels in the image
num_pixels = rows * cols

# Create an empty one-dimensional array for the decoded pixels
pixels = np.empty(num_pixels, dtype=np.uint8)

# The problem tells us that the first symbol is 0
current_value = 0

# This tells us where to start writing the next run
position = 0

for count in runs:

    count = int(count)

    # Fill 'count' positions with the current value
    pixels[position:position + count] = current_value

    # Move to the next empty position
    position = position + count

    # Switch:
    # 0 becomes 1
    # 1 becomes 0
    current_value = 1 - current_value


# Make sure the RLE data produced exactly the expected
# number of pixels
print("Decoded pixels:", position)
print("Expected pixels:", num_pixels)


# ---------------------------------------------------------
# Reshape into the original image
# ---------------------------------------------------------

# The assignment says the data is stored in column-major order.
# order='F' tells NumPy to fill the image column by column.
image = pixels.reshape((rows, cols), order='F')


# ---------------------------------------------------------
# Display the image
# ---------------------------------------------------------

plt.imshow(image, cmap='gray', vmin=0, vmax=1)
plt.axis('off')
plt.title('Decompressed RLE Image')
plt.show()

# ---------------------------------------------------------
# Compression: original pixels stored as 32-bit integers
# ---------------------------------------------------------

original_32_bits = num_pixels * 32
compressed_bits = len(A) * 32

compression_ratio_32 = original_32_bits / compressed_bits

percent_saved_32 = (
    1 - compressed_bits / original_32_bits
) * 100

print()
print("Original size using 32-bit pixels:", original_32_bits, "bits")
print("RLE size:", compressed_bits, "bits")
print("Compression ratio:", compression_ratio_32)
print("Percent space saved:", percent_saved_32, "%")

# ---------------------------------------------------------
# Compression assuming original pixels were only 1 bit
# ---------------------------------------------------------

original_1_bit = num_pixels

ratio_1 = original_1_bit / compressed_bits
saved_1 = (1 - compressed_bits / original_1_bit) * 100

print()
print("1-bit original:")
print("Original size =", original_1_bit, "bits")
print("RLE size      =", compressed_bits, "bits")
print("Compression ratio =", ratio_1)
print("Space saved =", saved_1, "%")