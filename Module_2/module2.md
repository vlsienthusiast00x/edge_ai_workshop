# Module 2 - ML Foundations (Regression & Optimization)
## Machine learning
Machine learning (ML) is a branch of artificial intelligence that allows computers to learn patterns and make predictions or decisions from data without being explicitly programmed with fixed rules. The below topics are some of the basic fields of ML:-

### 1. Linear regression
#### Definition:
Linear Regression is a fundamental machine learning algorithm used for predictive modeling. It establishes a linear relationship between an independent variable (input) and a dependent variable (output), by fitting a straight line to the data.

<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/9edef658-a18a-4f6c-ace0-888a284b0b5a" />

#### Mathematical representation
𝑦 = 𝛽0 + 𝛽1.𝑥 + 𝜖
- 𝑦 : Predicted value (dependent variable)

- 𝑥 : Input feature (independent variable)

- 𝛽0 : Intercept (bias term)

- 𝛽1 : Slope (weight coefficient)

- 𝜖 : Error term (difference between prediction and actual value)

#### Implementation in python using scikit
<img width="800" height="680" alt="image" src="https://github.com/user-attachments/assets/113d166b-2af4-44ec-93bb-0a605d4032f7" />

### 2. Polynomial regression
#### Definition
Polynomial regression is a type of regression analysis that models the relationship between variables using a polynomial equation, allowing you to fit curved lines instead of just a straight line.

#### Mathematical representation
𝑦 = 𝛽0 + 𝛽1.𝑥 + 𝛽2.𝑥2 + 𝛽3.𝑥3+⋯+𝛽𝑛.𝑥𝑛+𝜖
- 𝑦 : Dependent variable (output)
- 𝑥 : Independent variable (input)
- 𝛽0,𝛽1,…,𝛽𝑛: Coefficients
- 𝑛 : Degree of the polynomial
- 𝜖 : Error term

#### Implementation using scikit
<img width="797" height="680" alt="image" src="https://github.com/user-attachments/assets/9d1006f4-d55a-424c-ad64-6cb72326ba08" />


