import cv2
import numpy as np

blue = (255,0,0)
green = (0,255,0)
red = (0,0,255)

imagen = "home.jpg"
pick_imagen = cv2.imread(imagen)

filtro_imagen = np.full((pick_imagen.shape), red, np.uint8)
juntar_imagen = cv2.add(pick_imagen, filtro_imagen)
juntar_imagen = cv2.addWeighted(pick_imagen, 0.8, filtro_imagen, 0.2, 0)

cv2.imshow("Filtro", juntar_imagen)
cv2.waitKey(0)
