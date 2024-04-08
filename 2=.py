import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Direction
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.Font(None, 36)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.score = 0
        self.level = 1
        self.speed = 10

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*BLOCK_SIZE)) % SCREEN_WIDTH), (cur[1] + (y*BLOCK_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.level = 1
        self.speed = 10

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, WHITE, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.turn((1, 0))

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, WHITE, r, 1)

# Main game function
def main():
    snake = Snake()
    food = Food()

    while True:
        screen.fill(BLACK)
        snake.handle_keys()
        snake.move()

        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            if snake.score % 3 == 0:
                snake.level += 1
                snake.speed += 2  # Increase speed on level up
            food.randomize_position()

        snake.draw(screen)
        food.draw(screen)

        # Draw score and level
        text = font.render(f"Score: {snake.score} | Level: {snake.level}", True, WHITE)
        screen.blit(text, (10, 10))

        # Border collision check
        if snake.get_head_position()[0] < 0 or snake.get_head_position()[0] >= SCREEN_WIDTH \
                or snake.get_head_position()[1] < 0 or snake.get_head_position()[1] >= SCREEN_HEIGHT:
            snake.reset()

        pygame.display.update()
        clock.tick(snake.speed)

if __name__ == "__main__":
    main()
