import sys

import pygame

# This module imports sys and pygame, which are used in the event cheking loop.
# The function needs no parameters at this point, and the body is copied from
# the event loop in alien_invasion.py

def chek_events():
    """Respond to keypresses and mouse events."""

    # Watch for keyboard and mouse events.
    # The for loop at is an event loop

# The new update_screen() function takes three parameters: ai_settings, screen and ship.
def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""

    # Redraw the screen during each pass through the loop

    # Fill the screen with the background color using the screen.fill() method,
    # which takes only one argument: a color.
    # access the background color when filling the screen at as well.

    screen.fill(ai_settings.bg_color)

    # We draw the ship onscreen by calling ship.blitme() after filling the
    # background, so the ship appears on top of the background.

    ship.blitme()

    # Make the most recently drawn screen visible.

    # The call to pygame.display.flip() at tells Pygame to make the most recently drawn
    # screen visible. In this case it draws an empty screen each time through the while loop
    # to erase the old screen so that only the new screen is visible. When we move the game
    # elements around, pygame.display.flip() will continually update the display to show the
    # new positions of elements and hide the old ones, creating the illusion of smooth movement.

    pygame.display.flip()

    for event in pygame.event.get():
        # To access the event detected by Pygame, we'll use the pygame.event.get() method.
        # Any keyboard or mouse event will cause the for loop to run.
        # Inside the loop, we'll write a series of if statements to detect and respond to specific events.
        # For example, when the player clicks the game window's close button, a pygame.QUIT event is
        # detected and we call sys.exit() to exit the game.
        if event.type == pygame.QUIT:
            sys.exit()
