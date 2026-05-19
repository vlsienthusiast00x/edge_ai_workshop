# Module 3 - From Regression to Classification (KNN → SVM)
### What is a KNN classifier?
A K-Nearest Neighbors (KNN) classifier is a supervised machine learning algorithm that classifies a data point based on the majority class of its K nearest neighboring data points in the feature space.

-----

<img width="550" height="250" alt="image" src="https://github.com/user-attachments/assets/d5fc2826-d940-4fec-b0f7-0ef6318f7a9c" />

### Implementation using scikit
In this implementation of the knn classifier we will be using a famous dataset called iris which classifies data into one of the 3 classes.

<img width="550" height="400" alt="image" src="https://github.com/user-attachments/assets/52f4eb11-3967-4f3f-85f0-9c8a810df632" />

### What is a SVM?
A Support Vector Machine (SVM) is a supervised machine learning algorithm that classifies data by finding an optimal hyperplane (decision boundary) that separates different classes with the maximum margin (distance between the boundary and nearest data points), where the nearest points are called support vectors, and kernels are used to handle non-linear data by transforming it into higher dimensions.

-----
<img width="753" height="474" alt="image" src="https://github.com/user-attachments/assets/ce28fa62-20e8-43dd-87fa-ad4376a7f517" />

### Implementation using scikit
<img width="550" height="450" alt="image" src="https://github.com/user-attachments/assets/b8ee1238-3f6d-4efa-9885-103cfdb7a3c0" />

### Implementation of SVM model on VSDSquadron PRO
Follow the same steps described in the previous module to make project in Freedom Studio and running it, just replace the main.c file's contents with this' [svm.c](codes/svm.c)

<img width="792" height="315" alt="image" src="https://github.com/user-attachments/assets/3bd009b3-2173-458b-bb20-4cddd0d68bc4" />

As we know that this svm model classifies the input array as one of the 3 classes, in this case the output is of class 0, which is the sentosa class of Iris flowers. You can change inputs to observe the accuracy of the prediction.

