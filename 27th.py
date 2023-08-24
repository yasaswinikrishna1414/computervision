import cv2
import numpy as np

# Read an image
image = cv2.imread(r"C:\Users\grk66\OneDrive\Pictures\Saved Pictures\cat.jpg")

# Read another image
img2 = cv2.imread(r"C:\Users\grk66\OneDrive\Pictures\Saved Pictures\cat.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Could not read the image.")
else:
    # Continue with your image processing and display logic
    print(image.shape)
    cv2.imshow("original", image)
    # ... rest of your code
