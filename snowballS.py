import os
import pygame

# Initialize Pygame
pygame.init()

# Constants
W, H = 940, 560
win = pygame.display.set_mode((W, H))
speed = 30

# Load Background Image
bg = pygame.image.load(os.path.join('img', 'bg64.png')).convert()
bg = pygame.transform.scale(bg, (W, H))

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('img', 'manC64.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 5
        self.vx = 0  # Horizontal velocity
        self.rect.x = 500  # Set the x-coordinate horizontal
        self.rect.y = 450  # Set the y-coordinate vertical

    def update(self, keys):
        if keys[pygame.K_a]:  # 'a' key for left movement
            self.vx = -self.speed  # Set velocity to move left
        elif keys[pygame.K_d]:  # 'd' key for right movement
            self.vx = self.speed  # Set velocity to move right
        else:
            self.vx = 0  # No key pressed, stop movement

        self.rect.x += self.vx

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Create Player
player = Player()

# Game Loop (Using Pygame for window and keyboard)
run = True
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Keyboard events
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Update
    player.update(keys)

    # Draw
    win.blit(bg, (0, 0))  # Draw the background
    player.draw(win)  # Draw the player

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
