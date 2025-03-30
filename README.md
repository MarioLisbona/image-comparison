# Image Hash Comparison

Simple Python tool to compare images using perceptual hashing.

## Setup

1. Install required packages:

```bash
pip install imagehash
```

2. Run the script:

```bash
python compare_image_hash.py <image1_path> <image2_path>
```

## Usage

```bash
python compare_image_hash.py images/image1.jpg images/image2.jpg
```

## Output

The script will output the hash difference between the two images.

```bash
Comparing:
Image 1: image1.jpg
Image 2: image2.jpg
Hash difference: 10
```

## Notes

- The script uses the average hash method by default. You can change the hash method in the script.
- The script assumes the images are in the `images` directory. You can change the directory in the script.
