from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt

# Load MNIST dataset
mnist = fetch_openml('mnist_784', version=1)

# Convert to NumPy arrays 
X = mnist.data.to_numpy()
y = mnist.target.astype(int).to_numpy()

# Normalize pixel values
X = X / 255.0

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Linear SVM (one-vs-rest scheme)
clf = LinearSVC(C=1.0, max_iter=10000, random_state=42)
clf.fit(X_train, y_train)

# Predict a single image
sample = X_test[0].reshape(1, -1)  
true_label = y_test[0]
pred = clf.predict(sample)

print("True label:", true_label)
print("Predicted label:", pred[0])


plt.imshow(X_test[0].reshape(28, 28), cmap="gray")
plt.title(f"True: {true_label}, Predicted: {pred[0]}")
plt.show()
