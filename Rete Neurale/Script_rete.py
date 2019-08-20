#libreria per leggere il file csv
import csv

PATH_DATASET_AUTO='../Dataset/Acquisizioni/Auto/Conversione/'
#righe per leggere il file csv
with open(PATH_DATASET_AUTO+'Acquisizione1.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
    	print(row)
       #creazione di una matrice di conversione?
       
    