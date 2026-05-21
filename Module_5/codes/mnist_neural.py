import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

# 1. Load MNIST dataset
X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
X = X / 255.0
y = y.astype(int)

# 2. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. Define a small MLP
mlp = MLPClassifier(hidden_layer_sizes=(32,), max_iter=20, activation='relu')
mlp.fit(X_train, y_train)

# 4. Export weights (int8) and biases (float32)
with open("weights.h", "w") as f:
    f.write("#include <stdint.h>\n")
    f.write("#ifndef WEIGHTS_H\n#define WEIGHTS_H\n\n")

    for i, (w, b) in enumerate(zip(mlp.coefs_, mlp.intercepts_)):
        # Compute per-layer scale for weights
        max_abs = np.max(np.abs(w))
        scale_w = 127.0 / max_abs if max_abs > 0 else 1.0

        # Quantize weights
        w_q = np.round(w * scale_w).astype(np.int8).flatten()
        b_f = b.astype(np.float32).flatten()  # keep biases float

        # Write weights
        f.write(f"static const int8_t layer{i}_weights[{w_q.size}] = {{\n")
        f.write(", ".join(map(str, w_q)))
        f.write("\n};\n\n")

        # Write biases
        f.write(f"static const float layer{i}_biases[{b_f.size}] = {{\n")
        f.write(", ".join(map(str, b_f)))
        f.write("\n};\n\n")

        # Write scale factor
        f.write(f"static const float layer{i}_scale = {scale_w}f;\n\n")

    f.write("#endif // WEIGHTS_H\n")

# 5. Export one test sample into input.h
sample_idx = 9  # pick a test image
sample = X_test.iloc[sample_idx].to_numpy()
label = y_test.iloc[sample_idx]

with open("input.h", "w") as f:
    f.write("#ifndef INPUT_H\n#define INPUT_H\n\n")
    f.write("static const float input[784] = {\n")
    f.write(", ".join(map(str, sample)))
    f.write("\n};\n\n")
    f.write(f"// True label: {label}\n")
    f.write("#endif // INPUT_H\n")

print("Export complete: input.h generated with one test sample")
