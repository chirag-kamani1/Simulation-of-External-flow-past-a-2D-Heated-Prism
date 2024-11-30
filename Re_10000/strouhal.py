import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

data = np.loadtxt('./postProcessing/forceCoeffs/0/coefficient.dat', skiprows=0)

L       = 1           # L = D - Diameter
V       = 1           # Velocity
time    = data[:,0]
Cd      = data[:,2]
Cl      = data[:,3]

# FFT

N       = len(time)
dt      = time[2] - time[1]

nmax=512                       # no. of points in the fft
freq, Cl_amp = signal.welch(Cl, 1./dt, nperseg=nmax)
plt.plot(freq, Cl_amp)         
plt.show() 

# # Strouhal Number
# Find the index corresponding to max amplitude
Cl_max_fft_idx = np.argmax(abs(Cl_amp))  
freq_shed      = freq[Cl_max_fft_idx ]
St             = freq_shed * L / V

print("Vortex shedding freq: %.3f [Hz]" % (freq_shed))
print("Strouhal Number: %.3f" % (St))
