#include <stdio.h>
#include <stdint.h>
#include "weights.h"
#include "input.h"

// Dense layer
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

// Argmax
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
