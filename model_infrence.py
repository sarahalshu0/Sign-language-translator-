import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# إعداد البيانات
train_data = ImageDataGenerator(rescale=1./255)
train_generator = train_data.flow_from_directory(
    'dataset',  # مجلد البيانات الذي يحتوي على الحروف
    target_size=(64, 64),  # تصغير الصور لهذا الحجم
    batch_size=16,
    class_mode='categorical'  # التصنيف متعدد الفئات
)

# بناء النموذج
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(train_generator.num_classes, activation='softmax')  # عدد الفئات حسب عدد الحروف
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# تدريب النموذج
model.fit(train_generator, epochs=10)

# حفظ النموذج
model.save('sign_lang_model.h5')
