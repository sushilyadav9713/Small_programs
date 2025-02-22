import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple 2D Race Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 50, 50)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Car settings
car_width = 50
car_height = 100
car_x = WIDTH // 2 - car_width // 2  # Start in the middle of the road
car_y = HEIGHT - car_height - 20  # Positioned near the bottom
car_speed = 5

# Obstacle settings
obstacle_width = 50
obstacle_height = 100
initial_obstacle_speed = 5  # Initialize the speed of obstacles
obstacle_color = RED


# Function to draw the car
def draw_car(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, car_width, car_height))


# Function to draw an obstacle
def draw_obstacle(x, y):
    pygame.draw.rect(screen, obstacle_color, (x, y, obstacle_width, obstacle_height))


# Function to check for collisions
def detect_collision(car_x, car_y, obstacle_x, obstacle_y):
    if (
        car_y < obstacle_y + obstacle_height
        and car_y + car_height > obstacle_y
        and car_x < obstacle_x + obstacle_width
        and car_x + car_width > obstacle_x
    ):
        return True
    return False


# Main game loop
def game_loop():
    global car_x, car_y

    # Initial obstacle settings
    obstacle_x = random.randint(0, WIDTH - obstacle_width)
    obstacle_y = -obstacle_height
    obstacle_speed = initial_obstacle_speed  # Use initialized speed here

    score = 0
    game_over = False

    while not game_over:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Key input for car movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
            car_x += car_speed

        # Clear the screen
        screen.fill(WHITE)

        # Draw the car
        draw_car(car_x, car_y)

        # Move and draw the obstacle
        obstacle_y += obstacle_speed
        draw_obstacle(obstacle_x, obstacle_y)

        # Check if the obstacle goes off screen and reset it
        if obstacle_y > HEIGHT:
            obstacle_y = -obstacle_height
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            score += 1
            obstacle_speed += 1  # Gradually increase speed to make the game harder

        # Check for collision
        if detect_collision(car_x, car_y, obstacle_x, obstacle_y):
            print(f"Game Over! Final Score: {score}")
            game_over = True

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(120)


# Run the game loop
game_loop()
