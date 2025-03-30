from PIL import Image
import imagehash
import sys
import os

def compare_images(image_path1, image_path2):
    # Calculate hash for both images
    hash_method = "average_hash"  # Can be: average_hash, perception_hash, difference_hash, wavelet_hash
    
    with Image.open(image_path1) as img1, Image.open(image_path2) as img2:
        if hash_method == "average_hash":
            hash1 = imagehash.average_hash(img1)
            hash2 = imagehash.average_hash(img2)
        elif hash_method == "perception_hash":
            hash1 = imagehash.phash(img1)
            hash2 = imagehash.phash(img2)
        elif hash_method == "difference_hash":
            hash1 = imagehash.dhash(img1)
            hash2 = imagehash.dhash(img2)
        elif hash_method == "wavelet_hash":
            hash1 = imagehash.whash(img1)
            hash2 = imagehash.whash(img2)
    
    # Calculate the hash difference
    difference = hash1 - hash2
    
    print(f"\nComparing Image Hashes:")
    print(f"Hash Method: {hash_method}")
    print(f"Image 1: {os.path.basename(image_path1)}")
    print(f"Hash 1: {hash1}")
    print(f"Image 2: {os.path.basename(image_path2)}")
    print(f"Hash 2: {hash2}")
    print(f"Hash difference: {difference}")
    print(f"Similar: {difference < 10}")  
    
    return difference

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python test2.py <image1_path> <image2_path>")
        sys.exit(1)
    
    image1_path = sys.argv[1]
    image2_path = sys.argv[2]
    
    difference = compare_images(image1_path, image2_path)