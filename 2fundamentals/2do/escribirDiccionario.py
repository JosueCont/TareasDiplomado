import pickle
d={'Escribiendo un diccionario por josue Contreras Flores'}

with open('diccionario.bin','wb') as fh:
        pickle.dump(d,fh)

