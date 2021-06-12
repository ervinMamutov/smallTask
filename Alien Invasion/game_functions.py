import sys

import pygame

from bullet import Bullet


# The group bullets is passed to check_keydown_events(). When the player presses the spacebar,
# we create a new bullet ( a Bullet instance thar we name_bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right

        # modify how the game responds when the player presses the right arrow key:
        # instead of changing the ship's position directly, merely set moving_right to True

        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    # add it to the group bullets using the add() method: the code bulets.add(new_bullet) stores
    # the new bullets in the group bullets.
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullet group.
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to key releases."""

    # We check if the key pressed is the right arrow key (pygame.K_RIGHT)
    # by reading the event.key attribute.

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


# This module imports sys and pygame, which are used in the event cheking loop.
# The function needs no parameters at this point, and the body is copied from
# the event loop in alien_invasion.py

# We give the check_events() funktion a ship parameter, because  the ship needs
# to move to the rihgt when the right arrow key is pressed.

# We need to add bullets as a parametr in the definition of check_events() and we need to pass bullets
# as an argument in th call to check_keydown_events() as well.

def chek_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():
        # To access the event detected by Pygame, we'll use the pygame.event.get() method.
        # Any keyboard or mouse event will cause the for loop to run.
        # Inside the loop, we'll write a series of if statements to detect and respond to specific events.
        # For example, when the player clicks the game window's close button, a pygame.QUIT event is
        # detected and we call sys.exit() to exit the game.
        if event.type == pygame.QUIT:
            sys.exit()
        # Watch for keyboard and mouse events.
        # The for loop at is an event loop

        # Inside check_events() we add an elif block to the event loop to respond when
        # Pygame detects a KEYDOWN event

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        # Add a new elif block, which responds to KEYUP events. When the player releases the
        # right arrow key (K_RIGHT), we set moving_right to False.
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

            # If the right arrow key was pressed, we move the ship to the right
            # by increasing the value of ship.rect.centerx by event.type == pygame.KEYDOWN

            ship.rect.centerx += 1


# The new update_screen() function takes three parameters: ai_settings, screen and ship.
# We give the bullets parameter to update_screen() at def ehich draws the bullets to the screen.

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""

    # Redraw the screen during each pass through the loop

    # Fill the screen with the background color using the screen.fill() method,
    # which takes only one argument: a color.
    # access the background color when filling the screen at as well.

    screen.fill(ai_settings.bg_color)

    # The bullets.spritees() method returns a list of all sprites in the group bullets.
    # To draw all fired bullets to the screen, we loop through the sprites in bullets
    # and call draw_billet()  on rach one.
    # Redraw all bullets behind ship and aliens.
    for bullets in bullets.sprites():
        bullets.draw_bullet()
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
