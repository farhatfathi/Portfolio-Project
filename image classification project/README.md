# Animal Image Classification: Cats, Dogs, Snakes 🐱🐶🐍

This project builds and fine-tunes an image classification model using both a custom CNN and a transfer learning approach with **MobileNetV2**. The dataset consists of 3 animal classes: **cats, dogs, and snakes**.

## 📁 Dataset Structure

The dataset is structured into 3 directories (each containing respective animal images):

/data/Animals/
├── cats/
├── dogs/
└── snakes/

## 🧠 Model Architecture

### 1. Custom CNN
- 3 convolutional layers (with BatchNormalization + MaxPooling)
- 2 fully connected dense layers
- Dropout for regularization

### 2. MobileNetV2 + CNN (Sequential)
- Pre-trained `MobileNetV2` (frozen)
- Global Average Pooling
- Fully connected layers with dropout
- Final softmax output layer for multi-class classification

## 🏋️‍♂️ Training

- **Image Augmentation** applied via `ImageDataGenerator`
- **EarlyStopping** callback stops training when validation accuracy ≥ 95% for 3 consecutive epochs.
- **ModelCheckpoint** saves the best performing model.
- **Class weights** are used to balance the training for imbalanced classes.

## 📈 Performance Visualization

Accuracy and Loss are plotted after training using:

```python
plot_history(history, "Model Title")

🧪 Evaluation

Model performance is evaluated using:
	•	classification_report
	•	confusion_matrix

💾 Model Export

The model is saved in:
	•	Keras .keras format
	•	TensorFlow SavedModel
	•	TFLite
	•	TensorFlow.js

📦 Dependencies
	•	TensorFlow
	•	NumPy
	•	Matplotlib
	•	Scikit-learn
	•	TensorFlowJS (pip install tensorflowjs)

▶️ How to Run
	1.	Clone the repo
	2.	Place your dataset under /data/Animals/
	3.	Run the notebook or script for training
	4.	Evaluate and visualize results

⸻

Author: Muhammad Fathi Farhat
Cohort ID: A200YBF317