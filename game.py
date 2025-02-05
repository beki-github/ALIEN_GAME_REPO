import pygame
from settings import Settings
from ship import Ship
import game_function
from gamestate import state

def run_game():
    """Initialize and run the game."""
    pygame.init()
    av_setting = Settings()
    screen = pygame.display.set_mode((av_setting.screen_width, av_setting.screen_height))
    pygame.display.set_caption("Alien Invasion New")
    # Create a ship instance
    ship = Ship(av_setting, screen)
    game_state=state(av_setting)
    
    # Create groups for aliens and bullets
    aliens = pygame.sprite.Group()  # Ensure this is a Group instance
    bullets = pygame.sprite.Group()

    
    # Create a fleet of aliens
    game_function.create_fleet(av_setting,screen,aliens,ship)
    
    while True:
        game_function.check_events(av_setting, screen, ship, bullets) 
        ship.update_postion()  # Ensure this method is defined in your Ship class
        bullets.update()
        game_function.collision_check(aliens,bullets,av_setting,screen,ship,game_state)
        game_function.update_alien(av_setting,aliens)
        game_function.update_screen(av_setting, screen, ship, aliens, bullets)

run_game()
