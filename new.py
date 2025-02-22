import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Program")

# Set up colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Set up the rectangle (the "player" object)
rect_x = width // 2
rect_y = height // 2
rect_width = 50
rect_height = 50
rect_speed = 5

# Main game loop
running = True
while running:
    # Handle events (key presses, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the list of keys currently being pressed
    keys = pygame.key.get_pressed()

    # Move the rectangle based on arrow key inputs
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Ensure the rectangle stays within the window boundaries
    rect_x = max(0, min(rect_x, width - rect_width))
    rect_y = max(0, min(rect_y, height - rect_height))

    # Fill the screen with white color
    screen.fill(white)

    # Draw the rectangle (the "player" object)
    pygame.draw.rect(screen, blue, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
