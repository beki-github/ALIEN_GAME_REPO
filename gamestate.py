import ship
import time
import pygame
import settings
import game_function
class state():
    def __init__(self,av_setting):
        self.av_setting=av_setting
        self.reset()
    def reset(self,ship,screen,aliens):
        self.av_setting.ship_allowed-=1
        screen_rect=screen.rect()
        ship.rect.centerx=screen_rect.centerx
        game_function.create_fleet(self.av_setting,screen,aliens,ship)
        
        


    


        