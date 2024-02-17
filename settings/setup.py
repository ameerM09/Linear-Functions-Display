from . import *

WIN_WIDTH = 500
WIN_HEIGHT = 625

CAPTION = "Linear Functions and Slopes"

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(CAPTION)

FPS = 60

SPACESHIP_WIDTH = 40
SPACESHIP_HEIGHT = 40

START_BTN_WIDTH = 100
START_BTN_HEIGHT = 40

RESTART_BTN_WIDTH = 40
RESTART_BTN_HEIGHT = 40

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (185, 185, 180)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (80, 0, 215)

FONT = pygame.font.SysFont("Comicsans", 20, bold = True, italic = True)
SMALL_FONT = pygame.font.SysFont("Comicsans", 15, italic = True)
