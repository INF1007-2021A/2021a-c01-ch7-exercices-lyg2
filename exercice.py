#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pow, pi
#il faut importer le fichier pour l'exercice2
#Il faut utiliser la fontion récursive.

# TODO: Définissez vos fonction ici
def ellipsoide(axe_x=10, axe_y=10, axe_z=10,masse_vol=5):
    volume=4*pi*axe_x*axe_y*axe_z/3
    masse=volume/masse_vol
    tuple=(volume, masse)
    return tuple
#Turle: on utilise les fonctions setheading, color, pensize, left, right, backward

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    k=ellipsoide(2,4,6,10)
    print("La volume est: ", k[0], "\n" "La masse est: ", k[1])
    pass
