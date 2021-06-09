# This class Ship will manage most of behavior of the player's ship
# First, we import the pygame module
import pygame

class Ship():
    # The __init__() method of Ship takes two parameters: the  self reference and
    # the screen where we'll draw the ship.
    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        # This finction returns a surface representing the ship, which we store in:
        self.image = pygame.image.load('/home/akmen/PycharmProjects/Alien Invasion/images/ship.bmp')
        # Once the image is loaded, we use get_rect() to access the surface's rect attribute:
        self.rect = self.image.get_rect()
        # We'll position the ship at the bottom center of the screen. To do so,
        # first store the screen's rect in self.screen_rect
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of screen.
        # Make the value of self.rect.centrex (the x-coordinate of the ship's center)
        # match the centerx attribute of the screen's rect:
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        # Add a self.moving_right attribute in this metod and set it to False initially
        self.moving_right = False
        self.moving_left = False

    # Add update(), which moves the ship right if the flag is True
    def update(self):
        """Update the ship's position based on the movement flags."""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
    # we define the blitme() method, which will draw the im
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

