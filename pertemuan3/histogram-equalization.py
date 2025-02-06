import cv2
import numpy as np
from matplotlib import pyplot as plt
# Membaca gambar dalam grayscale
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
# Mengubah ukuran gambar agar tidak full windows
resized_image = cv2.resize(image, (650, 600))
# Equalisasi histogram
equalized_image = cv2.equalizeHist(resized_image)
# Menampilkan gambar asli dan hasil equalization
cv2.imshow('Original Image', resized_image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Menampilkan histogram
plt.hist(equalized_image.ravel(), 256, [0,256])
plt.title('Histogram of Equalized Image')
plt.show()