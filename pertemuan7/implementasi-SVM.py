import cv2
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Membaca dataset citra
# X adalah array fitur dan y adalah array label (kelas)
X = [] # fitur dari citra
y = [] # label dari citra

# Split data untuk pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Inisialisasi model SVM
clf = svm.SVC(kernel='linear')

# Latihan model menggunakan data pelatihan
clf.fit(X_train, y_train)

# Prediksi menggunakan data uji
y_pred = clf.predict(X_test)

# Hitung akurasi
accuracy = accuracy_score(y_test, y_pred)
print(f'Akurasi: {accuracy * 100:.2f}%')