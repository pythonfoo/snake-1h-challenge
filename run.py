"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random
from collections import deque
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

direction = "left"
snake = deque([(10, 5), (11, 5), (12, 5), (13,5), (14,5)])

point = (8,5)
tick_count=0

def update():
    global done
    global point
    d = {
        "left": (-1, 0),
        "right": (1, 0),
        "up": (0, -1),
        "down": (0, 1)
    }
    hx, hy = snake[0]

    dx, dy = d[direction]

    snake.appendleft((hx+dx, hy+dy))
    hx, hy = snake[0]

    if snake[0] == point:
        snake.pop()
        point = (random.choice(list(range(10))), random.choice(list(range(10))))
    print(point)
    
    # print(hx, hy, 0 > hx or hx > 13, 0 > hy or hy > 9)
    if 0 > hx or hx > 13 or 0 > hy or hy > 9:
        done = True
    if snake[0] in list(snake)[1:]:
        done = True


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_q:
                done = True

 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    for i in range(14):
        for j in range(10):
            pygame.draw.rect(screen, GREEN, (i*50, j*50, 49, 49))
    for x,y in snake:
        pygame.draw.rect(screen, RED, (x*50, y*50, 49, 49))
    x,y = point
    pygame.draw.rect(screen, RED, (x*50, y*50, 49, 49))
    tick_count += 1
    if tick_count > 30:
        tick_count = 0
        update()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

