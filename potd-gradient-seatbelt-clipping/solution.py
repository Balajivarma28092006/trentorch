import numpy as np


def clip_grad_norm(g: np.ndarray, tau: float) -> np.ndarray:
    norm = np.linalg.norm(g)
    if norm > tau:
        g = g * (tau / norm)
    return g
