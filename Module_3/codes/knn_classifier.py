from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

knn = KNeighborsClassifier(n_neighbors=5, weights="uniform")
knn.fit(X_train, y_train)


accuracy = knn.score(X_test, y_test)
print("Model accuracy on test set:", accuracy)

# Format: [sepal length, sepal width, petal length, petal width]
sample = [[6.5, 3.0, 5.2, 2.0]]  
prediction = knn.predict(sample)[0]

print("Prediction for sample:", iris.target_names[prediction])
