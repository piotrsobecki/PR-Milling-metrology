"""Small CLI for demo/processing."""
import argparse
import numpy as np
from .processing import bandpass_filter


def demo():
    fs = 500.0
    t = np.arange(0, 2.0, 1.0/fs)
    x = np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*50*t)
    y = bandpass_filter(x, fs, 1.0, 10.0)
    print(f"Input mean {x.mean():.3f}, output mean {y.mean():.3f}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='signal_analysis CLI')
    parser.add_argument('--demo', action='store_true', help='run demo')
    args = parser.parse_args()
    if args.demo:
        demo()
