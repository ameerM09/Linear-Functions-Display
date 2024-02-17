from . import *

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets/bg.png")), (WIN_WIDTH, WIN_HEIGHT))

SPACESHIP = pygame.transform.scale(pygame.image.load(os.path.join("assets/blue_spaceship.png")), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

BTN_SOUND_EFFECT = pygame.mixer.Sound("assets/btn_sound_effect.wav")

START_BTN = pygame.transform.scale(pygame.image.load(os.path.join("assets/start_btn.png")), (START_BTN_WIDTH, START_BTN_HEIGHT))
RESTART_BTN = pygame.transform.scale(pygame.image.load(os.path.join("assets/restart_btn.png")), (RESTART_BTN_WIDTH, RESTART_BTN_HEIGHT))

PLAY_SIMULATION_BTN = pygame.transform.scale(pygame.image.load(os.path.join("assets/play_simulation_btn.png")), (75, 35))

COIN_WIDTH = 50
COIN_HEIGHT = 50

COIN = pygame.transform.scale(pygame.image.load(os.path.join("assets/coin.png")), (COIN_WIDTH, COIN_HEIGHT))

UP_ARROW = pygame.image.load(os.path.join("assets/up_arrow.png"))
DOWN_ARROW = pygame.image.load(os.path.join("assets/down_arrow.png"))
