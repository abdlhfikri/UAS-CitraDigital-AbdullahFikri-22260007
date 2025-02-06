import cv2
import numpy as np
# Membaca gambar
image = cv2.imread('image.jpg')
# Mendapatkan dimensi gambar
(h, w) = image.shape[:2]
# Translasi
M_translation = np.float32([[1, 0, 50], [0, 1, 100]])
translated_image = cv2.warpAffine(image, M_translation, (w, h))
# Mengubah ukuran gambar agar tidak full windows
resized_image = cv2.resize(translated_image, (650, 600))
# Rotasi 45 derajat
center = (w // 2, h // 2)
M_rotation = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, M_rotation, (w, h))
# Mengubah ukuran gambar agar tidak full windows
resized_image2 = cv2.resize(rotated_image, (650, 600))
# Menampilkan hasil
cv2.imshow('Translated Image', resized_image)
cv2.imshow('Rotated Image', resized_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()