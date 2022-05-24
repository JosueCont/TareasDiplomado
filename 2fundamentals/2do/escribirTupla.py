import pickle
t=()
t=True,3.1,'Prueba','Josue contreras','Propietario'

with open('tupla.bin','wb') as fh:
        pickle.dump(t,fh)

