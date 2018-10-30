import numpy as np
import matplotlib.pylab as plt
from numpy import linalg 
datos=np.genfromtxt("WDBC.dat",delimiter=",", usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31))
#matriz 569 por 30, quitamos la segunda columna que son letras
N=569.0
promfilas=np.zeros(569)
i=0
while(i<569):
	promfilas[i]=(np.sum(datos[i,:]))/569.0
	i=i+1

promcols=np.zeros(30)
i=0
while(i<30):
	promcols[i]=(np.sum(datos[:,i]))/30.0
	i=i+1

while(i<30):
	datos[:,i]=datos[:,i]-promcols[i] #normaliza para que queden columnas centradas en 0
	i=i+1

#for i in range 

#multiplicamos por transpuesta

datos2=datos.transpose()

matrizcuadrada=np.matmul(datos2,datos)

cov=matrizcuadrada/569.0

val,vect=np.linalg.eig(cov)
i=0
print "Autovalores con autovector correspondiente"
while (i<30):
	print str(val[i])
	print str(vect[:,i])
	i=i+1
print "Los primeros 4 autovectores con autovalores 1665738.4, 10813, 1362.42 y 541.6 son los que tienen mayor covarianza y corresponden a las primeras 4 variables de los datos. "

diagnostico=np.genfromtxt("WDBC.dat", usecols=(0,1), delimiter=",",invalid_raise = False,dtype=unicode)
BM=diagnostico[:,1]
binario=np.zeros(569)
i=0
while(i<569):
	if (BM[i]=="B"):
		binario[i]=1
		i=i+1
	else:
		i=i+1
#arreglo con unos y ceros 1 para diagnostico beningno y 0 para maligno


PC1=vect[0]
PC2=vect[1]
PC1a=np.dot(datos,PC1)
PC2a=np.dot(datos,PC2)
plt.scatter(PC1a,PC2a,c=binario)

plt.savefig("LeonBenjamin_PCA.pdf")
plt.show()
print "En la grafica se ve claramente que los resultados benignos tienen una tendencia a estar por debajo de la linea principal de tendencia y los malignos por encima. Tambien vemos que no hay diagnosticos benignos hacia la parte mas negativa de la grafica."
		







	
