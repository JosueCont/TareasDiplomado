import pickle

with open('diccionario.bin','rb') as fh:
        d = pickle.load(fh) 

print(d)

