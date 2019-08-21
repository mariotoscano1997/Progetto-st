'''allenamento rete neurale
	script di Mario Toscano, Giovanni Spina, Riccardo Chillemi
	'''	
#libreria per leggere il file csv
import csv
import numpy as np
PATH_DATASET_AUTO='../Dataset/Acquisizioni/Auto/Conversione/'
#righe per leggere il file csv
with open(PATH_DATASET_AUTO+'Acquisizione1.csv') as csv_file:
	csv_reader = csv.reader(csv_file)
	line_count = 0
	step=12
	frequency=24   
	i=0
	x=[]
	for row in csv_reader:
		if(i!=0):
			x.append(row)		
		i=1
#creazione matrice per mettere i record 24 a 24
y= np.zeros(((len(x)-24)/12+1, 24*3+1),dtype=int);
riga=0
#ciclo per sistemare la matrice
for i in range(0, len(x)-24,12):
	for j in range(0,24):
		y[riga,j*3]=x[i+j][0]
		y[riga,j*3+1]=x[i+j][1]
		y[riga,j*3+2]=x[i+j][2]
	y[riga,24*3]=x[i+j-1][3]
	riga=riga+1
#stampa della matrice
print(y)
#codifica della matrice in binario

