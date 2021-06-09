import sys

import pygame

# This module imports sys and pygame, which are used in the event cheking loop.
# The function needs no parameters at this point, and the body is copied from
# the event loop in alien_invasion.py

def chek_events():
    """Respond to keypresses and mouse events."""

    # Watch for keyboard and mouse events.
    # The for loop at is an event loop

    for event in pygame.event.get():
        # To access the event detected by Pygame, we'll use the pygame.event.get() method.
        # Any keyboard or mouse event will cause the for loop to run.
        # Inside the loop, we'll write a series of if statements to detect and respond to specific events.
        # For example, when the player clicks the game window's close button, a pygame.QUIT event is
        # detected and we call sys.exit() to exit the game.
        if event.type == pygame.QUIT:
            sys.exit()
