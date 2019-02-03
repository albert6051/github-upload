import sys

import pygame

# 12-4 implementation
def check_events():
    # Respond to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the program when close the window
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # print the event.key attribute whenever a pygame.KEYDOWN event
            print(event.key)