import csv
import numpy
import os

path = input("Inserisci il percorso delle acquisizioni:\n")
path2 = path+"/Conversione"
indexfile = 1
filecounter = -1

def getLabel(label):
    if(label==">Walk"):
        return 0
    if(label==">Car (driving)"):
        return 1
    if(label==">Car (passenger)"):
        return 1
    if(label==">car"):
        return 1
    if(label==">Bike"):
        return 2
    if(label==">Bus"):
        return 3
    if(label==">Metro"):
        return 4
    if(label==">Train"):
        return 5
    return -1


if(os.path.exists(path2)):
    print("Directory già esistente: Cancello i suoi file.\n")
    file_da_rimuovere = [f for f in os.listdir(path2)]
    for f in file_da_rimuovere :
       os.remove(path2+"/"+f)
else:
    os.makedirs(path2)

    
for filename in os.listdir(path):
    inputfile = filename
    inputm = []
    filecounter+=1
    if(os.path.isfile(path+"/"+inputfile)):
        with open(path+"/"+inputfile,"r") as file:
            reader = csv.reader(file, delimiter = ",")
            print("Leggo il file" +str(filecounter))
            line_count=0
            annotation = ""
            
            for row in reader:
                line_count+=1
                if (line_count<=2):
                    continue
                if(row[1] != ""):
                    annotation = row[1]
                    continue
                if(annotation == ""):
                    continue
                
                riga = [row[2],row[3],row[4],getLabel(annotation)]            
                inputm.append(riga)
        file.close()

        columns = ["AccX [mg]", "AccY", "AccZ", "Ground Truth"]
        with open(path2+"/"+"Acquisizione"+str(indexfile)+".csv", 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            print("Scrivo il file" +str(filecounter)+"\n")
            writer.writerow(columns)
            writer.writerows(inputm)
            indexfile+=1
        csvFile.close()
        
print("Ho terminato di scrivere i file")










