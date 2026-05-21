# Module 5 - Neural Networks on RISC-V Microcontrollers
# Neural Networks
## What is a Neural Network?
A **neural network** is a computational model inspired by the human brain. It consists of layers of interconnected nodes (called *neurons*) that process input data and learn patterns to make predictions or classifications.

### Structure of a Neural Network

<img width="474" height="298" alt="image" src="https://github.com/user-attachments/assets/c5ed41c1-fe45-46ec-acb4-59f8525572a1" />


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

## Coding neural network for recognising handwritten digits
We will be using the same MNIST datasat as used before. We will use sklearn's `MPLClassifier` to predict digits. `MLPClassifier` is a strong tool for running neural network models which have small amount of data, for a big data, **Keras** is a better approach.
```python
# 3. Define a small MLP
mlp = MLPClassifier(hidden_layer_sizes=(32,), max_iter=20, activation='relu')
mlp.fit(X_train, y_train)
```

This declares the number of neurons in the hidden layer and their activiation function and trains the model.

## Quantizing the parameters
After compiling `mnist_neural.py`, two header files are generated one for the model's input and other containing weights and biases of each layer of the neural network. Obviously we cannot run our neural network directly on the board because the weights which are generated are in float and are 25300+ in number in this project. It is very important to keep in mind that one should only quantize the weights of each layer (in this case it is 2) not the biases because they are very small in count and have values very near to zero or in negative, so if we quantize them we will get all 0s.
```python
        # Compute per-layer scale for weights
        max_abs = np.max(np.abs(w))
        scale_w = 127.0 / max_abs if max_abs > 0 else 1.0

        # Quantize weights
        w_q = np.round(w * scale_w).astype(np.int8).flatten()
        b_f = b.astype(np.float32).flatten() 
```
This snippet quantizes the weights of the two layers.

## Neural network implementation on VSDSquadron PRO
## 1. Includes and Headers
```c
#include <stdio.h>
#include <stdint.h>
#include "weights.h"
#include "input.h"
```
- **`stdio.h`** → Provides standard input/output functions like `printf`.
- **`stdint.h`** → Defines fixed-width integer types (`int8_t`, `int32_t`).
- **`weights.h`** → Contains the trained neural network weights and biases.
- **`input.h`** → Contains the test input image (flattened MNIST digit).

---

## 2. Dense Layer Function
```c
void dense_layer(const int8_t *weights, const float *biases, float scale,
                 const float *input, float *output,
                 int in_size, int out_size, int apply_relu) {
    for (int j = 0; j < out_size; j++) {
        float acc = biases[j];
        int32_t sum = 0;

        for (int i = 0; i < in_size; i++) {
            sum += (int32_t)(input[i] * 127.0f) * weights[i * out_size + j];
        }

        acc += (float)sum / scale;

        // ReLU
        output[j] = apply_relu ? (acc > 0.0f ? acc : 0.0f) : acc;
    }
}
```

### Explanation:
- **Purpose**: Implements a fully connected (dense) layer of the neural network.
- **Parameters**:
  - `weights` → Quantized weights (`int8_t`).
  - `biases` → Bias values (`float`).
  - `scale` → Scaling factor to adjust quantized sums back to float.
  - `input` → Input vector (flattened image or hidden layer).
  - `output` → Output vector (hidden activations or logits).
  - `in_size` → Number of input neurons.
  - `out_size` → Number of output neurons.
  - `apply_relu` → Flag to apply ReLU activation (used for hidden layers).
- **Process**:
  - Multiply input values (scaled to int8 range) with weights.
  - Accumulate results in `sum`.
  - Add bias and rescale back to float.
  - Apply **ReLU** if requested (clamps negative values to 0).

---

## 3. Argmax Function
```c
int argmax(const float *logits, int size) {
    int max_index = 0;
    float max_val = logits[0];
    for (int i = 1; i < size; i++) {
        if (logits[i] > max_val) {
            max_val = logits[i];
            max_index = i;
        }
    }
    return max_index;
}
```

### Explanation:
- **Purpose**: Finds the index of the largest value in the output vector.
- **Use case**: Determines which digit (0–9) has the highest confidence score.
- **Process**:
  - Initialize with the first value.
  - Iterate through all logits.
  - Update `max_index` whenever a larger value is found.
  - Return the index of the maximum → predicted digit.

---

## 4. Main Function
```c
int main() {

    // Hidden layer output
    float hidden[32];
    dense_layer(layer0_weights, layer0_biases, layer0_scale,
                input, hidden, 784, 32, 1);

    // Output layer
    float output[10];
    dense_layer(layer1_weights, layer1_biases, layer1_scale,
                hidden, output, 32, 10, 0);

    // Prediction
    int predicted = argmax(output, 10);
    printf("Predicted digit: %d\n", predicted);

    return 0;
}
```

### Explanation:
- **Step 1**: Compute hidden layer activations (32 neurons).
  - Input: 784 pixels (flattened MNIST image).
  - Output: 32 hidden features.
  - ReLU applied.
- **Step 2**: Compute output layer logits (10 neurons).
  - Input: hidden layer activations.
  - Output: 10 class scores (digits 0–9).
  - No ReLU (final layer).
- **Step 3**: Use `argmax` to select the digit with the highest score.
- **Step 4**: Print the predicted digit.

---

## Summary
This program:
1. Loads an MNIST image (`input.h`).
2. Passes it through a **2-layer neural network**:
   - Hidden layer (784 → 32 neurons, ReLU).
   - Output layer (32 → 10 neurons).
3. Uses **argmax** to select the predicted digit.
4. Prints the result.

---

