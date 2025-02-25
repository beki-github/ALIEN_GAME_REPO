import sys
import pygame
from bullets import Bullet
from aliens import Aliens
import time
import gamestate
def check_keydown_event(event,av_settings,screen,ship,bullets):
     """check for for key up events"""
     if event.key==pygame.K_RIGHT:
          ship.moving_right=True
     elif event.key==pygame.K_LEFT:
          ship.moving_left=True
     elif event.key==pygame.K_SPACE:
          # creating than adding new bullets
          # i forgot where the bullets are deleted :(
          if len(bullets)<av_settings.bullet_allowed:
            new_bullet=Bullet(av_settings,screen,ship)
            bullets.add(new_bullet)
     elif event.key==pygame.K_q:
          sys.exit()
def check_keyup_event(event,ship):
     """check for keydown event"""
     if event.key==pygame.K_RIGHT:
          ship.moving_right=False
     elif event.key==pygame.K_LEFT:
          ship.moving_left=False
def check_events(av_settings,screen,ship,bullets):
      for event in pygame.event.get(): #tpye:ignore 
            if event.type==pygame.QUIT:
                sys.exit()
            # check for key event
            elif event.type==pygame.KEYDOWN: 
                 # this checks if there is a key pressed
                check_keydown_event(event,av_settings,screen,ship,bullets)
            elif event.type==pygame.KEYUP:
                 # this checks if it's not pressed
                 check_keyup_event(event,ship)
def get_number_row(av_setting,alien_height,ship_height):
     """calculate the number of rows that fit in the screen"""
     avalable_space_y=av_setting.screen_height-(4*alien_height+ship_height)
     row_number=int(avalable_space_y/(3*alien_height))
     return row_number
     
def get_alien_number(av_settings,alien_width):
     """calcuate the number of aliens that fit in the screem"""
     avalable_space_x=av_settings.screen_width-(2*alien_width)
     alien_number_x=int(avalable_space_x/(2*alien_width))
     return alien_number_x

def create_alien(av_settings,screen,alien_number,aliens,row_number):
     alien=Aliens(av_settings,screen)
     alien_width=alien.rect.width
     alien.x=alien_width+(2*alien_width*alien_number)
     alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
     alien.rect.x=alien.x
     aliens.add(alien)

def create_fleet(av_setting,screen,aliens,ship):
     alien=Aliens(av_setting,screen)
     alien_number_x=get_alien_number(av_setting,alien.rect.width)
     row_numbers=get_number_row(av_setting,alien.rect.height,ship.rect.height)
     for row_number in range(row_numbers):
          for alien_number in range(alien_number_x):
               create_alien(av_setting,screen,alien_number,aliens,row_number)

# this where copy of bullets that're outside the screen are deleted
# why didn't  call it update bullets instead of update screen: cause it updates the whole screen after each iteration
def update_screen(av_setting,screen,ship,aliens,bullets):
    screen.fill(av_setting.bg_colour) #fill the screen after each iteration 
    #draw the bullets
    for bullet in bullets.sprites():
         bullet.draw_bullet()
    for bullet in bullets.copy():
            if bullet.rect.bottom <=0:
                bullets.remove(bullet)
    ship.blitme() 
    aliens.draw(screen)
    pygame.display.flip() #this change the screen after 
def check_fleet_postion(aliens,av_settings):
    for alien in aliens:
        if alien.check_edge():
             alien.change_direction(aliens)
 
             break
def ship_hit(aliens,screen, game_state,ship,bullets,av_setting):
     time.sleep(0.5)
     aliens.empty()
     bullets.empty()
     game_state.ship_left-=1
     create_fleet(av_setting,screen,aliens,ship)
     av_setting.alien_speed_factor=0.05
     ship.center_ship()

#i wrote this comment to cope with the guilt of wasting my time
# LGTM!#

def update_alien(av_setting,aliens):
     check_fleet_postion(aliens,av_setting)
     aliens.update()
def collision_check(aliens,bullets,av_setting,screen,ship,game_state):
     collisons=pygame.sprite.groupcollide(bullets,aliens,False,True)#if there is collision it deletes both objects from the screen.
     if len(aliens)==0:
          bullets.empty()
          create_fleet(av_setting,screen,aliens,ship,)
          av_setting.alien_speed_factor+=1
     if pygame.sprite.spritecollideany(ship,aliens):
          print(" you lost the game ")
          ship_hit(aliens,screen,game_state,ship,bullets,av_setting)
     for alien in aliens:
          screen_rect=screen.get_rect()
          if alien.rect.bottom>=screen_rect.bottom:
               ship_hit(aliens,screen,game_state,ship,bullets,av_setting)
     

     