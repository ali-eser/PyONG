import pygame

pygame.init()
pygame.display.set_caption('PyONG')
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
player1_pos = pygame.Vector2(screen.get_width() - (screen.get_width() / 1.01), screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width() / 1.01 - 7, screen.get_height() / 2)

print(screen.get_width() / 1.01)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(pygame.Color(41, 41, 51))
    p1 = pygame.draw.rect(screen, "whitesmoke", ((player1_pos), (7, screen.get_height() / 5.2)))
    p2 = pygame.draw.rect(screen, "whitesmoke", ((player2_pos), (7, screen.get_height() / 5.2)))
    pygame.draw.line(screen, pygame.Color(61, 61, 75), (screen.get_width() / 2 , 0), 
                    (screen.get_width() / 2, screen.get_height()), 3)
    circle = pygame.draw.circle(screen, "yellow", (screen.get_width() / 2, screen.get_height() / 2), 7)

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player1_pos.y -= 380 * dt
    if key[pygame.K_UP]:
        player2_pos.y -= 380 * dt
    if key[pygame.K_s]:
        player1_pos.y += 380 * dt
    if key[pygame.K_DOWN]:
        player2_pos.y += 380 * dt
    
    pygame.display.flip()
    clock.tick(60)
    dt = clock.tick(60) / 1000

pygame.quit()