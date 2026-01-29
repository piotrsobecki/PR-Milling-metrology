"""Core signal processing helpers."""
from typing import Tuple
import numpy as np
from scipy import signal


def bandpass_filter(x: np.ndarray, fs: float, low: float, high: float, order: int = 4) -> np.ndarray:
    """Apply a Butterworth bandpass filter.

    Args:
        x: 1D signal
        fs: sampling frequency (Hz)
        low: low cutoff (Hz)
        high: high cutoff (Hz)
        order: filter order

    Returns:
        filtered signal (same shape as `x`)
    """
    nyq = 0.5 * fs
    lown = low / nyq
    highn = high / nyq
    b, a = signal.butter(order, [lown, highn], btype="band")
    y = signal.filtfilt(b, a, x)
    return y


def compute_spectrogram(x: np.ndarray, fs: float, nperseg: int = 256, noverlap: int = 128) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute spectrogram (frequencies, times, Sxx).

    Returns (f, t, Sxx)
    """
    f, t, Sxx = signal.spectrogram(x, fs=fs, nperseg=nperseg, noverlap=noverlap)
    return f, t, Sxx
