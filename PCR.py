import numpy as np
import matplotlib.pylab as plt
from numpy import linalg 
datos=np.genfromtxt("WDBC.dat",delimiter=",", usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31))
#matriz 569 por 32
N=569*32
promfilas=np.zeros(569)
i=0
while(i<569):
	promfilas[i]=np.sum(datos[i,:])
	i=i+1

promcols=np.zeros(30)
i=0
while(i<30):
	promcols[i]=np.sum(datos[:,i])
	i=i+1
print promcols
	
