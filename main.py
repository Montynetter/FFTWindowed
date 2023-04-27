import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch


# Loading data from a file
data = np.loadtxt('path to input file')

# Splitting data into two columns
time = data[:, 0]
current = data[:, 1]

# Path to output folder
if not os.path.exists('Path to output folder'):
    os.makedirs('Path to output folder')


# Determining the length of the signal and the number of windows
signal_length = len(current)
n_windows = 1000

# Window size
window_size = signal_length // n_windows

# Creating arrays to store data for each window
freqs = np.zeros(n_windows)
amps = np.zeros(n_windows)

# Цикл по окнам
for i in range(n_windows):
    # Calculating the start and end indices for the current window
    start_index = i * window_size
    end_index = (i + 1) * window_size

    # Extracting the signal for the current window
    window_current = current[start_index:end_index]

    # Calculating the spectrum of the current window
    f, Pxx = welch(window_current, fs=1 / (time[1] - time[0]), nperseg=window_size)

    # Determining the index of maximum amplitude
    max_amp_index = np.argmax(Pxx)

    # Saving frequency and amplitude for the current window
    freqs[i] = f[max_amp_index]
    amps[i] = Pxx[max_amp_index]

    # Plotting a graph for the current window
    plt.figure()
    plt.plot(f, Pxx)
    plt.title(f'Window {i + 1}')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude')
    plt.xlim([0, 20])
    plt.savefig(f'window_{i + 1}.png') #path to folder past in format C:\\Users\\username\\...\\window_{i + 1}.png
    plt.close()

# Plotting a graph of frequency dependence on the window number
plt.figure()
plt.plot(freqs)
plt.title('Dependence of Frequency on Window Number')
plt.xlabel('Window Number')
plt.ylabel('Frequency [Hz]')
plt.ylim([0, 20])
plt.savefig('freq_vs_window.png') # Path to folder past in format C:\\Users\\username\\...\\freq_vs_window.png
plt.close()

# Plotting a graph of amplitude dependence on the window number
plt.figure()
plt.plot(amps)
plt.title('Dependence of Amplitude on Window Number')
plt.xlabel('Window Number')
plt.ylabel('Amplitude')
plt.savefig('amp_vs_window.png') # Path to folder past in format C:\\Users\\username\\...\\amp_vs_window.png
plt.close()