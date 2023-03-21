import pygame
from pygame import gfxdraw

def ball_physics():
    global bsx, bsy
    ball.x += bsx
    ball.y += bsy
    
    # Collision
    if ball.top <= 0 or ball.bottom >= screen.get_height():
        bsy *= -1
    if p1.colliderect(ball) or p2.colliderect(ball):
        bsx *= -1

def player_controls():
    global p1s, p2s
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        p1.y -= p1s * dt
    if key[pygame.K_UP]:
        p2.y -= p2s * dt
    if key[pygame.K_s]:
        p1.y += p1s * dt
    if key[pygame.K_DOWN]:
        p2.y += p2s * dt
    if p1.bottom >= screen.get_height():
        p1.bottom = screen.get_height()
    if p1.top <= 0:
        p1.top = 0
    if p2.bottom >= screen.get_height():
        p2.bottom = screen.get_height()
    if p2.top <= 0:
        p2.top = 0


def calc_score():
    global p1score, p2score
    if ball.left <= 0:
        p2score += 1
        ball.center = screen.get_width() / 2 - 10, screen.get_height() / 2 - 10
    if ball.right >= screen.get_width():
        p1score += 1
        ball.center = screen.get_width() / 2 - 10, screen.get_height() / 2 - 10



pygame.init()
pygame.display.set_caption('PyONG')
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()
p1 = pygame.Rect(screen.get_width() - (screen.get_width() / 1.01), screen.get_height() / 2, 7, screen.get_height() / 5.2)
p2 = pygame.Rect(screen.get_width() / 1.01 - 7, screen.get_height() / 2, 7, screen.get_height() / 5.2)
ball = pygame.Rect(screen.get_width() / 2 - 10, screen.get_height() / 2 - 10, 20, 20)
font = pygame.font.SysFont(None, 72)
p1score, p2score = 0, 0
bsx, bsy, p1s, p2s = 8, 8, 550, 550

# Gameplay loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw gameplay elements
    screen.fill(pygame.Color(41, 41, 51))
    p1score_text = font.render(f"{p1score}", True, pygame.Color(150, 150, 200))
    p2score_text = font.render(f"{p2score}", True, pygame.Color(150, 150, 200))
    screen.blit(p1score_text, ((screen.get_width() / 2) - 120, 20))
    screen.blit(p2score_text, ((screen.get_width() / 2) + 60, 20))
    pygame.draw.rect(screen, "whitesmoke", p1, border_radius=5)
    pygame.draw.rect(screen, "whitesmoke", p2, border_radius=5)
    pygame.draw.line(screen, pygame.Color(61, 61, 75), (screen.get_width() / 2 , 0), 
                    (screen.get_width() / 2, screen.get_height()), 3)
    pygame.draw.ellipse(screen, "red", ball)

    # Add ball collision
    ball_physics()

    # Calculate score 
    calc_score()
    
    # Add controls
    player_controls()

    # Render
    pygame.display.flip()

    # Set framerate
    clock.tick(77)

    # Run physics independent of framerate
    dt = clock.tick(77) / 1000

pygame.quit()