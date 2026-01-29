import numpy as np
from signal_analysis.processing import bandpass_filter


def test_bandpass_attenuates():
    fs = 500.0
    t = np.arange(0, 2.0, 1.0/fs)
    # 5 Hz (in-band) + 50 Hz (out-of-band)
    x = np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*50*t)
    y = bandpass_filter(x, fs, 1.0, 10.0)
    # compute RMS power of components via FFT
    X = np.abs(np.fft.rfft(x))
    Y = np.abs(np.fft.rfft(y))
    freqs = np.fft.rfftfreq(len(t), 1.0/fs)
    # power near 50 Hz should be much reduced after filtering
    idx50 = (freqs>45) & (freqs<55)
    idx5 = (freqs>4) & (freqs<6)
    assert Y[idx5].mean() > 0.1
    assert Y[idx50].mean() < X[idx50].mean() * 0.3
