import numpy as np
import matplotlib.pyplot as plt

# Parameters
x = np.linspace(0, 2 * np.pi, 1000)  # x values from 0 to 2π with 1000 points
frequency1 = 1.0                     # Frequency of the first sine wave
frequency2 = 1.5                     # Frequency of the second sine wave
phase_shift = np.pi / 2              # Phase shift for the second sine wave

# Functions
def sinusoid(frequency, phase=0):
    """Helper function to create a sinusoidal signal."""
    return np.sin(x * frequency + phase)

# Create data
y1 = sinusoid(frequency1)
y2 = sinusoid(frequency2, phase_shift)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Sine wave 1 (frequency={} Hz)'.format(frequency1))
plt.plot(x, y2, label='Sine wave 2 (frequency={} Hz, phase-shift={})'.format(frequency2, phase_shift))
plt.legend()
plt.title('Two Sine Waves Out of Phase')
plt.grid()
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.show()