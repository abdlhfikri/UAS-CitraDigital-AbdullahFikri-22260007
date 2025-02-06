import cv2
# Membaca gambar
image = cv2.imread('image.jpg')
# Mendapatkan dimensi gambar
(h, w) = image.shape[:2]
# Menentukan pusat gambar
center = (w // 2, h // 2)
# Menentukan matriks rotasi
M = cv2.getRotationMatrix2D(center, 45, 1.0)
# Melakukan rotasi
rotated_image = cv2.warpAffine(image, M, (w, h))
# Mengubah ukuran gambar agar tidak full windows
resized_image = cv2.resize(rotated_image, (650, 600))
# Menampilkan hasil
cv2.imshow('Rotated Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()