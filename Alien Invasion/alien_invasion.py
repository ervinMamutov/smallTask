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
        # These two functions make the while loop simpler and will make further
        # development easier. Instead of working inside run_game(), we can do most
        # of our work in the module game_functions.
        gf.chek_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)



# which initializes the game and starts the main loop.
run_game()
