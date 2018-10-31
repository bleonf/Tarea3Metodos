import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg 
import scipy.fftpack as fft
from scipy import ndimage

img = plt.imread("arbol.png")
#retorna matriz de numpy de 256x256

fourier=(fft.ifft2(img))

frecuencia=np.fft.fftfreq(len(fourier[0].real))

plt.figure("Fourier")
plt.plot(frecuencia,fourier)
plt.savefig("LeonBenjamin_FT2D.pdf")


#filtro, quitamos la locacion exacta en las frecuencias donde se hallaba el ruido
#los tres errores que bota el ejercicio son señales de precaucion al usuario por que no estamos teniendo en cuenta la parte imaginaria de la transformada	
i=0
while i<256:
		if ((abs(frecuencia[i].real)>0.24 and abs(frecuencia[i].real)<0.26)or(abs(frecuencia[i].real)>0.038 and abs(frecuencia[i].real)<0.043)):
			fourier[i]=0
			i=i+1
		else:
			i=i+1
plt.figure("Fourier Filtrada")
plt.plot(frecuencia,fourier)
plt.savefig("LeonBenjamin_FT2D_filtrada.pdf")



inversatotal=fft.ifft2(fourier).real
#Utilizamos parte real
plt.figure("Imagen Filtrada")
plt.imshow(inversatotal,cmap="gray",origin="lower")
#utilizamos origin porque la imagen sali al revez
plt.savefig("LeonBenjamin_Imagen_filtrada.pdf")



