# Image Hash Comparison

Simple Python tool to compare images using perceptual hashing.

## Setup

1. Install required packages:

```bash
pip install Pillow imagehash
```

## Usage

Compare two images by providing their file paths:

```bash
python compare_image_hash.py image1.jpg image2.jpg
```

## Hash Methods

You can change the hashing algorithm by modifying the `hash_method` variable in the script:

```python
hash_method = "average_hash"  # Change this line to use different methods
```

Available hash methods:

- `"average_hash"` (aHash) - Fast, but less accurate
- `"perception_hash"` (pHash) - More robust to scaling/compression
- `"difference_hash"` (dHash) - Good at detecting edges
- `"wavelet_hash"` (wHash) - Good at detecting both color and edges

## Example Output

```
Comparing Image Hashes:
Hash Method: average_hash
Image 1: photo1.jpg
Hash 1: f0f0f0f0f0f0f0f0
Image 2: photo2.jpg
Hash 2: f0f0f0f0f0f0f0f8
Hash difference: 1
Similar: True
```

## Notes

- Hash difference of 0 means identical images
- Higher numbers indicate more different images
- Images are considered similar if difference < 10
