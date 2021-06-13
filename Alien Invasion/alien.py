import pygame
from pygame.sprite import Sprite

# Most of this class is like the Ship class except for the placment of the alien.
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Inttialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('/home/akmen/PycharmProjects/Alien Invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        # We initially place each alien near the top-left corner if the screen,
        self.rect.x = self.rect.width # adding a space to the left of it that's equal to the alien's width
        self.rect.y = self.rect.height # space above it equal to its height.
        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
