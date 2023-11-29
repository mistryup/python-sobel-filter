import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from PIL import Image

# Load the image
# pick an image with borders etc which need highlighting
image_path = "image.jpg" 

# Convert to grayscale as easier to edge detect
# Load into numpy array for easy manipulation 
image = np.array(Image.open(image_path).convert('L'))  

# Apply Sobel filter for edge detection
sobel_filtered = ndimage.sobel(image)

# Display the original and processed images
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray') # Grayscale it for side by side comparison with new image
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(sobel_filtered, cmap='gray')
plt.title('Edge Detection (Sobel)')
plt.show()
