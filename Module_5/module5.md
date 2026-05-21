# Module 5 - Neural Networks on RISC-V Microcontrollers
# Neural Networks
## What is a Neural Network?
A **neural network** is a computational model inspired by the human brain. It consists of layers of interconnected nodes (called *neurons*) that process input data and learn patterns to make predictions or classifications.

### Structure of a Neural Network
A typical neural network has three main types of layers:

1. **Input Layer**
   - Receives raw data (e.g., pixel values of an image).
   - Each neuron represents one feature of the input.

2. **Hidden Layers**
   - Perform transformations on the input using weights and biases.
   - Apply activation functions (like ReLU, sigmoid, or tanh) to introduce non-linearity.
   - Multiple hidden layers allow the network to learn complex patterns.

3. **Output Layer**
   - Produces the final result (e.g., class probabilities for digit recognition).
   - Often uses a softmax activation for classification tasks.

### How It Works
- **Forward Propagation**: Input data flows through the layers, and each neuron computes a weighted sum of inputs plus a bias, then applies an activation function.
- **Loss Function**: Compares the network’s prediction with the true label to measure error.
- **Backpropagation**: Adjusts weights and biases by propagating the error backward through the network using gradient descent.
- **Training**: Repeated forward and backward passes gradually minimize the loss, improving accuracy.

### Example: Digit Recognition
For MNIST digit classification:
- Input layer: 784 neurons (28×28 pixels).
- Hidden layer: e.g., 128 neurons with ReLU activation.
- Output layer: 10 neurons (digits 0–9) with softmax activation.
- The network learns to map pixel patterns to digit labels.

### Key Concepts
- **Weights**: Parameters that determine the strength of connections between neurons.
- **Biases**: Additional parameters that shift activation functions.
- **Activation Functions**: Introduce non-linearity, enabling the network to learn complex relationships.
- **Epochs**: Number of times the entire dataset passes through the network during training.

---

## Coding neural network for recofnising handwritten digits
We will use sklearn's `MPLClassifier` to predict digits. `MLPClassifier` is a strong tool for running neural network models which have small amount of data, for a big data **Keras** is a better approach.
