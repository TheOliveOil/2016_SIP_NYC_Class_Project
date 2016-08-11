import os,sys
import pygame as pg

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (152, 251, 152)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
PURPLE =  (160, 32, 240)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Character:
    def __init__(self,rect):
        self.rect = pg.Rect(rect)
        self.click = False
        self.image = pg.Surface(self.rect.size).convert()
        self.image.fill((GREEN))
    def update(self,surface):
        if self.click:
            self.rect.center = pg.mouse.get_pos()
        surface.blit(self.image,self.rect)

def main(Surface,Player):
    game_event_loop(Player)
    Surface.fill(PURPLE)
    Player.update(Surface)


def game_event_loop(Player):
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if Player.rect.collidepoint(event.pos):
                Player.click = True
        elif event.type == pg.MOUSEBUTTONUP:
            Player.click = False
        elif event.type == pg.QUIT:
            pg.quit(); sys.exit()

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((1000,600))
    MyClock = pg.time.Clock()
    MyPlayer = Character((0,0,150,150))
    MyPlayer.rect.center = Screen.get_rect().center
    while 1:
        main(Screen,MyPlayer)
        pg.display.update()
        MyClock.tick(60)