#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import pandas as pd
from PIL import Image
from scipy.misc import imsave

NFFT = 120     # the length of the windowing segments
Fs = 500  # the sampling rate
OVERLAP = NFFT/8

# time1 = np.arange(0,5,0.0001, dtype=np.complex64)
# time = np.arange(0,15,0.0001, dtype=np.complex64)
# time1 = np.linspace(0,5,num=64*NFFT, dtype=np.complex64)
# time = np.linspace(0,15,num=64*NFFT, dtype=np.complex64)
# data1=np.sin(2*np.pi*300*time1)
# data2=np.sin(2*np.pi*600*time1)
# data3=np.sin(2*np.pi*900*time1)
# data=np.append(data1,data2 )
# data=np.append(data,data3)
# data=np.append(data,data1)

time = np.linspace(0,5,num=64*NFFT, dtype=np.complex64)
data=np.sin(2*np.pi*300*time)
# print len(time)
# print len(data)


# plot signal and spectrogram

# plt.gray()
# fig = plt.figure(frameon=False)
# fig = plt.figure(1)
# ax = plt.Axes(fig, [0., 0., 1., 1.,])
# ax = plt.Axes(fig, [0., 0., 1., 1.,])
# ax = plt.gca()
# ax.set_axis_off()
# fig.add_axes(ax)
# ax1 = plt.subplot(211)
# plt.plot(time,data)   # for this one has to either undersample or zoom in
# plt.xlim([0,15])
# plt.subplot(212 )  # don't share the axis
# Pxx, freqs, bins, im = plt.specgram(data, NFFT=NFFT,   Fs=Fs,noverlap=100, cmap=plt.cm.gist_heat)

# Check the spectrogram from matplotlib
# Pxx, freqs, bins, im = plt.specgram(data, NFFT=NFFT,   Fs=Fs, window=np.hamming(NFFT), noverlap=OVERLAP, cmap=plt.gray(), sides='twosided')
# Pxx, freqs, bins, im = plt.specgram(data, NFFT=NFFT,   Fs=Fs, window=np.hamming(NFFT), cmap=plt.gray(), sides='twosided')

# print("Data shape: ", data.shape)
# print("Pxx shape: ", Pxx.shape)
# print("Freqs shape: ", freqs.shape)
# ax.set_adjustable(adjustable='box-forced')
# fig.savefig('test.jpg', dpi=100)
# plt.close()
# Now check the spectrogram from scipy
g = plt.figure()
# g = plt.figure(2)
f, t, Sxx = signal.spectrogram(data, Fs, mode='magnitude', return_onesided=False, nperseg=64, noverlap=0)
plt.pcolormesh(t, f, Sxx)
print("Sxx shape: ", Sxx.shape)
print("f shape: ", f.shape)
print("t shape: ", t.shape)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')

# h = plt.figure(3)
f1, t1, Sxx1 = signal.spectrogram(data, Fs, mode='magnitude', window=np.hamming(NFFT),return_onesided=False, nperseg=None)
# plt.pcolormesh(t1, f1, Sxx1)
print("Sxx1 shape: ", Sxx1.shape)
print("f1 shape: ", f1.shape)
print("t1 shape: ", t1.shape)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

# result = Image.fromarray(Sxx, mode='L')
gmi = 255 - Sxx
print(Sxx)
print(Sxx[1])
Sxx_scaled = Sxx * 255.0 / np.amax(Sxx)
print(Sxx_scaled)
imsave('out.jpg', Sxx_scaled)


# result = Image.fromarray(Sxx)
# result.show()
# result.save('out.jpg')

# Calculate average of the 120 FFTs generated by the spectrogram
# avgd = np.zeros(64, dtype=np.complex64)
avgd = np.average(Sxx_scaled, axis=1)
print(avgd)
print(avgd.shape)

mouse = np.vstack((avgd, avgd))
print(mouse)
print(mouse.shape)



# TODO: understand the other returned values from plt.specgram and from
# scipy.signal.spectrogram and compare the returned values
# Check if they are matrixes - useful for later averaging




