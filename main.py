import pygame

pygame.init()

#creazione di un schermo
screen = pygame.display.set_mode((600, 400))

clock = pygame.time.Clock()

#title window
pygame.display.set_caption("Space Invaders")

#icon della app
icon = pygame.image.load('asset/spaceship.png')
pygame.display.set_icon(icon)

#Player
playerimage = pygame.image.load('asset/Ship_1.png')
playerX = 300
playerY = 320

#player sprite
def player():
    screen.blit(playerimage,(playerX, playerY))

#update the screen
def update():
    # rgb display
    screen.fill((0, 0, 20))
    player()
    pygame.display.update()

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()
















