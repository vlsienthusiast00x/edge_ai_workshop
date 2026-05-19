# Module 3 - From Regression to Classification (KNN → SVM)
### What is a KNN classifier?
A K-Nearest Neighbors (KNN) classifier is a supervised machine learning algorithm that classifies a data point based on the majority class of its K nearest neighboring data points in the feature space.

-----

<img width="550" height="250" alt="image" src="https://github.com/user-attachments/assets/d5fc2826-d940-4fec-b0f7-0ef6318f7a9c" />

### Implementation using scikit
In this implementation of the knn classifier we will be using a famous dataset called [Iris](https://archive.ics.uci.edu/dataset/53/iris) which classifies data into one of the 3 classes of Iris flowers.

<img width="550" height="400" alt="image" src="https://github.com/user-attachments/assets/52f4eb11-3967-4f3f-85f0-9c8a810df632" />

### What is a SVM?
A Support Vector Machine (SVM) is a supervised machine learning algorithm that classifies data by finding an optimal hyperplane (decision boundary) that separates different classes with the maximum margin (distance between the boundary and nearest data points), where the nearest points are called support vectors, and kernels are used to handle non-linear data by transforming it into higher dimensions.

-----
<img width="753" height="474" alt="image" src="https://github.com/user-attachments/assets/ce28fa62-20e8-43dd-87fa-ad4376a7f517" />

### Implementation using scikit
<img width="550" height="450" alt="image" src="https://github.com/user-attachments/assets/b8ee1238-3f6d-4efa-9885-103cfdb7a3c0" />

### Implementation of SVM model on VSDSquadron PRO
Follow the same steps described in the previous module to make project in Freedom Studio and running it, just replace the main.c file's contents with this' [svm.c](codes/svm.c)

<img width="500" alt="image" src="https://github.com/user-attachments/assets/3bd009b3-2173-458b-bb20-4cddd0d68bc4" />

As we know that this svm model classifies the input array as one of the 3 classes, in this case the output is of class 0, which is the sentosa class of Iris flowers. You can change inputs to observe the accuracy of the prediction.

## Implementing MNIST hadwritten digit classification model with SVM 
The MNIST dataset is a benchmark collection of handwritten digit images (0–9), widely used in machine learning and deep learning. It contains 70,000 grayscale images of size 28×28 pixels, split into 60,000 training samples and 10,000 test samples. Each image is labeled with the digit it represents.

<img width="1000" height="300" alt="image" src="https://github.com/user-attachments/assets/7ec72c05-3a88-4665-a714-08c9c0a5e822" />

----
To implement this model using SVM we can use the same SVC macro provided by sklearn library.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/385b27be-b5a1-4997-a65d-9f9e1f512958" />

The above picture is created by matplotlib after providing a sample input data.


