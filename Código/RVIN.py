import cv2
import numpy as np

def generaRuido(imagen,porcentaje,nombre):
    img = cv2.imread(imagen)
    gauss = np.random.normal(0,1,img.size)
    gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')

    img_gauss = cv2.add(img,gauss)

    cv2.imwrite(imgRiudo,nombre)