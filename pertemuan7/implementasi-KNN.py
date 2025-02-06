from sklearn.neightbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Split data untuk pelatihan dan pengumjian 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Inisialisasi model KNN
knn = KNeighborsClassifier(n_neighbors=3)

# Latihan model menggunakan data pelatihan
knn.fit(X_train, y_train)

# Prediksi menggunakan data uji
y_pred = knn.predict(X_test)

# Hitungan akurasi
accuracy = accuracy_score(y_test, y_pred)
print(f'Akurasi KNN: {accuracy * 100:.2f}%')