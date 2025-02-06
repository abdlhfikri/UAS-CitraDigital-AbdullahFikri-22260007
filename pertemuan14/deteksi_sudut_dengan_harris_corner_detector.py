import cv2
import numpy as np

# Baca citra dalam grayscale
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Terapkan Harris Corner Detector
gray = np.float32(image)
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Tingkatkan sudut yang terdeteksi
image[corners > 0.01 * corners.max()] = [0, 0, 255]

# Tampilkan hasil deteksi sudut
cv2.imshow('Harris Corner Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()