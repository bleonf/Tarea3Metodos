
import numpy as np
import matplotlib.pylab as plt
from numpy import fft 
import cmath 

a=np.genfromtxt("signal.dat",delimiter=",")
b=np.genfromtxt("incompletos.dat",delimiter=",")

signalx=a[:,0]
signaly=a[:,1]
nsignal=len(signalx)
freqssignal=np.fft.fftfreq(nsignal,(2*signalx[-1]))

incompx=b[:,0]
incompy=b[:,1]
nincomp=len(incompx)

plt.figure()
plt.plot(signalx,signaly)
plt.savefig("LeonBenjamin_signal.pdf")
plt.show

def fourier(senhal,j):
	i=0
	suma=0
	while (i<len(senhal)):
		suma=suma+(senhal[i]*(np.exp(2*np.pi*i*(freqssignal[j]))))
		i=i+1
	return suma
	
fouriersenhal=np.zeros(512)
i=0
while (i<512):
	fouriersenhal[i]=fourier(signaly,i)
	i=i+1
	
plt.plot(freqssignal,fouriersenhal)
plt.show()


	

	


	
