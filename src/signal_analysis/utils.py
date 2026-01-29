"""Utility IO helpers."""
from typing import Tuple
import numpy as np
import pandas as pd


def load_csv(path: str, column: int = 0) -> Tuple[np.ndarray, float]:
    """Load a single-column CSV as a numpy array.

    Returns (data, sampling_interval) — sampling interval placeholder is None here.
    """
    df = pd.read_csv(path)
    arr = df.iloc[:, column].to_numpy(dtype=float)
    return arr, None


def save_array(path: str, x: np.ndarray) -> None:
    """Save a 1D array to a CSV file."""
    pd.DataFrame(x).to_csv(path, index=False, header=False)
