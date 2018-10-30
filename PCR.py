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

diagnostico=np.genfromtxt("WDBC.dat", usecols=(1), delimiter=",",invalid_raise = False)
#lista con letras M para maligno y B para benigno
#diagnosticofinal=diagnostico[:,1]
#binario es lista con 1 y 0 (booleano) correspondiente  las letras
binario=np.zeros(569)
i=0
while (i<569):
	if (diagnostico[i]=="B"):
		binario[i]=1
		i=i+1
	else:
		i=i+1

plt.figure("PC1,PC2")
plt.scatter(datos[:,0],datos[:,1],c=datos[:,0])
#diferente color segun su posicion en la grafica, no sabia como hacer para pasar de una lista de strings a binario y hacer eso para los datos de la figura
plt.savefig("LeonBenjamin_PCA.pdf")
print "Segun los resultados de la grafica, aunque no estoy seguro de cuales resultados son benignos y cuales malignos(ver comentarios),puedo suponer que la tendencia clara que hay entre PC1 y PC2 nos lleva a concluir que si se puede utilizar el metodo de PCA como medida de prevencion a pacientes de cancer aunque tal vez no como una medida absoluta para dignosticar."
		







	
