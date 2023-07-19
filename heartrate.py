#!/usr/bin/env python3

import numpy as np
from scipy import signal
from sklearn.decomposition import FastICA
import pyautogui
import time
from scipy.fft import fft, fftfreq
from scipy.signal import argrelextrema, medfilt2d
import matplotlib.pyplot as plt

delta_t = 0.01
total_time = 5.0
num_samples = int(total_time / delta_t)
old_pos = pyautogui.position()
data = []

print('start')
start_time = time.time()
for _ in range(num_samples):
	time.sleep(delta_t)
	new_pos = pyautogui.position()
	dx = new_pos[0] - old_pos[0]
	dy = new_pos[1] - old_pos[1]
	data.append([dx, dy])
	old_pos = new_pos
end_time = time.time()
print('end')
delta_t=(end_time-start_time)/num_samples

ica = FastICA(n_components=2)
ica_result = ica.fit_transform(data)
ica_result = medfilt2d(ica_result, kernel_size=3)
lowcut = 0.5
highcut = 8.0
nyquist = 0.5 / delta_t
low = lowcut / nyquist
high = highcut / nyquist
b, a = signal.butter(1, [low, high], btype='band')
filtered_data = signal.lfilter(b, a, ica_result, axis=0)

yf_x = fft(filtered_data[:, 0])
yf_y = fft(filtered_data[:, 1])
xf = fftfreq(num_samples, delta_t)
xf = xf[:num_samples//2]
combined_yf = yf_x + yf_y
mask = (xf > lowcut) & (xf < highcut)
peaks_indices = argrelextrema(np.abs(combined_yf[:num_samples//2][mask]), np.greater)
peaks_frequencies = xf[mask][peaks_indices]
top_three_peaks_frequencies = peaks_frequencies[np.argsort(-np.abs(combined_yf[:num_samples//2][mask][peaks_indices]))[:3]]
top_frequency = top_three_peaks_frequencies[0]

print(f"The top three peak frequencies are: {top_three_peaks_frequencies}")
print(f"Estimated BPM: {int(60*top_frequency)}")
plt.figure()
plt.subplot(4, 1, 1)
plt.title('Original Data')
plt.plot(data)
plt.subplot(4, 1, 2)
plt.title('ICA Transformed Data')
plt.plot(ica_result)
plt.subplot(4, 1, 3)
plt.title('Filtered Data')
plt.plot(filtered_data)
plt.subplot(4, 1, 4)
plt.title('Signal Frequencies')
plt.plot(xf, 2.0/num_samples * np.abs(combined_yf[:num_samples//2]))
plt.tight_layout()
plt.show()