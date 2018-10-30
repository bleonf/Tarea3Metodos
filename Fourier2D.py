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
fouriertotal=(fft.ifft2(img))

frecuencia=np.fft.fftfreq(len(fouriertotal[0]))

plt.figure("Fourier")
plt.plot(frecuencia,fouriertotal)
plt.savefig("LeonBenjamin_FT2D.pdf")
plt.show()



i=0
j=0
while j<256:
	while i<256:
		if ((fouriertotal[i,j]>0.03) and (fouriertotal[i,j]<0.08)):
			fouriertotal[i,j]=0
			i=i+1
		else:
			i=i+1
	j=j+1	
plt.figure("Fourier Filtrada")
plt.plot(frecuencia,fouriertotal)
plt.savefig("LeonBenjamin_FT2D_filtrada.pdf")
plt.show()


inversatotal=fft.ifft2(fouriertotal).real
#Utilizamos parte real
plt.figure("Imagen con filtro en  real")
plt.imshow(inversatotal,cmap="gray")
plt.savefig("LeonBenjamin_Imagen_filtrada.pdf")
plt.show()

#no supe como aplicar el filtro, ya que al hacer fourier me da con numeros complejos

