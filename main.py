import pygame
from os.path import join
from random import randrange

ANYA_SURFACE = pygame.image.load(join('Assets', 'anya.png'))
WIDTH, HEIGHT = ANYA_SURFACE.get_width(), ANYA_SURFACE.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Anya Forger')
pygame.display.set_icon(ANYA_SURFACE.convert_alpha())

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 20
clock = pygame.time.Clock()


class Color:
    def __init__(self):
        self.ran_color = (randrange(0, 256), randrange(0, 256), randrange(0, 256))

    def change(self):
        self.__init__()


def draw(color):
    WIN.fill(color)
    WIN.blit(ANYA_SURFACE, (0, 0))
    pygame.display.update()


def main() -> None:
    running = True
    color = Color()
    while running:
        clock.tick(FPS)
        draw(color.ran_color)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                color.change()
            if event.type == pygame.QUIT:
                running = False
                break
    pygame.quit()


if __name__ == '__main__':
    main()
