import pygame
from pantalla import ControladorPantalla
from Model import GameModel
from Presenter import GamePresenter
from colores import Colores

class GameView:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.controlador_pantalla = ControladorPantalla()
        self.presenter = GamePresenter(self.model)
        self.update_flag = pygame.USEREVENT

    def draw(self, pantalla):
        self.model.dibujar(pantalla)
        pygame.display.update()

    def run(self):
        self.controlador_pantalla.setup()
        pygame.time.set_timer(self.update_flag, 200)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.presenter.handle_event(event, self.update_flag)
            self.presenter.update(self.controlador_pantalla)
            self.draw(self.controlador_pantalla.pantalla)
            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    game_view = GameView()
    game_view.run()