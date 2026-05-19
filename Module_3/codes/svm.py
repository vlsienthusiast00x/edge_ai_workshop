from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = datasets.load_iris()
X = iris.data   # All 4 features
y = iris.target # Labels

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train Linear SVM classifier (one-vs-rest scheme)
clf = LinearSVC(C=1.0, random_state=42, max_iter=10000)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate performance
print("Predictions:", y_pred)
print("True labels:", y_test)
print("Weights (coef_):\n", clf.coef_)
print("Biases (intercept_):\n", clf.intercept_)
print("Accuracy:", accuracy_score(y_test, y_pred))
