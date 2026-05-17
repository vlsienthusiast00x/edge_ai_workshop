# Module 1 - Edge AI Orientation & Hardware Primer

## Traditional Logic vs edge AI Logic
### What is Edge AI?
Edge AI is the practice of running artificial intelligence models directly on local devices (like smartphones, IoT sensors, cameras, or robots) instead of relying on cloud servers. This enables real-time decision-making, faster responses, better privacy, and reduced bandwidth usage.
### Comparison Table

| Aspect            | Traditional Logic                 | AI Logic (Edge AI)                   |
|-------------------|-----------------------------------|-------------------------------------|
| **Approach**      | Manual, step-by-step              | AI-assisted, automated suggestions  |
| **Control**       | Full developer control            | Shared control with AI guidance     |
| **Speed**         | Slower, requires coding effort    | Faster, AI generates optimized code |
| **Error Handling**| Manual debugging                  | AI proposes fixes instantly         |
| **Optimization**  | Human intuition                   | ML-driven recommendations           |
| **Learning Curve**| Requires deep coding knowledge    | Easier with AI support              |
| **Creativity**    | Limited to developer imagination  | AI expands possibilities            |

---

## Getting familiar with VSDSquadron PRO 

### VSDSquadron PRO Specifications

### Board Overview
- **Form Factor**: 84 mm × 52 mm (Max Height: Top 8 mm, Bottom 1 mm)
- **I/O Voltage**: 3.3V
- **Input Voltage**: 5V (Nominal, via USB-C)
- **Operating Temperature**: 20°C – 35°C (68°F – 95°F)
- **USB Interface**: USB-C Type (via FT2232 USB-to-Serial Converter)
- **Crystal Oscillators**: On-board 12 MHz, 16 MHz

---

### Microcontroller (SiFive FE310-G002)
- **Architecture**: RV32IMAC ISA (32-bit RISC-V)
- **Core**: SiFive E31 Core Complex
- **Frequency**: Up to 320 MHz
- **Performance**: 1.61 DMIPS/MHz, 2.73 Coremark/MHz
- **Hardware Accelerators**: Integer Multiply/Divide (8-bit/cycle multiply, 1-bit/cycle divide)
- **Branch Predictor**: 40 BTB entries, 128 BHT entries, 2-entry RAS

---

### Memory Subsystem
- **Instruction Cache (L1)**: 16 KB, 2-way set associative, 32-byte lines
- **Data SRAM (L1)**: 16 KB DTIM, 2-cycle access latency
- **Mask ROM (MROM)**: 8 KB (Boot code, platform config, debug routines)
- **OTP Program Memory**: 8 KB, in-circuit programmable
- **Off-Chip SPI Flash**: 32 Mbit ISSI SPI Flash (on board), expandable up to 512 MiB via QSPI

---

### Peripherals & Interfaces
- **GPIO**: 19 Digital I/O pins (on board), 32 on chip  
  - Configurable as input/output, pull-ups, drive strengths, output inversion
- **UART**: 2 instances (UART0, UART1) with 8-entry TX/RX FIFO
- **I2C**: 1 instance (I2C0)
- **QSPI**: Dedicated flash interface + 2 additional QSPI controllers
- **PWM**: 3 independent controllers  
  - PWM0: 8-bit, 4 comparators  
  - PWM1: 16-bit, 4 comparators  
  - PWM2: 16-bit, 4 comparators  
  - 9 PWM pins on board
- **External Interrupts**: 19 pins
- **External Wakeup**: 1 pin (AON_PMU_DWAKEUP_N)

---

### Debugging Features
- **JTAG**: 4-wire IEEE 1149.1 compliant
- **Debug Module**: 8 programmable hardware breakpoints
- **Instructions**: Implements BYPASS and IDCODE (0x20000913)
- **Access**: Via JTAG DEBUG instruction (2-bit opcode, 7-bit address, 32-bit data field)

---


### Dimensions
- **Board Size**: 84 mm × 52 mm  
- **Height**: Top 8 mm, Bottom 1 mm


