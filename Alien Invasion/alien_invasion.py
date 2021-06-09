import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


# Alien Invasion starts as the this function
def run_game():
    """
    Initialize pygame, settings, and screen object.

    """
    # We import Settings into the main program file, and then create an instance
    # of Settings and store it in ai_settings after making the call to:
    pygame.init()

    ai_settings = Settings()
    # When create a screen
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Inavasion')

    # Make a ship

    # We import Ship ans then make an instance of Ship (named ship) after the screen
    # has been created. It must come before the main while loop so we don't make a new
    # instance of the ship on each pass through the loop.

    ship = Ship(screen)

    # Start the main loop for the game.

    # The game is controlled by a while loop
    # that contains an event loop and code that manages screen updates
    while True:
        gf.chek_events()

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


# which initializes the game and starts the main loop.
run_game()
