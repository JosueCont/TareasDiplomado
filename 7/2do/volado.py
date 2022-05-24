import random
opciones=['cara','cruz']

lanzamientos=20
cara=0
cruz=0
    
for n in range(lanzamientos):
    tiro=random.choice(opciones)
    if tiro == 'cara':
        cara+=1
    else:
        cruz+=1

print("cara: ", cara)
print("cruz: ", cruz)


#tarea 3 Escoger una distribucion de random y usarla
# tarea 4 numpy elegir distribucion y hacer programa para generar eventos con la distribucion
