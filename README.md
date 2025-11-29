# SA-OFC-Simulation
Simulation code for the Structure-Aware Optimal Feedback Control (SA-OFC) model used in the manuscript.

## Overview
This repository contains the full implementation of the SA-OFC simulations, which evaluate how posture-dependent biomechanical stability (parameter **S**) influences optimal feedback control, noise amplification, and movement variability.

The simulation reproduces all results reported in the manuscript, including:
- Endpoint scatter plots across stability levels  
- Variance–stability curve  
- Eigenvalue changes with stability  
- Controller-mismatch effects  

## File Structure
SA-OFC-Simulation/
│── model.py              # SA-OFC model (dynamics + noise + LQR)
│── main_simulation.py    # Runs simulations for multiple S values
│── requirements.txt      # Dependencies
│── simulation_results.npy (generated after running main_simulation.py)
## Requirements
The simulation uses Python 3.8+ and the following packages:
numpy
scipy

To install:

```bash
pip install -r requirements.txt

Run the full sweep of stability values:
python main_simulation.py

Description of the Model
The SA-OFC model incorporates:
	•	Planar point-mass dynamics
	•	Posture-dependent damping (scaled by S)
	•	Signal-dependent motor noise
	•	Additive process noise
	•	Discrete-time Linear Quadratic Regulator (LQR)

The model equations and simulation parameters correspond exactly to those described in the manuscript’s Methods section.
Citing This Code

If you use this implementation, please cite:
N. Yamaki (2025). SA-OFC-Simulation: Structure-Aware Optimal Feedback Control model.
GitHub: https://github.com/nobuchika-yamaki/SA-OFC-Simulation
DOI: (will be added after Zenodo archive)
