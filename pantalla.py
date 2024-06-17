import pygame
from colores import Colores

class ControladorPantalla():

    def setup(self):
        self.fuente_titulo = pygame.font.Font(None, 40)
        self.fondo_puntuacion = self.fuente_titulo.render("Puntuacion", True, Colores.blanco)
        self.siguiente_fondo = self.fuente_titulo.render("Siguiente", True, Colores.blanco)
        self.game_over_fondo = self.fuente_titulo.render("GAME OVER", True, Colores.blanco)

        self.siguiente_rect = pygame.Rect(360, 215, 170, 180)
        self.puntuacion_rect = pygame.Rect(360, 55, 170, 60)

        self.pantalla = pygame.display.set_mode((570, 620))
        pygame.display.set_caption("Tetris")
