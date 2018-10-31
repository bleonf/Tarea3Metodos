
import numpy as np
import matplotlib.pylab as plt
import scipy as sci
from numpy import fft 
from scipy.interpolate import interp1d

a=np.genfromtxt("signal.dat",delimiter=",")
b=np.genfromtxt("incompletos.dat",delimiter=",")

signalx=a[:,0]
signaly=a[:,1]
nsignal=len(signalx)
fsignal=np.fft.fftfreq(nsignal,(signalx[-1]-signalx[-2]))
print "Se utiliza el paquete fft.fftfreq de numpy con un dt de la diferencia de las dos frcuencias mas grandes de los datos"

print (fsignal)
print (f1signal)

incompx=b[:,0]
incompy=b[:,1]
nincomp=len(incompx)

plt.figure("fig1")
plt.plot(signalx,signaly)
plt.savefig("LeonBenjamin_signal.pdf")


def fourier(senhal,k):
	i=0
	suma=0
	while (i<len(senhal)):
		suma=suma+(senhal[i]*((np.e)**((-1j)*2.0*np.pi*i*(k/512.0))))
		i=i+1
	return suma
#fourier de senhal	
fouriersignal=np.zeros(512)
i=0
while (i<512):
	fouriersignal[i]=fourier(signaly,i)
	i=i+1

plt.figure("fig2")	
plt.plot(np.abs(fsignal),(fouriersignal))
plt.savefig("LeonBenjamin_TF.pdf")


print "las frecuencias principales se encuentran en 210 ,138 ,245 y 388 hz"

#filtro pasa bajos
i=0
while (i<512):
	if (np.abs(fsignal[i])>1000):
		fouriersignal[i]=0.0
		i=i+1
	else:
		i=i+1

plt.figure("fig3")	
plt.plot(np.abs(fsignal),(fouriersignal))
plt.savefig("LeonBenjamin_filtrada.pdf")

fcubica=sci.interpolate.interp1d(incompx,incompy,kind="cubic")
fcuadratica=sci.interpolate.interp1d(incompx,incompy,kind="quadratic")

t=np.linspace(min(incompx),max(incompx),512)
fcubt=fcubica(t)
fcuadt=fcuadratica(t)
#fourier de interpolacion cubica
fouriercub=np.zeros(512)
i=0
while (i<512):
	fouriercub[i]=fourier(fcubt,i)
	i=i+1
freqcub=np.fft.fftfreq(512,t[-1]-t[-2])
#fourier de interpolacion cuadratica
fouriercuad=np.zeros(512)
i=0
while (i<512):
	fouriercuad[i]=fourier(fcuadt,i)
	i=i+1
freqcuad=np.fft.fftfreq(512,t[-1]-t[-2])


plt.figure("LeonBenjamin_TF_interpola")
plt.subplot(3,1,1)
plt.plot(np.abs(fsignal),(fouriersignal))
plt.xlabel("Frecuencia(hz)")
plt.ylabel("Amplitud-Senhal")

plt.subplot(3,1,2)
plt.plot(np.abs(freqcuad),fouriercuad)
plt.xlabel("Frecuencia(hz)")
plt.ylabel("Amplitud-Cuad")

plt.subplot(3,1,3)
plt.plot(np.abs(freqcub),fouriercub)
plt.xlabel("Frecuencia(hz)")
plt.ylabel("Amplitud-Cubica")

plt.tight_layout()
plt.savefig("LeonBenjamin_TF_interpola.pdf")

print "En la transformada de las interpolaciones falta un pico completo que en la transformada de la senhal es el tercero mas grande."

#arreglos en blanco para ser llenados
cubica1000=np.zeros(512)
cubica500=np.zeros(512)
cuad1000=np.zeros(512)
cuad500=np.zeros(512)
signal500=np.zeros(512)

#funcion para aplicar cualquier filtro a cualquiera de los arreglos
def filtro(signal,arreglo,freq):
	i=0
	while (i<512):
		if (np.abs(freqcuad[i])>freq):
			arreglo[i]=0.0
			i=i+1
		else:
			arreglo[i]=signal[i]
			i=i+1	
filtro(fouriercub,cubica1000,1000)
filtro(fouriercub,cubica500,500)
filtro(fouriercuad,cuad1000,1000)
filtro(fouriercuad,cuad500,500)
filtro(fouriersignal,signal500,500)

plt.figure("LeonBenjamin_2Filtros")
plt.subplot(2,1,1)
plt.plot(np.abs(fsignal),(fouriersignal),c="green")
plt.plot(np.abs(freqcuad),cuad1000,c="blue")
plt.plot(np.abs(freqcub),cubica1000,c="red")
plt.xlabel("Frecuencia(hz)")
plt.ylabel("Amplitud-filtro1000")

plt.subplot(2,1,2)
plt.plot(np.abs(fsignal),(signal500),c="green")
plt.plot(np.abs(freqcuad),cuad500,c="blue")
plt.plot(np.abs(freqcub),cubica500,c="red")
plt.xlabel("Frecuencia(hz)")
plt.ylabel("Amplitud-filtro500")

plt.tight_layout()
plt.savefig("LeonBenjamin_2Filtros.pdf")
	


	
