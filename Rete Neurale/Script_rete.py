'''allenamento rete neurale
	script di Mario Toscano, Giovanni Spina, Riccardo Chillemi
	'''	
#libreria per leggere il file csv
import csv
import numpy as np
import os.path
PATH_DATASET_AUTO='../Dataset/Acquisizioni/Auto/Conversione/'
PATH_DATASET_BICI='../Dataset/Acquisizioni/Bici/Conversione/'
PATH_DATASET_BUS='../Dataset/Acquisizioni/Bus/Conversione/'
PATH_DATASET_WALK='../Dataset/Acquisizioni/Walk/Conversione/'
PATH_DATASET_TRAIN='../Dataset/Acquisizioni/Train/Conversione/'
PATH_DATASET_METRO='../Dataset/Acquisizioni/Metro/Conversione/'
#righe per leggere il file csv

#print(os.path.isfile(PATH_DATASET_AUTO+'Acquisizione{}.csv'.format(j)))
def getMatrix(path_dir):
	j=1
	x=[]
	while(os.path.isfile(path_dir+'Acquisizione{}.csv'.format(j))):
		with open(path_dir+'Acquisizione{}.csv'.format(j)) as csv_file:
			#print(csv_file)
			csv_reader = csv.reader(csv_file)
			line_count = 0
			step=12
			frequency=24   
			i=0
			for row in csv_reader:
				if(i!=0):
					x.append(row)		
				i=1
			#print(x)
			j=j+1
	#print(len(x))
	#creazione matrice per mettere i record 24 a 24
	y= np.zeros(((len(x)-24)/12+1, 24*3+1),dtype=int);
	riga=0
	#ciclo per sistemare la matrice
	for i in range(0, len(x)-23,12):
		for j in range(0,24):
			y[riga,j*3]=x[i+j][0]
			y[riga,j*3+1]=x[i+j][1]
			y[riga,j*3+2]=x[i+j][2]
		y[riga,24*3]=x[i+j-1][3]
		riga=riga+1
		
	#stampa della matrice
	return y
	#codifica della matrice in binario
auto=getMatrix(PATH_DATASET_AUTO)
bus=getMatrix(PATH_DATASET_BUS)
walk=getMatrix(PATH_DATASET_WALK)
train=getMatrix(PATH_DATASET_TRAIN)
metro=getMatrix(PATH_DATASET_METRO)
bici=getMatrix(PATH_DATASET_BICI)
'''
print(auto)
print(bus)
print(metro)
print(train)
print(walk)
print(bici)
'''
matrix=np.concatenate((auto,bus,bici,train,metro,walk));
print(matrix);