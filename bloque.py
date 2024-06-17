from colores import Colores
import pygame
from posicion import Posicion

class Bloque:
    def __init__(self, id):
        self.id = id
        self.celdas = {}
        self.tamano_celda = 30
        self.fila_offset = 0
        self.columna_offset = 0
        self.estado_rotacion = 0
        self.colores = Colores.dar_color_celda()

    def mover(self, filas, columnas):
        self.fila_offset += filas
        self.columna_offset += columnas

    def dar_posicion_celda(self):
        losas = self.celdas[self.estado_rotacion]
        losas_movidas = []
        for posicion in losas:
            posicion = Posicion(posicion.fila + self.fila_offset, posicion.columna + self.columna_offset)
            losas_movidas.append(posicion)
        return losas_movidas

    def rotar(self):
        self.estado_rotacion += 1
        if self.estado_rotacion == len(self.celdas):
            self.estado_rotacion = 0

    def deshacer_rotacion(self):
        self.estado_rotacion -= 1
        if self.estado_rotacion == 0:
            self.estado_rotacion = len(self.celdas) - 1

    def dibujar(self, pantalla, offset_x, offset_y):
        losas = self.dar_posicion_celda()
        for losa in losas:
            losa_rect = pygame.Rect(offset_x + losa.columna * self.tamano_celda, offset_y + losa.fila * self.tamano_celda,
                                    self.tamano_celda - 1, self.tamano_celda - 1)
            pygame.draw.rect(pantalla, self.colores[self.id], losa_rect)
