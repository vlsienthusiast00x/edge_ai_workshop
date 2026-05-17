import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Sample data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
y = np.array([2, 5, 9, 20, 35, 50, 70, 95, 130])

# Polynomial transformation (degree=2 for quadratic curve)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Fit model
model = LinearRegression()
model.fit(X_poly, y)

# Predictions
y_pred = model.predict(X_poly)
print(y_pred)
# Plot
plt.scatter(X, y, color="blue", label="Data Points")
plt.plot(X, y_pred, color="red", label="Polynomial Fit")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Polynomial Regression Example")
plt.legend()
plt.show()
