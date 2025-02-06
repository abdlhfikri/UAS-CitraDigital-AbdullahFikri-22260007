from skimage.feature import greycomatrix, greycoprops
import cv2

# Membaca gambar dalam grayscale
image = cv2.imread('image.jpg', 0)

# Menhitung GLCM
glcm = greycomatrix(image, distances=[1], angles=[0], levels=256, symmetric=True, normed=True)

# Menghitung fitur tekstur dari GLCM
contrast = greycoprops(glcm, 'contrast')[0, 0]
energy = greycoprops(glcm, 'energy')[0, 0]

print(f'Contrast: {contrast}, Energy: {energy}')