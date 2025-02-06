import cv2
import numpy as np
from skimage.feature import local_binary_pattern

# Membaca gambar dalam grayscale
image = cv2.imread('image.jpg', 0)

# Menearpkan local binary pattern
radius = 1
n_points = 8 * radius
lbp = local_binary_pattern(image, n_points, radius, method='uniform')

# Menampilkan hasil
cv2.imshow('Local Binary Pattern', lbp)
cv2.waitKey(0)
cv2.destroyAllWindows()