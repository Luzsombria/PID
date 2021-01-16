import cv2
import numpy as np
import random

def generaRuido(imagen,porcentaje,nombre):
    img = cv2.imread(imagen, cv2.IMREAD_GRAYSCALE)
    rows, columns = img.shape
    imgRuido = np.zeros( (rows, columns), dtype = np.uint8)
    valorIN = random.randint(0,255)
    
    for x in range(0,rows):
        for y in range(0,columns):
            randomP = random.random()
            if randomP <= porcentaje:
                imgRuido[x,y] = valorIN
            else:
                imgRuido[x,y] = img[x,y]

    cv2.imwrite(imgRuido,nombre)