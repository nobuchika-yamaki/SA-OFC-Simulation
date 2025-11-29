# model.py
import numpy as np
from scipy.linalg import solve_discrete_are

class SAOFCModel:
    def __init__(self, S=1.0, dt=0.01):
        self.S = S
        self.dt = dt
        damping = 0.4 * S
        self.A = np.array([
            [1, 0, dt, 0],
            [0, 1, 0, dt],
            [0, 0, 1 - damping * dt, 0],
            [0, 0, 0, 1 - damping * dt]
        ])
        self.B = np.array([
            [0, 0],
            [0, 0],
            [dt, 0],
            [0, dt]
        ])
        self.process_noise_std = 0.015 / S
        self.signal_noise_scale = 0.03 * (1 / S)
        self.Q = np.diag([50, 50, 1, 1])
        self.R = np.eye(2) * 0.01
        self.K = self.compute_lqr_gain()

    def compute_lqr_gain(self):
        P = solve_discrete_are(self.A, self.B, self.Q, self.R)
        K = np.linalg.inv(self.B.T @ P @ self.B + self.R) @ (self.B.T @ P @ self.A)
        return K

    def step(self, x):
        u = -self.K @ x
        sd_noise = np.random.randn(2) * self.signal_noise_scale * np.linalg.norm(u)
        u_noisy = u + sd_noise
        w = np.random.randn(4) * self.process_noise_std
        return self.A @ x + self.B @ u_noisy + w
