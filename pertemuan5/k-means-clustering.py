import cv2
import numpy as np

# Menyamaratakan warna menjadi 2 jenis warna

# Membaca gambar
image = cv2.imread('image.jpg')
Z = image.reshape((-1, 3))

# Konversi ke float32
Z = np.float32(Z)

# Kriteria K-means
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Konversi kembali ke unit8 dan reshape
center = np.uint8(center)
res = center[label.flatten()]
segmented_image = res.reshape((image.shape))

# Menampilkan hasil
cv2.imshow('K-Means Sementation', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()