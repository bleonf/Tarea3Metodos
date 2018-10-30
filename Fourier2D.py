import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg 
import scipy.fftpack as fft

img = plt.imread("arbol.png")
#retorna matriz de numpy de 256x256


realfourier=(fft.ifft2(img)).real
#parte real
imagfourier=(fft.ifft2(img)).imag
#parte imaginara

plt.figure("fig2-Real")
plt.imshow(realfourier)
plt.savefig("LeonBenjamin_FT2D.pdf")
#Intento de filtro
i=0
j=0
while i<256:
	while j<256:
		if (abs(realfourier[i,j])>=0.001):
			realfourier[i,j]=0.0 #Al cambiar este numero se ven efectos en la imagen
			j=j+1
		else:
			j=j+1
	i=i+1
plt.figure("fig2-Real")
plt.imshow(realfourier)
plt.savefig("LeonBenjamin_FT2D_filtrada.pdf")

inversareal=fft.ifft2(realfourier)

i=0
j=0
while i<256:
	while j<256:
		if (abs(imagfourier[i,j])>=0.001):
			imagfourier[i,j]=0.0 #Al cambiar este numero se ven efectos en la imagen
			j=j+1
		else:
			j=j+1
	i=i+1
######################################
#plt.figure("fig3-imag")
#plt.imshow(imagfourier)
#plt.show()
#########################################


np.clip(imagfourier,-0.001,0.001)
np.clip(realfourier,-0.001,0.001)
inversareal=fft.ifft2(realfourier)
inversaimag=fft.ifft2(imagfourier)

inversatotal=fft.ifft2(realfourier).real
#Utilizamos parte real
plt.figure("Imagen con filtro en  real")
plt.imshow(inversatotal)
plt.savefig("LeonBenjamin_Imagen_filtrada.pdf")

#no supe como aplicar el filtro, ya que al hacer fourier me da con numeros complejos

