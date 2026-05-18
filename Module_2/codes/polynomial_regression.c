#include <stdio.h>

float intercept = 5.5714286f;
float coefficients[3] = {0.0f, -4.7147186f, 2.0281385f};

// Prediction function
float predict(float x) {
    return intercept + coefficients[1] * x + coefficients[2] * (x * x);
}

// Print float values
void print_float(float val) {
    int int_part = (int)val;
    int frac_part = (int)((val - int_part) * 100);
    if (frac_part < 0) frac_part = -frac_part;
    printf("%d.%02d", int_part, frac_part);
}

int main() {
    float input = 8.0f;
    float output = predict(input);

    printf("Prediction for ");
    print_float(input);
    printf(" = ");
    print_float(output);
    printf("\n");

    return 0;
}
