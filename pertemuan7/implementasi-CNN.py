from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical

# Inisialisasi model CNN
model = Sequential()

# Tambahkan convolutional layer
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flattening
model.add(Flatten())

# Fully connected layer
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', matrics=['accuracy'])

# Latih model
model.fit(X_train, to_categorical(y_train), epochs=10, batch_size=32)

# Evaluasi model
loss, accuracy = model.evaluate(X_test, to_categorical(y_test))
print(f'Akurasi CNN: {accuracy * 100:.2f}%')