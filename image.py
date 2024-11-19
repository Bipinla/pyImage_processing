#Using python 3.13.0 numpy-2.1.3 opencv-python-4.10.0.84
import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Function to upload an image
def upload_image():
    Tk().withdraw()  # Prevents the root window from appearing
    filename = askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    return filename

# Load the image
image_path = upload_image()
if image_path:
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (1, 1), 0)

    # Apply binary thresholding to isolate black spots
    _, binary = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)

    # Find contours of the black spots
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    result = image.copy()
    cv2.drawContours(result, contours, -1, (0, 255, 0), 2)  # Draw in green

    # Show the result
    cv2.imshow('Detected Black Spots', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No image selected.")
