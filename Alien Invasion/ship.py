# This class Ship will manage most of behavior of the player's ship
# First, we import the pygame module
import pygame

class Ship():
    # The __init__() method of Ship takes two parameters: the  self reference and
    # the screen where we'll draw the ship.
    # We add ai_settings to the list of parameters.
    # So the ship will have access to its speed seting.
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Now that we're adjusting the position of the ship by fractions of a pixel,
        # we need to store the position in a variable thet can store a decimal value.
        # You can use a decimal value to set a rect's attribute, but the rect will store
        # only the integer portion of that value. To store the ship's position accurately,
        # we define a new attribute self.center, which can hols decimal values.

        self.ai_settings = ai_settings

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

        # Store a decimal value for the ship's center.

        # We used the float() function to convert the value of self.rect.centerx to a decimal
        # and store this value in self.center.

        self.center = float(self.rect.centerx)

        # Movement flag
        # Add a self.moving_right attribute in this metod and set it to False initially
        self.moving_right = False
        self.moving_left = False

    # Add update(), which moves the ship right if the flag is True
    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's center value, not the rect.

        # This code checks the position of the ship befor changing the value of self.center.
        # The code self.rect.right returns the x-coordinate value of the right
        # edge of the ship's rect. If this value is less than the value returned
        # by self.screen_rect.right, the ship hasn't reached the right edge of the screen.

        if self.moving_right and self.rect.right < self.screen_rect.right:

            # When we change the ship's position in update(), the value of self.center is
            # adjusted by the amount stored in ai_settings.ship_speed_factor.

            self.center += self.ai_settings.ship_speed_factor

        # The same goes for the left edge: if the value of the left side of the rect is
        # greayer than zero, the ship hasn't reached the left edge of the screen.

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.

        # We use the new value to update portion of self.rect.centerx, which controls
        # the position of the ship.

        self.rect.centerx = self.center
    # we define the blitme() method, which will draw the im
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

