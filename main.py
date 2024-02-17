from settings import *

class Spaceship():
    VEL = 2

    def __init__(self, x, y, asset):
        self.x = x
        self.y = y
        self.asset = asset
        self.vel = self.VEL

        self.change_in_x = 0
        self.change_in_y = 0

    def draw(self, win):
        win.blit(self.asset, (self.x, self.y))

    def key_bindings(self, on_key_pressed):
        if on_key_pressed[pygame.K_UP] or on_key_pressed[pygame.K_w]:
            if self.y >= 0:
                self.y = self.y - self.vel

                self.change_in_y = self.change_in_y + 1

        elif on_key_pressed[pygame.K_DOWN] or on_key_pressed[pygame.K_s]:
            if self.y <= WIN_HEIGHT - SPACESHIP_HEIGHT * 3:
                self.y = self.y + self.vel

                self.change_in_y = self.change_in_y - 1

        elif on_key_pressed[pygame.K_RIGHT] or on_key_pressed[pygame.K_d]:
            if self.x <= WIN_WIDTH - SPACESHIP_WIDTH:
                self.x = self.x + self.vel
                
                self.change_in_x = self.change_in_x + 1

        elif on_key_pressed[pygame.K_LEFT] or on_key_pressed[pygame.K_a]:
            if self.x >= 0:
                self.x = self.x - self.vel

                self.change_in_x = self.change_in_x - 1

    def get_mask(self):
        return pygame.mask.from_surface(self.asset)

