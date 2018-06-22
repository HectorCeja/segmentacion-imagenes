# -*- coding: utf-8 -*-
from PIL import Image , ImageFilter
from pylab import *
from numpy import *

import numpy as np
import matplotlib as mpl

@staticmethod
def imagen():
    imagen = Image.open('C:/Users/Public/Pictures/Sample Pictures/coca.jpg')
    #imshow(imagen)
    imagen.show()
    
    imagen_gris = Image.open('C:/Users/Public/Pictures/Sample Pictures/coca.jpg').convert('L')
    #imshow(imagen)
    imagen_gris.show()
    ima_fil = imagen.filter(ImageFilter.SHARPEN)
    #imshow(ima_fil)
    ima_fil.show()
    
@staticmethod
def distancia(color, promedio, covarianza):
    #ecuacion de mahalanobis
    d1 = (color-promedio.dot(linalg.inv(covarianza)))
    #multiplicar d2 contra d1 punto a punto con transport
    d2 = d1.dot((color-promedio).T)
    #obtener la raiz de mahalanobis que es la distancia
    d3 = sqrt(d2)
    
    return d3
    
@staticmethod
def mahalanobis():
    #convertir colores en valores numericos
    imagen = array(Image.open('C:/Users/Public/Pictures/Sample Pictures/coca.jpg'))
    #imagen de salida
    sal = imagen
    
    fil, col, capa = imagen.shape
    
    x = int(input('Cuantas muestras tomarás: '))
    #genera ventana
    figure()
    imshow(imagen)
    
    pos = int32(ginput(x))
    
    val = imagen[pos[:,1], pos[:,0]]

    cova = np.cov(val.T, ddof=0)
    pro = np.mean(val, axis=0)
    
    for i in range(fil):
        for j in range(col):
            pixel = imagen[i,j,:]
            DIS = distancia(pixel, pro, cova)
            if DIS > 15:
                sal[i,j,:] = 255
    
    figure()
    imshow(sal)
    show()


    #print('Fila: %s , Columna: %s, valores: %s' % (str(fil), str(col), str(val)))
    #show()
    

def main():
    
    mahalanobis()


if __name__ == "__main__":
    main()
