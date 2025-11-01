'''
<summary>
   Classic VideoGame Space Invaders
   Use:
     - Python3
     - Pygame
</summary>
'''

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
# Variabili Globali Player
speed = 0.1
playerX = 300
playerY = 300

# Enemy
enemyimage = pygame.image.load('asset/Ship_3.png')
# Variabili Globali Enemy
speed = 0.1
enemyX = 300
enemyY = 48

#UI
font = pygame.font.Font('freesansbold.ttf', 10)

#text
def draw_text(text, x, y, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

#player sprite
def player(x,y):
    screen.blit(playerimage,(x, y))

def Enemy(x,y):
    screen.blit(enemyimage, (x, y))

#update the screen
def update():
    # rgb display
    screen.fill((0, 0, 20))
    player(playerX, playerY)
    Enemy(enemyX, enemyY)
    Control()
    draw_text(f"Posizione: {playerX}, {playerY}", 10, 10)
    pygame.display.update()

#Controlli player
def Control():

    global playerX, playerY
    global speed

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        playerX -= speed
    if key[pygame.K_RIGHT]:
        playerX += speed
    if key[pygame.K_UP]:
        playerY -= speed
    if key[pygame.K_DOWN]:
        playerY += speed

    #Muri
    if playerX <= 0:
        playerX = 0
    if playerY <= -2.49:
        playerY = -2.49
    if playerY >= 340:
        playerY = 340
    if playerX >= 580:
        playerX = 580

#Game Loop
running = True
while running:
    update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




















