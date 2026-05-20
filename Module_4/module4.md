# Module 4 - Memory-Constrained ML & Quantization Basics
## ML quantization
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

✅ **In short:** Quantization trades precision for efficiency. It makes ML models smaller, faster, and more power‑friendly — which is critical for deploying neural networks on embedded systems like microcontrollers.
