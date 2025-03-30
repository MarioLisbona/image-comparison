from PIL import Image
import imagehash
import sys
import os

def compare_images(image_path1, image_path2):
    # Calculate hash for both images
    with Image.open(image_path1) as img1, Image.open(image_path2) as img2:
        hash1 = imagehash.average_hash(img1)
        hash2 = imagehash.average_hash(img2)
    
    # Calculate the hash difference
    difference = hash1 - hash2
    
    print(f"\nComparing:")
    print(f"Image 1: {os.path.basename(image_path1)}")
    print(f"Image 2: {os.path.basename(image_path2)}")
    print(f"Hash difference: {difference}")
    print(f"Similar: {difference < 10}")  # Adjust threshold as needed
    
    return difference

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python test2.py <image1_path> <image2_path>")
        sys.exit(1)
    
    image1_path = sys.argv[1]
    image2_path = sys.argv[2]
    
    difference = compare_images(image1_path, image2_path)