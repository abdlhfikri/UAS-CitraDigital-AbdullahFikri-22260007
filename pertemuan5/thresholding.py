import cv2
import numpy as np

# Membuat foto menjadi hitam putih seperti di app photoshop

# Membaca gambar dalam grayscale
image = cv2.imread('image.jpg', 0)

# Menerapkan thresholding
ret, thresh_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Menampilkan hasil
cv2.imshow('Thresholded Image', thresh_image)
cv2.waitKey(0)
cv2.destroyAllWindows()