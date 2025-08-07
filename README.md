# Exploring Dynamic Circuits through Gibbs Free Energy Calculations via Variational Quantum Algorithms

![Python](https://img.shields.io/badge/Python-3.12.10-blue.svg) ![Qiskit](https://img.shields.io/badge/Qiskit-1.1.0-green)   

## Abstract
Dynamic circuits represent a paradigm shift in quantum algorithm design by enabling mid-
circuit measurements, conditional operations, and classical-quantum feedback during execution.
In this work, we leverage the power of dynamic circuits to variationally estimate the Gibbs Free
Energy of quantum systems, focusing on the Transverse Field Ising Model (TFIM). Utilizing
Qiskit’s dynamic capabilities, we implement variational quantum Gibbs state preparation, in-
corporate swap tests with mid-circuit resets, and demonstrate the effect of Quasi-Probabilistic
Readout Correction (QPRC) in noisy environments. Our implementation achieves high-fidelity
ground state approximation with efficient circuit depth management, demonstrating the poten-
tial of dynamic circuits for near-term quantum thermodynamic calculations.

## Code instructions

- Run the following command in the terminal to install the dependencies:
  
   ```pip install -r requirements.txt```
- The Jupyter Notebooks are available in the `jupyter_notebooks` folder.
- The helper functions used in the project are available in the `src` folder.
