# Imaginary Numbers in Logic Gates: Beyond Ternary Paradigms

This repository implements the mathematical framework and software simulation for a four-state logic system that incorporates the imaginary unit into traditional ternary logic. This research explores new dimensions for computing paradigms by adding an orthogonal state to the standard  base.

## Theoretical Framework

While traditional ternary logic operates on a linear scale, this system introduces a fourth state, , representing oscillatory or reactive characteristics.

| State | Logic Level | Physical Analogy |
| --- | --- | --- |
| **+1** | High / Active | Warmth / Strong DC Signal      |
| **0** | Neutral / Standby | Equilibrium / No Signal     |
| **-1** | Low / Inactive | Coldness / Negative DC Signal |
| **i** | Imaginary | Oscillatory / AC Characteristics     |

## The Universal Imaginary NAND Gate

The core of this implementation is the **Universal Imaginary NAND Gate**. The research demonstrates its functional completeness, allowing for the construction of diverse logic gates within this four-state framework.

**Key Logic Rules:**

**Output = 1:** Generated if any input is Low (-1).



**Output = 0:** Produced if any input is Neutral (0), provided no Low (-1) input is present.



**Output = -1:** Generated if both inputs are High (1), or if a High (1) input interacts with an Imaginary (i) input.



**Output = i:** Occurs strictly when both inputs are the Imaginary unit (i).



## Research Citation

If you utilize this code or logic in your research, please cite:

> Pulickal, P. B. (2024). *Imaginary Numbers in Logic Gates: Beyond Ternary Paradigms.*
