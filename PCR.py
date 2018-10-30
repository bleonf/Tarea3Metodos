import numpy as np
import matplotlib.pylab as plt
from numpy import linalg 
datos=np.genfromtxt("WDBC.dat",delimiter=",", usecols=(0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31))
#matriz 569 por 31, quitamos la segunda columna que son letras
N=569.0
promfilas=np.zeros(569)
i=0
while(i<569):
	promfilas[i]=(np.sum(datos[i,:]))/569.0
	i=i+1

promcols=np.zeros(31)
i=0
while(i<31):
	promcols[i]=(np.sum(datos[:,i]))/31.0
	i=i+1

while(i<31):
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
while (i<31):
	print str(val[i])
	print str(vect[:,i])
	i=i+1
print "Los primeros 5 autovectores con autovalores 1.7x10**16, 155x10**6,10800, 1360 y 500 son los que tienen mayor covarianza y corresponden a las primeras 5 variables de los datos. "

diagnostico=np.genfromtxt("WDBC.dat", usecols=(0,1))
#lista con letras M para maligno y B para benigno
diagnosticofinal=diagnostico[:,1]
#binario es lista con 1 y 0 (booleano) correspondiente  las letras
binario=np.zeros(569)

i=0
while (i<569):
	if (diagnosticofinal[i]==B):
		binario[i]=1
		i=i+1
	else:
		i=i+1
print diagnosticofinal
print binario

		







	
