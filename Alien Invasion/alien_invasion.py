import pygame
# We import Group from pygame.sprite.
from  pygame.sprite import Group

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

    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    # We make an instance of Group and call it bullets. This group is created outside of the
    # while loop so we don't create a new group of bullets each time the loop cycles.
    bullets = Group()

    # Start the main loop for the game.

    # The game is controlled by a while loop
    # that contains an event loop and code that manages screen updates
    while True:
        # These two functions make the while loop simpler and will make further
        # development easier. Instead of working inside run_game(), we can do most
        # of our work in the module game_functions.
        gf.chek_events(ai_settings, screen, ship, bullets) # the main loop check for player input
        ship.update() # then it updates the position of the ship

        # We pass bullets to chek_events() snd update_screen(). We'll need to work with bullets
        # in check_events() when the spacbar is pressed, and we'll need to update the bullets that
        # are being drawn to the sdreen in update_screen().
        # When you call update() on a group(), the group automatically calls upsate() for each sprite
        # in the group. The line bullets.update() calls bullet.update() for each bullet
        # we place in the group bullets.
        gf.update_bullets(bullets) # any bullets that have been fired
        gf.update_screen(ai_settings, screen, ship, bullets) # we than use the updated positions to draw a new screen



# which initializes the game and starts the main loop.
run_game()
