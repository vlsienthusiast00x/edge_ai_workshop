# Module 4 - Memory-Constrained ML & Quantization Basics
# Quantization in Machine Learning

Quantization is the process of converting high‑precision values (like 32‑bit floating‑point numbers) into lower‑precision discrete values (such as 8‑bit integers).  
This reduces memory usage, speeds up computation, and lowers power consumption — all while keeping accuracy close to the original model.

---

## Why Quantization Matters
- **Smaller Model Size** → FP32 → INT8 cuts size by ~4×  
- **Faster Inference** → Integer math is faster than floating‑point  
- **Lower Power Usage** → Essential for embedded/IoT devices  
- **Edge Deployment** → Enables running ML models on resource‑constrained hardware

---

## How It Works
1. **Range Determination**  
   - Find min/max values of weights or activations.  
   - Static quantization: pre‑calculated using calibration data.  
   - Dynamic quantization: calculated during inference.

2. **Scaling & Zero‑Point**  
   - **Scale (S)**: Defines how floating values map to integers.  
   - **Zero‑Point (Z)**: Integer that represents “0” in float domain.  
   - Example: Mapping range `[-1, 1]` to INT8 range `[-128, 127]`.

3. **Weight Quantization**  
   - Compress trained parameters into integers.

4. **Activation Quantization**  
   - Compress outputs during inference.

---

## Trade‑offs
- **Quantization Error** → Difference between original and quantized values  
- **Rounding Noise** → Can reduce accuracy slightly  
- **Precision Loss** → Especially in sensitive feedback loops  
- **Implementation Care** → Scale and zero‑point must be applied correctly

✅ **In short:** Quantization trades precision for efficiency. It makes ML models smaller, faster, and more power‑friendly — which is critical for deploying neural networks on embedded systems like microcontrollers.

## Quantizing the MNIST handwritten digits SVM
We cannot directly export our weights to our main c program because VSDSQuadron PRO has only `16KB` SRAM and doing so can produce overflow of over `15KB` of memory. Below is the snippet of quantizing the main `mnist_svm.py`'s weights to int_8 and biases to int_32.
```py
# Simple scaling: map weights to int8 range [-127,127]
scale_w = np.max(np.abs(weights)) / 127.0
weights_q = np.round(weights / scale_w).astype(np.int8)

# Biases: scale to int32
biases_q = np.round(biases / (scale_w)).astype(np.int32)
```
Adding this small snippet to our code can reduce our memory usage by ×4.

## Implementation on VSDSquadron PRO
Now that we have quantized our weights and biases, we are ready to export them to a header file from which our main c program can read the weights and biases. After compiling the `mnist_svm.py` 2 header files are generetated `weights.h` and `input.h`. `input.h` is the input image that is taken from `X_test` array of test images that is feeded to the main c program, and `weights.h` are the weights of the model feeded to main c program.

It is important to declare the weights and biases arrays in the `weights.h` as ```c static const```

