#settings class
class Settings():
    def __init__(self):
        self.screen_width=1000
        self.screen_height=600
        self.bg_colour=(255,255,255)
        self.ship_speed_factor=1
    #BULLET attribute
        self.bullet_widith=200
        self.bullet_height=15
        self.bullet_colour=60,60,60
        self.bullet_speed_factor=1
        self.bullet_allowed=200
    #ALIEN attribute :
        self.alien_speed_factor=0.05
    # MOVING DIRECTION// 1 for moving right // -1 for moving left //drop speed of alien=10
        self.ship_allowed=3
        self.moving_direction=1
        self.drop_speed=5
