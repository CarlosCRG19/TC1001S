def filtroBGR(archivo,b,g,r):

    imagen = "home.jpg"
    pick_imagen = cv2.imread(imagen)

    filtro_imagen = np.full((pick_imagen.shape), (b,g,r), np.uint8)
    juntar_imagen = cv2.add(pick_imagen, filtro_imagen)
    juntar_imagen = cv2.addWeighted(pick_imagen, 0.8, filtro_imagen, 0.2, 0)

    return juntar_imagen
