import sys
import pygame


# Alien Invasion starts as the this function
def run_game():
    """
    Initialize game and create a screen object.

    """
    # initializes background setting that Pygame needs to work properly
    pygame.init()
    # create a display windows called screen on which we'll draw all of
    # the game elements.
    # The arguments (1200, 800) is a tuple defines the dimensions of the game windows
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_capion('Alien Inavasion')

    # Set the background color.
    # Colors in Pygame are specified as RGB colors: red(0, 255, 0), green(0, 255, 0),
    # blue(0, 0, 255)

    bg_color = (230, 230, 230)

    # Start the main loop for the game.

    # The game is controlled by a while loop
    # that contains an event loop and code that manages screen updates
    while True:

        # Watch for keyboard and mouse events.

        # Redraw the screen during each pass through the loop
        # Fill the screen with the background color using the screen.fill() method, which takes
        # only one argument: a color.
        screen.fill(bg_color)

        # The for loop at is an event loop
        for event in pygame.event.get():
            # To access the event detected by Pygame, we'll use the pygame.event.get() method.
            # Any keyboard or mouse event will cause the for loop to run.
            # Inside the loop, we'll write a series of if statements to detect and respond to specific events.
            # For example, when the player clicks the game window's close button, a pygame.QUIT event is
            # detected and we call sys.exit() to exit the game.
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible.

        # The call to pygame.display.flip() at tells Pygame to make the most recently drawn
        # screen visible. In this case it draws an empty screen each time through the while loop
        # to erase the old screen so that only the new screen is visible. When we move the game
        # elements around, pygame.display.flip() will continually update the display to show the
        # new positions of elements and hide the old ones, creating the illusion of smooth movement.
        pygame.display.flip()


# which initializes the game and starts the main loop.
run_game()
