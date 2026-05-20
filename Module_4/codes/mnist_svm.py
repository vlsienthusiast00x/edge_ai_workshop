import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_openml

# ---- Train the model ----
mnist = fetch_openml('mnist_784', version=1)
X, y = mnist.data.to_numpy(), mnist.target.astype(int).to_numpy()
X = X / 255.0  # normalize

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

clf = LinearSVC(C=1.0, max_iter=10000, random_state=42)
clf.fit(X_train, y_train)

weights = clf.coef_    # shape (10, 784)
biases  = clf.intercept_

# ---- Quantization parameters ----
# Simple scaling: map weights to int8 range [-127,127]
scale_w = np.max(np.abs(weights)) / 127.0
weights_q = np.round(weights / scale_w).astype(np.int8)

# Biases: scale to int32
biases_q = np.round(biases / (scale_w)).astype(np.int32)

# ---- Export to header file ----
with open("weights.h", "w") as f:
    f.write("#include <stdint.h>\n")
    f.write("#ifndef WEIGHTS_H\n")
    f.write("#define WEIGHTS_H\n\n")

    f.write("static const int8_t weights[10][784] = {\n")
    for i in range(weights_q.shape[0]):
        row = ", ".join(str(w) for w in weights_q[i])
        f.write(f"    {{ {row} }},\n")
    f.write("};\n\n")

    f.write("static const int32_t biases[10] = {\n")
    row = ", ".join(str(b) for b in biases_q)
    f.write(f"    {row}\n")
    f.write("};\n\n")

    f.write("static const float scale_w = %.6f;\n" % scale_w)
    f.write("#endif // WEIGHTS_H\n")


idx = 1   
sample = X_test[idx]
label = y_test[idx]

with open("input.h", "w") as f:
    f.write("#ifndef INPUT_H\n")
    f.write("#define INPUT_H\n")
    f.write(f"#define TRUE {label}\n\n")

    f.write(f"// MNIST test sample index {idx}\n")

    f.write("static const float input[784] = {\n")
    row = ", ".join(f"{v:.6f}" for v in sample)
    f.write(f"    {row}\n")
    f.write("};\n\n")

    f.write("#endif // INPUT_H\n")
