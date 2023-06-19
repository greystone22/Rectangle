# This script is supposed to display a rectangle going around the screen

import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Rectangle")

# Set the initial position and dimensions of the rectangle
rect_width = 50
rect_height = 30
rect_x = random.randint(0, screen_width - rect_width)
rect_y = random.randint(0, screen_height - rect_height)

# Set the initial movement direction of the rectangle
dx = 5
dy = 5

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the position of the rectangle
    rect_x += dx
    rect_y += dy

    # Check if the rectangle reaches the screen boundaries
    if rect_x <= 0 or rect_x >= screen_width - rect_width:
        dx *= -1
    if rect_y <= 0 or rect_y >= screen_height - rect_height:
        dy *= -1

    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Draw the rectangle
    pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
