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
class CharacterTable(object):
    """Given a set of characters:
    + Encode them to a one-hot integer representation
    + Decode the one-hot or integer representation to their character output
    + Decode a vector of probabilities to their character output
    """
    def __init__(self, chars):
        """Initialize character table.

        # Arguments
            chars: Characters that can appear in the input.
        """
        print(set(chars))
        self.chars = sorted(set(chars))
        print(chars)
        self.char_indices = dict((c, i) for i, c in enumerate(self.chars))
        self.indices_char = dict((i, c) for i, c in enumerate(self.chars))
    def encode(self, C, num_rows):
        """One-hot encode given string C.
        # Arguments
            C: string, to be encoded.
            num_rows: Number of rows in the returned one-hot encoding. This is
                used to keep the # of rows for each data the same.
        """
        #				5 		11
        x = np.zeros((num_rows*len(self.chars)))
        '''
        0 8
        1 0
        2 4
        '''
       	print(C)
        
       	for i, c in enumerate(C):
        	print("i {}  c {} in {}".format(i,c, enumerate(C)))
            	x[i*len(self.chars)+self.char_indices[c]] = 1

        

        '''
         1 2 3 4 5 6 7 8 9 0 +
       0 0 0 0 0 0 0 0 1 0 0 0 
       1 0 0 0 0 0 0 0 0 0 1 0 
       2 0 0 0 1 0 0 0 0 0 0 0 

        '''
        return x

    def decode(self, x, calc_argmax=True):
        """Decode the given vector or 2D array to their character output.
        # Arguments
            x: A vector or a 2D array of probabilities or one-hot representations;
                or a vector of character indices (used with `calc_argmax=False`).
            calc_argmax: Whether to find the character index with maximum
                probability, defaults to `True`.
        """
        if calc_argmax:
            x = x.argmax(axis=-1)
        return ''.join(self.indices_char[x] for x in x)
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
chars = '0123456789-'
ctable = CharacterTable(chars)
print("numero di righe {} colonne {}". format(len(auto),len(auto[0])))

x = np.zeros((len(auto), len(auto[0]), 5*len(chars)), dtype=np.bool)
for i in range(0, len(auto)):
	for j in range(0, len(auto[0])):
		x[i,j]= ctable.encode(str(auto[i,j]),5)
		
		print(x[i,j])


'''
y = np.zeros((len(questions), DIGITS + 1, len(chars)), dtype=np.bool)
for i, sentence in enumerate(questions):
    x[i] = ctable.encode(sentence, MAXLEN)
for i, sentence in enumerate(expected):
    y[i] = ctable.encode(sentence, DIGITS + 1)
matrix=np.concatenate((auto,bus,bici,train,metro,walk));
'''
print(matrix);
