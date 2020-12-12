import sys
import pygame

class MadLibs:
    """Overall class to manage the assets of the game and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("MadLibs!")

        # Set the background color.
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.Quit:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
    
    if __name__ == '__main__':
        # Make a game instance and run the game.
        ai = MadLibs()
        ai.run_game()