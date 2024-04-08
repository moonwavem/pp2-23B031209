import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collect Coins")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.Font(None, 36)

# Variables for player and coin
player_rect = pygame.Rect(50, SCREEN_HEIGHT//2, 50, 50)
coins = []
collected_coins = 0

# Function to generate a random coin
def generate_coin():
    x = random.randint(0, SCREEN_WIDTH - 50)
    y = random.randint(0, SCREEN_HEIGHT - 50)
    return pygame.Rect(x, y, 20, 20)

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    # Check for collision with coins
    for coin in coins[:]:
        if player_rect.colliderect(coin):
            coins.remove(coin)
            collected_coins += 1
    
    # Generate coins randomly
    if random.random() < 0.01:
        coins.append(generate_coin())
    
    # Draw player
    pygame.draw.rect(screen, YELLOW, player_rect)
    
    # Draw coins
    for coin in coins:
        pygame.draw.ellipse(screen, WHITE, coin)
    
    # Display collected coins
    text = font.render(f"Coins: {collected_coins}", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 10, 10))
    
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
