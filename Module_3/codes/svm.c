#include <stdio.h>

// Weights and biases initialization
const float biases[3] = { 0.11075444,  1.89005527, -1.23569765};
const float weights[3][4] = {
		{0.18260589,  0.45261904, -0.80650125, -0.45133743},
	    {0.10523523, -1.00140409,  0.29794679, -0.77798341},
        {-0.74518728, -1.20519247,  1.36592234,  1.5793089}
};

// Prediction function
int predict(float *x) {
	float decision_score[3];
	for (int i = 0; i < 3; i++) {
		decision_score[i] = biases[i];
		for (int n = 0; n < 4; n++) {
			decision_score[i] += weights[i][n] * x[n];
		}
	}

	float highest_score = decision_score[0];
	int pred_class = 0;
	for (int k = 1; k < 3; k++) {
		if (decision_score[k] > highest_score) {
			highest_score = decision_score[k];
			pred_class = k;
		}
	}
	return pred_class;

}


int main() {
	float input[4] = {5.7, 3.8, 1.7, 0.3};
    int output = predict(input);
    const char *labels[3] = {"setosa", "versicolor", "virginica"};
    printf("Prediction = %d (%s)\n", output, labels[output]);
    return 0;
}
