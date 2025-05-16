
##############################*******************************#########################*******************##############################
import numpy as np
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG19
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import math

# Paths to the dataset
train_dir = "E:/ML Dataset/BrainTumor/Training"
test_dir = "E:/ML Dataset/BrainTumor/Testing"

# Parameters
img_size = (224, 224)
batch_size = 32
epochs = 12  # Increased epochs for better training
num_classes = 4  # Glioma, Meningioma, Pituitary, No Tumor

# Data Augmentation for Training Set
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# No augmentation for testing data, just rescaling
test_datagen = ImageDataGenerator(rescale=1./255)

# Create Data Generators for Training and Testing
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=True
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False
)

# Visualize the dataset distribution
def visualize_data_distribution(generator, title):
    class_labels = list(generator.class_indices.keys())
    count_per_class = [len(os.listdir(os.path.join(generator.directory, label))) for label in class_labels]

    # Light pastel colors for the bars
    pastel_colors = ['#FFB6C1', '#87CEFA', '#C8A2C8', '#78c08f']

    # Plot bar chart for data distribution
    plt.figure(figsize=(8, 6))
    plt.bar(class_labels, count_per_class, color=pastel_colors)
    plt.title(title)
    plt.xlabel('Tumor Classes')
    plt.ylabel('Number of Images')
    plt.show()

# Visualize the distribution for both training and testing data
visualize_data_distribution(train_generator, "Training Data Distribution")
visualize_data_distribution(test_generator, "Testing Data Distribution")

# Load pre-trained VGG-19 model without top layers
base_model = VGG19(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Add custom layers for classification
x = Flatten()(base_model.output)
x = Dense(256, activation='relu')(x)
output = Dense(num_classes, activation='softmax')(x)  # 4 classes: Glioma, Meningioma, Pituitary, No Tumor

# Create the full model
model = Model(inputs=base_model.input, outputs=output)

# Freeze the convolutional base of VGG19 to only train the custom layers initially
for layer in base_model.layers:
    layer.trainable = False

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Print the model summary
model.summary()

# Callbacks for saving the best model and early stopping
checkpoint = ModelCheckpoint("best_model.keras", monitor='val_accuracy', save_best_only=True, mode='max')
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train the model
history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=test_generator,
    callbacks=[checkpoint, early_stopping],
    steps_per_epoch=train_generator.samples // batch_size,
    validation_steps=test_generator.samples // batch_size
)

# Load the best model
model.load_weights("best_model.keras")

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(test_generator, steps=math.ceil(test_generator.samples / batch_size))
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

# Predictions
predictions = model.predict(test_generator, steps=math.ceil(test_generator.samples / batch_size))
y_pred = np.argmax(predictions, axis=1)

# Class indices
class_labels = list(train_generator.class_indices.keys())

# Ground truth
y_true = test_generator.classes

# Compute the confusion matrix
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

# Classification Report
print(classification_report(y_true, y_pred, target_names=class_labels))

# Save the final model
model.save("E:/ML Dataset/BrainTumor/final_vgg19_brain.keras")
