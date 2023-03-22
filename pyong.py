import pygame


def ball_physics():
    global bsx, bsy
    ball.x += bsx
    ball.y += bsy

    # Collision
    if ball.top <= 0 or ball.bottom >= screen.get_height():
        bsy *= -1
        audio()
    if p1.colliderect(ball) or p2.colliderect(ball):
        bsx *= -1
        audio()


def player_controls():
    global p1sp, p2sp


    if pygame.key.get_pressed()[pygame.K_w]:
        p1.y -= p1sp * dt
    if pygame.key.get_pressed()[pygame.K_UP]:
        p2.y -= p2sp * dt
    if pygame.key.get_pressed()[pygame.K_s]:
        p1.y += p1sp * dt
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        p2.y += p2sp * dt

    if p1.bottom >= screen.get_height():
        p1.bottom = screen.get_height()
    if p1.top <= 0:
        p1.top = 0
    if p2.bottom >= screen.get_height():
        p2.bottom = screen.get_height()
    if p2.top <= 0:
        p2.top = 0


def calc_score():
    global p1score, p2score, bsx, bsy, starter

    if ball.left <= 0:
        p2score += 1
        ball.center = screen.get_width() / 2 - 10, screen.get_height() / 2 - 10
        bsx *= -1
        bsy *= -1
        pygame.time.wait(200)
    if ball.right >= screen.get_width():
        p1score += 1
        ball.center = screen.get_width() / 2 - 10, screen.get_height() / 2 - 10
        bsx *= -1
        bsy *= -1
        pygame.time.wait(200)


def winner_screen():
    global starter, p1score, p2score

    if p1score >= 10:
        screen.fill(pygame.Color(41, 41, 51))
        p1victory = splash_font.render(f"Player 1 Won!", True, pygame.Color(120, 120, 150))
        play_again = text_font.render(f"Press SPACE to play again", True, pygame.Color(120, 120, 150))
        screen.blit(p1victory, p1victory.get_rect(center = screen.get_rect().center))
        screen.blit(play_again, play_again.get_rect(midbottom = screen.get_rect().midbottom))
        starter = 0
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            starter += 1
            p1score = 0
            p2score = 0
    elif p2score >= 10:
        screen.fill(pygame.Color(41, 41, 51))
        p2victory = splash_font.render(f"Player 2 Won!", True, pygame.Color(120, 120, 150))
        play_again = text_font.render(f"Press SPACE to play again", True, pygame.Color(120, 120, 150))
        screen.blit(p2victory, p2victory.get_rect(center = screen.get_rect().center))
        screen.blit(play_again, play_again.get_rect(midbottom = screen.get_rect().midbottom))
        starter = 0
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            starter += 1
            p1score = 0
            p2score = 0


def audio():
    ball_hit = pygame.mixer.Sound("./audio/ball_hit.wav")
    ball_hit.play()


pygame.mixer.pre_init(44100, -16, 2)
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('PyONG')
screen = pygame.display.set_mode((1280, 720), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=1)
clock = pygame.time.Clock()
p1 = pygame.Rect(screen.get_width() - (screen.get_width() / 1.01), screen.get_height() / 2, 7, screen.get_height() / 5.2)
p2 = pygame.Rect(screen.get_width() / 1.01 - 7, screen.get_height() / 2, 7, screen.get_height() / 5.2)
ball = pygame.Rect(screen.get_width() / 2 - 10, screen.get_height() / 2 - 10, 20, 20)
splash_font = pygame.font.SysFont(None, 250)
text_font = pygame.font.SysFont(None, 70)
p1score, p2score = 0, 0
bsx, bsy, p1sp, p2sp = 11, 11, 630, 630
starter = 1

# Gameplay loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw gameplay elements
    screen.fill(pygame.Color(41, 41, 51))

    # Start the game
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        starter += 1

    # Splash screen
    if starter == 1:
        splash_title = splash_font.render("PyONG!", True, pygame.Color(120, 120, 150))
        start_title = text_font.render("Press SPACE to start", True, pygame.Color(120, 120, 150))
        screen.blit(splash_title, splash_title.get_rect(center = screen.get_rect().center))
        screen.blit(start_title, start_title.get_rect(midbottom = screen.get_rect().midbottom))

    if starter > 1:
        score_text = splash_font.render(f"{p1score}            {p2score}", True, pygame.Color(120, 120, 150))
        screen.blit(score_text, score_text.get_rect(center = screen.get_rect().center))
        pygame.draw.rect(screen, "whitesmoke", p1, border_radius=5)
        pygame.draw.rect(screen, "whitesmoke", p2, border_radius=5)
        pygame.draw.line(screen, pygame.Color(61, 61, 75), (screen.get_width() / 2 , 0), 
                        (screen.get_width() / 2, screen.get_height()), 3)
        pygame.draw.ellipse(screen, "orangered", ball)

        # Add ball collision
        ball_physics()

        # Add controls
        player_controls()

        # Calculate score
        calc_score()

    # Render winner screen if a player scores 10
    winner_screen()

    # Render
    pygame.display.flip()

    # Set framerate
    clock.tick(240)

    # Run physics independent of framerate
    dt = clock.tick(80) / 1000

pygame.quit()