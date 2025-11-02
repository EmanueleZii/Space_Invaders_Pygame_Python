'''
<summary>
   Classic VideoGame Space Invaders
   In Uso:
     Linguaggi:
        - Python3
      Librerie:
        - Pygame
        - Random
        - Math
</summary>
'''

import pygame
import random
import math
from pygame import mixer

#Inizializza Pygame
pygame.init()

#creazione di un schermo
screen = pygame.display.set_mode((600, 400))

clock = pygame.time.Clock()

#title window
pygame.display.set_caption("Space Invaders")

#icon della app
icon = pygame.image.load('asset/spaceship.png')
pygame.display.set_icon(icon)

#Background
background = pygame.image.load('asset/background.jpg')

# Background Music
mixer.music.load('asset/background.wav')
mixer.music.set_volume(0.3)
mixer.music.play()

#Player
playerimage = pygame.image.load('asset/Ship_1.png')

# Variabili Globali Player
player_speed = 2.3

playerX = 300
playerY = 300

# Bullet
bulletimage = pygame.image.load('asset/bullet.png')
bullet_speed = 40
bulletX = 285
bulletY = 265
bulletXchange = 0
bulletYchange = 10
bullet_state = "ready"

# Enemy
enemyimage = []
enemyX = []
enemyY = []
enemy_speed = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyimage.append(pygame.image.load('asset/Ship_3.png'))
    # Variabili Globali Enemy
    enemy_speed.append(2)
    enemyX.append(0)
    enemyY.append(random.randint(0, 300))

# Score punteggio
score = 0
#UI
font = pygame.font.Font('freesansbold.ttf', 20)

# Text on Screen
def draw_text(text, x, y, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Player Sprite
def player(x,y):
    screen.blit(playerimage,(x, y))
# Enemy
def Enemy(i):
    screen.blit(enemyimage[i], (enemyX[i], enemyY[i]))

# shoot system
def fire_Bullet(x,y):
    global bullet_state, bulletY
    bullet_state = "fire"
    screen.blit(bulletimage, (x+16, y+10))

# Enemy Movement
def enemyMovement():
    global enemyX, enemyY, enemy_speed, num_of_enemy, score
    global bulletX, bulletY, bullet_state
    for i in range(num_of_enemy):
        enemyX[i] += enemy_speed[i]

        # movement and wall per enemy
        if enemyX[i] <= 0 or enemyX[i] >= 580:
            enemy_speed[i] *= -1
            enemyY[i] += 20
        # Collision
        collision = IsCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision == True:
            explosion_sound = mixer.Sound('asset/explosion.wav')
            explosion_sound.set_volume(0.3)
            explosion_sound.play()
            bulletY = 285
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 300)
            enemyY[i] = random.randint(0, 300)

# Update the screen
def update():
    global bullet_state, bulletY, score, playerX, playerY, bulletX, bulletY
    global enemyX, enemyY
    # Color RGB display
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    #player
    player(playerX, playerY)
    control()
    #enemy
    for i in range(num_of_enemy):
        Enemy(i)

    enemyMovement()

    #Bullet movement
    if bullet_state == "fire":
        fire_Bullet(playerX, bulletY)
        bulletY -= bulletYchange
        if bulletY <= 0:
            bulletY = playerY
            bullet_state = "ready"

    #testo sullo schermo
    draw_text(f"Score: {score}", 250, 10)

    # update display
    pygame.display.update()

#Controlli Player
def control():

    global playerX, playerY
    global player_speed
    global enemyX, enemyY, bulletX, bulletY

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        playerX -= player_speed
    if key[pygame.K_RIGHT]:
        playerX += player_speed
    if key[pygame.K_UP]:
        playerY -= player_speed
    if key[pygame.K_DOWN]:
        playerY += player_speed
    if key[pygame.K_SPACE] and bullet_state == "ready":
        bulletX = playerX
        bulletY = playerY
        fire_Bullet(bulletX, bulletY)
        bulletsound = mixer.Sound('asset/laser.wav')
        bulletsound.set_volume(0.3)
        bulletsound.play()

    # Wall For The Player
    if playerX <= 0:
        playerX = 0
    if playerY <= -2.49:
        playerY = -2.49
    if playerY >= 340:
        playerY = 340
    if playerX >= 580:
        playerX = 580


def IsCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

#Game Loop
running = True
while running:
    clock.tick(60)
    update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False












