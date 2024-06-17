class Colores:

    gris_oscuro = (26, 31, 40)
    verde = (47, 230, 23)
    rojo = (232, 18, 18)
    naranja = (226, 116, 17)
    amarillo = (237, 234, 4)
    lila = (166, 0, 247)
    cyan = (21, 204, 209)
    azul = (13, 64, 216)
    blanco = (255, 255, 255)
    azul_oscuro = (44, 44, 127)
    azul_claro = (59, 85, 162)
    @classmethod
    def dar_color_celda(cls):
        return [cls.gris_oscuro, cls.verde, cls.rojo, cls.naranja, cls.amarillo,
                cls.lila, cls.cyan, cls.azul]