class Button():
    def __init__(self, x, y, btn_image):
        self.btn_image = btn_image
        self.rect = self.btn_image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def check_for_click(self):
        action = False

        cursor_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(cursor_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        return action

    def draw(self, win):
        win.blit(self.btn_image, (self.rect.x, self.rect.y))

class Coin():
    ASSET = COIN

    def __init__(self, pos):
        self.pos = pos
        self.asset = self.ASSET

    def draw(self, win):
        win.blit(self.asset, (self.pos))

    def get_mask(self):
        return pygame.mask.from_surface(self.asset)

def interactive_bar_functionality(win, input_slope, spaceship):
    interactive_bar = pygame.Rect((0, WIN_HEIGHT - 125), (WIN_WIDTH, 125))
    pygame.draw.rect(win, GRAY, interactive_bar)

    slope_equation = f"y = {input_slope}x + b"

    slope_text = FONT.render(slope_equation, 1, PURPLE)
    win.blit(slope_text, (15, WIN_HEIGHT - slope_text.get_height() * 2))

    tip_text1 = SMALL_FONT.render("Follow the coin to", 1, PURPLE)
    win.blit(tip_text1, (WIN_WIDTH - tip_text1.get_width() * 1.15, WIN_HEIGHT - 62.5))

    tip_text2 = SMALL_FONT.render("create the slope path!", 1, PURPLE)
    win.blit(tip_text2, (WIN_WIDTH - tip_text2.get_width() * 1.115, WIN_HEIGHT - 42.5))

    x_pos1 = [
        0, 
        WIN_WIDTH * 0.25, 
        WIN_WIDTH * 0.34, 
        WIN_WIDTH * 0.37, 
        WIN_WIDTH * 0.4
    ]

    x_pos1_index = -1

    x_pos2 = [
        WIN_WIDTH, 
        WIN_WIDTH * 0.75, 
        WIN_WIDTH * 0.66, 
        WIN_WIDTH * 0.63, 
        WIN_WIDTH * 0.6
    ]

    x_pos2_index = -1

    positive_coin_coords = [
        (275, 180),
        (275, 130),
        (275, 80),
        (275, 30),
        (275, 0)
    ]

    negative_coin_coords = [
        (275, 280),
        (275, 330),
        (275, 380),
        (275, 430),
        (275, 450)
    ]

    positive_coin_pos_index = -1
    negative_coin_pos_index = -1

    for slope in range(1, 6):
        x_pos1_index = x_pos1_index + 1
        x_pos2_index = x_pos2_index + 1

        positive_coin_pos_index = positive_coin_pos_index + 1
        negative_coin_pos_index = negative_coin_pos_index + 1

        if slope_equation == f"y = {slope}x + b":
            pygame.draw.line(win, BLUE, (x_pos1[x_pos1_index], WIN_HEIGHT - 125), (x_pos2[x_pos2_index], 0), width = 5)

            positive_coin = Coin(positive_coin_coords[positive_coin_pos_index])

            positive_coin.draw(win)

        if slope_equation == f"y = -{slope}x + b":
            pygame.draw.line(win, RED, (x_pos1[x_pos1_index], 0), (x_pos2[x_pos2_index], WIN_HEIGHT - 125), width = 5)

            negative_coin = Coin(negative_coin_coords[negative_coin_pos_index])

            negative_coin.draw(win)
                
    if slope_equation == "y = 0x + b":
        pygame.draw.line(win, GREEN, (0, WIN_HEIGHT // 2 - 60), (WIN_WIDTH, WIN_HEIGHT // 2 - 60), width = 5)

def draw_grid(width, rows, win):
    size_btwn = width // rows

    x = 0
    y = 0

    for pos in range(rows):
        x = x + size_btwn
        y = y + size_btwn

        pygame.draw.line(win, (WHITE), (x, 0), (x, width))
        pygame.draw.line(win, (WHITE), (0, y), (width, y))

    label_x = FONT.render("x", 1, WHITE)
    win.blit(label_x, (0, WIN_HEIGHT // 2 - 60))

    label_y = FONT.render("y", 1, WHITE)
    win.blit(label_y, (WIN_WIDTH // 2 - 15, 0))

def draw_challenges(win, rise_over_run_challenges, challenge_index):
    for slope in range(-5, 6):
        rise_over_run_challenges.append(f"Follow the rise/run path for y = {slope}x + b")

    challenge_text = FONT.render(rise_over_run_challenges[challenge_index], 1, PURPLE)
    win.blit(challenge_text, (WIN_WIDTH // 2 - challenge_text.get_width() // 2, 510))

def main_loop():
    run = True
    refresh_rate = pygame.time.Clock()

    spaceship = Spaceship(WIN_WIDTH // 2 - SPACESHIP.get_width() // 2, WIN_HEIGHT // 2 - SPACESHIP.get_height() * 2.15, SPACESHIP)

    input_slope = 0

    rise_over_run_challenges = []

    challenge_index = 5

    while run:
        refresh_rate.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        increase_slope_arrow = Button(60, 555, UP_ARROW)

        decrease_slope_arrow = Button(60, 600, DOWN_ARROW)

        challenge_btn = Button(WIN_WIDTH // 2 - START_BTN.get_width() + 10, 565, START_BTN)

        restart_btn = Button(WIN_WIDTH // 2 + RESTART_BTN.get_width() // 2, 565, RESTART_BTN)

        if increase_slope_arrow.check_for_click() and input_slope <= 4:
            pygame.time.delay(500)
            input_slope = input_slope + 1

        if decrease_slope_arrow.check_for_click() and input_slope >= -4:
            pygame.time.delay(500)
            input_slope = input_slope - 1

        on_key_pressed = pygame.key.get_pressed()

        spaceship.key_bindings(on_key_pressed)

        WIN.blit(BG, (0, 0))

        draw_grid(WIN_WIDTH, 10, WIN)

        if challenge_btn.check_for_click():
            pygame.time.delay(500)
            BTN_SOUND_EFFECT.play()

            spaceship.x, spaceship.y = WIN_WIDTH // 2 - SPACESHIP.get_width() // 2, WIN_HEIGHT // 2 - SPACESHIP.get_height() * 2.15
            challenge_index = random.randrange(len(rise_over_run_challenges))

        if restart_btn.check_for_click():
            main_loop()

        interactive_bar_functionality(WIN, input_slope, spaceship)

        draw_challenges(WIN, rise_over_run_challenges, challenge_index)

        spaceship.draw(WIN)

        increase_slope_arrow.draw(WIN)
        decrease_slope_arrow.draw(WIN)
        challenge_btn.draw(WIN)
        restart_btn.draw(WIN)

        pygame.display.update()

if __name__ == "__main__":
    main_loop()