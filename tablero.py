import pygame
from colores import Colores

class Tablero:
    def __init__(self):
        self.num_filas = 20
        self.num_columnas = 10
        self.tamano_celda = 30
        self.tablero = [[0 for i in range(self.num_columnas)] for i in range(self.num_filas)]
        self.colores = Colores.dar_color_celda()

    def print_tablero(self):
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                print(self.tablero[fila][columna], end=" ")
            print()

    def esta_dentro(self, fila, columna):
        if fila >= 0 and fila < self.num_filas and columna >= 0 and columna < self.num_columnas:
            return True
        return False

    def esta_vacio(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            return True
        return False

    def fila_completa(self, fila):
        for columna in range(self.num_columnas):
            if self.tablero[fila][columna] == 0:
                return False
        return True

    def borrar_fila(self, fila):
        for columna in range(self.num_columnas):
            self.tablero[fila][columna] = 0

    def mover_fila_abajo(self, fila, num_filas):
        for columna in range(self.num_columnas):
            self.tablero[fila+num_filas][columna] = self.tablero[fila][columna]
            self.tablero[fila][columna] = 0

    def borrar_filas_completas(self):
        completa = 0
        for fila in range(self.num_filas-1,0,-1):
            if self.fila_completa(fila):
                self.borrar_fila(fila)
                completa += 1
            elif completa > 0:
                self.mover_fila_abajo(fila, completa)
        return completa

    def reiniciar(self):
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                self.tablero[fila][columna] = 0

    def dibujar_tablero(self, pantalla):
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                valor_celda = self.tablero[fila][columna]
                celda_rect = pygame.Rect(columna * self.tamano_celda + 11, fila * self.tamano_celda + 11,
                                         self.tamano_celda - 1, self.tamano_celda - 1)
                pygame.draw.rect(pantalla, self.colores[valor_celda], celda_rect)
