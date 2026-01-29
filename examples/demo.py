"""Example: generate synthetic signal and plot filtered result."""
import matplotlib.pyplot as plt
import numpy as np
from signal_analysis.processing import bandpass_filter, compute_spectrogram


def main():
    fs = 500.0
    t = np.arange(0, 2.0, 1.0/fs)
    x = np.sin(2*np.pi*5*t) + 0.8*np.sin(2*np.pi*50*t)
    y = bandpass_filter(x, fs, 1.0, 20.0)

    fig, ax = plt.subplots(2, 1, figsize=(8,6))
    ax[0].plot(t, x)
    ax[0].set_title('Raw signal')
    ax[1].plot(t, y)
    ax[1].set_title('Bandpass 1-20 Hz')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
