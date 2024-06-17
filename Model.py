import random
import pygame
import os

from tablero import Tablero
from bloques import (
    IBloque, JBloque, LBloque, OBloque, SBloque, TBloque, ZBloque
)

class GameModel:
    def __init__(self):
        self.tablero = Tablero()
        self.bloques = [IBloque(),JBloque(),LBloque(),OBloque(),SBloque(),TBloque(),ZBloque()]  # Agrega bloques aquí
        self.bloque_actual = self.dar_bloque_random()
        self.siguiente_bloque = self.dar_bloque_random()
        self.game_over = False
        self.puntuacion = 0

        print("Ruta de trabajo actual:", os.getcwd())

        pygame.mixer.music.load("BackGroundMusic.ogg")
        pygame.mixer.music.play(-1)

    def actualizar_puntuacion(self, lineas_borradas, puntos_mover_abajo):
        if lineas_borradas == 1:
            self.puntuacion += 100
        elif lineas_borradas == 2:
            self.puntuacion += 300
        elif lineas_borradas == 3:
            self.puntuacion += 500
        self.puntuacion += puntos_mover_abajo

    def dar_bloque_random(self):
        if len(self.bloques) == 0:
            self.bloques = [IBloque(),JBloque(),LBloque(),OBloque(),SBloque(),TBloque(),ZBloque()]  # Agrega bloques aquí
        bloque = random.choice(self.bloques)
        self.bloques.remove(bloque)
        return bloque

    def mover_izquierda(self):
        self.bloque_actual.mover(0, -1)
        if not self.bloque_dentro() or not self.fijar_bloque():
            self.bloque_actual.mover(0, 1)

    def mover_derecha(self):
        self.bloque_actual.mover(0, 1)
        if not self.bloque_dentro() or not self.fijar_bloque():
            self.bloque_actual.mover(0, -1)

    def mover_abajo(self):
        self.bloque_actual.mover(1, 0)
        if not self.bloque_dentro() or not self.fijar_bloque():
            self.bloque_actual.mover(-1, 0)
            self.bloquear_bloque()

    def bloquear_bloque(self):
        losas = self.bloque_actual.dar_posicion_celda()
        for posicion in losas:
            self.tablero.tablero[posicion.fila][posicion.columna] = self.bloque_actual.id
        self.bloque_actual = self.siguiente_bloque
        self.siguiente_bloque = self.dar_bloque_random()
        filas_limpias = self.tablero.borrar_filas_completas()
        self.actualizar_puntuacion(filas_limpias, 0)
        if not self.fijar_bloque():
            self.game_over = True

    def fijar_bloque(self):
        losas = self.bloque_actual.dar_posicion_celda()
        for losa in losas:
            if not self.tablero.esta_vacio(losa.fila, losa.columna):
                return False
        return True

    def reiniciar(self):
        self.tablero.reiniciar()
        self.bloques = [IBloque(),JBloque(),LBloque(),OBloque(),SBloque(),TBloque(),ZBloque()]  # Agrega bloques aquí
        self.bloque_actual = self.dar_bloque_random()
        self.siguiente_bloque = self.dar_bloque_random()
        self.puntuacion = 0

    def rotar(self):
        self.bloque_actual.rotar()
        if not self.bloque_dentro() or not self.fijar_bloque():
            self.bloque_actual.deshacer_rotacion()

    def bloque_dentro(self):
        losas = self.bloque_actual.dar_posicion_celda()
        for losa in losas:
            if not self.tablero.esta_dentro(losa.fila, losa.columna):
                return False
        return True

    def dibujar(self, pantalla):
        self.tablero.dibujar_tablero(pantalla)
        self.bloque_actual.dibujar(pantalla, 11, 11)

        if self.siguiente_bloque.id == 3:
            self.siguiente_bloque.dibujar(pantalla, 300, 290)
        elif self.siguiente_bloque.id == 4:
            self.siguiente_bloque.dibujar(pantalla, 300, 270)
        else:
            self.siguiente_bloque.dibujar(pantalla, 310, 270)