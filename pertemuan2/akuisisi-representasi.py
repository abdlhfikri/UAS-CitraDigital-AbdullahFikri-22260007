import cv2
import numpy as np
from matplotlib import pyplot as plt
# Membaca gambar
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
# Menampilkan gambar
resized_image = cv2.resize(image, (650, 600))
cv2.imshow('Original Image', resized_image)
cv2.waitKey(0)
# Menampilkan histogram
plt.hist(image.ravel(), 256, [0,256])
plt.title('Histogram of Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
# Menutup jendela OpenCV
cv2.destroyAllWindows()

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# # Membaca gambar dalam format RGB
# image_rgb = cv2.imread('image.jpg')

# # Konversi gambar dari RGB ke Grayscale
# image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

# # Menampilkan gambar grayscale
# cv2.imshow('Grayscale Image', image_gray)
# cv2.waitKey(0)

# # Menampilkan histogram dari gambar grayscale
# plt.hist(image_gray.ravel(), 256, [0, 256])
# plt.title('Histogram of Grayscale Image')
# plt.xlabel('Pixel Intensity')
# plt.ylabel('Frequency')
# plt.show()

# # Menutup semua jendela OpenCV
# cv2.destroyAllWindows()
