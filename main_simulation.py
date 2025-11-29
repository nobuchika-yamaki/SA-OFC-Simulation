# main_simulation.py
import numpy as np
from model import SAOFCModel

def run_single_trial(S, total_time=0.5, dt=0.01):
    model = SAOFCModel(S=S, dt=dt)
    steps = int(total_time / dt)
    x = np.array([0, 0, 0, 0], dtype=float)
    for _ in range(steps):
        x = model.step(x)
    return x[:2]

def simulate_across_stability(S_values, n_trials=500):
    results = {}
    for S in S_values:
        endpoints = np.array([run_single_trial(S) for _ in range(n_trials)])
        results[S] = endpoints
        print(f"S={S}: done")
    return results

if __name__ == "__main__":
    S_values = [0.1, 0.2, 0.4, 0.55, 0.9]
    results = simulate_across_stability(S_values)
    np.save("simulation_results.npy", results)
    print("Simulation finished. Saved to simulation_results.npy")
