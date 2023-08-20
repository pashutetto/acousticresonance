import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

f = ''  # file name
s,a = wavfile.read(f)

na = len(a)
a_k = np.fft.fft(a)[0:int(na/2)]/na 
a_k[1:] = 2*a_k[1:] 
Pxx = np.abs(a_k)  
f = s*np.arange((na/2))/na 

fig,ax = plt.subplots()
plt.plot(f,Pxx,'b-',label='Audio Signal')
plt.plot([20,20000],[0.1,0.1],'r-',alpha=0.7,\
         linewidth=10,label='Audible (Humans)')
ax.set_xscale('log'); ax.set_yscale('log')
plt.grid(); plt.legend()
plt.ylabel('Amplitude')
plt.xlabel('Frequency (Hz)')
plt.show()