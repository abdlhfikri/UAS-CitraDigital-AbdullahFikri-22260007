import cv2
import numpy as np

# Membaca Gambar
image = cv2.imread('image.jpg')
h, w = image.shape[:2]

# Mendefinisikan emapt titik sudut citra asli
points1 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])

# Mendefinisikan empat titik sudut baru
points2 = np.float32([[0, 0], [w, 0], [w // 4, h], [3 * w // 4, h]])

# Mendapatkan matriks transformasi persepektif
M_perspective = cv2.getPerspectiveTransform(points1, points2)

# Melakukan transformasi perspektif
perspective_transformed_image = cv2.warpPerspective(image, M_perspective, (w, h))

# Menampilkan Hsil
cv2.imshow('Perspective Transform image', perspective_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()