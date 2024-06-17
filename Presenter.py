import pygame
from colores import Colores

class GamePresenter:
    def __init__(self, model):
        self.model = model

    def handle_event(self, event, update_flag):
        if event.type == pygame.KEYDOWN:
            if self.model.game_over:
                self.model.game_over = False
                self.model.reiniciar()
            if event.key == pygame.K_LEFT and not self.model.game_over:
                self.model.mover_izquierda()
            if event.key == pygame.K_RIGHT and not self.model.game_over:
                self.model.mover_derecha()
            if event.key == pygame.K_DOWN and not self.model.game_over:
                self.model.mover_abajo()
                self.model.actualizar_puntuacion(0, 1)
            if event.key == pygame.K_UP and not self.model.game_over:
                self.model.rotar()
        if event.type == update_flag and not self.model.game_over:
            self.model.mover_abajo()

    def update(self, controlador_pantalla):
        fondo_valor_puntuacion = controlador_pantalla.fuente_titulo.render(str(self.model.puntuacion), True, Colores.blanco)

        controlador_pantalla.pantalla.fill(Colores.azul_oscuro)
        controlador_pantalla.pantalla.blit(controlador_pantalla.fondo_puntuacion, (365, 20, 50, 50))
        controlador_pantalla.pantalla.blit(controlador_pantalla.siguiente_fondo, (375, 180, 50, 50))

        if self.model.game_over:
            controlador_pantalla.pantalla.blit(controlador_pantalla.game_over_fondo, (360, 490, 50, 50))

        pygame.draw.rect(controlador_pantalla.pantalla, Colores.azul_claro, controlador_pantalla.puntuacion_rect, 0, 10)
        controlador_pantalla.pantalla.blit(
            fondo_valor_puntuacion,
            fondo_valor_puntuacion.get_rect(
                centerx=controlador_pantalla.puntuacion_rect.centerx,
                centery=controlador_pantalla.puntuacion_rect.centery
            )
        )
        pygame.draw.rect(controlador_pantalla.pantalla, Colores.azul_claro, controlador_pantalla.siguiente_rect, 0, 10)