# Each time we introduce new functionality into our game,we'll typically introduce
# some new setting as well. Instead of adding settings throughout the code, let's
# write a module called settings that contains a class called Settings to stores all
# one settings in one place. This approach allows us to pass around one settings
# object instead of many individual settings.
# In addition, it makes our function calls simpler and makes it easier to modify the
# game's appearance as our project grows. To modify the game, we'll simple change some
# values in setting.py instead of searching for different settings throughout our files.

class Settings():
    """ A class to store all settings for Alien Invasion. """

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
