import pygame as pg
from main_scripts.settings import *

class Buttons:
    def __init__(self, sc):
        self.sc = sc

    def create_btn(self, center, width, height, text, font_size, events):
        font = pg.font.Font(None, font_size)
        x = center[0]-width//2
        y = center[1]-height//2

        text_w, text_h = font.size(text)
        text_x = center[0]-text_w//2
        text_y = center[1]-text_h//2

        mouse_pos = pg.mouse.get_pos()

        pg.draw.rect(self.sc, WHITE, (x, y, width, height))

        if pg.rect.Rect(x, y, width, height).collidepoint(mouse_pos):
            pg.draw.rect(self.sc, GRAY, (x, y, width, height))
            for event in events:
                if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    return True
        
        pg.draw.rect(self.sc, BLACK, (x, y, width, height), 4)
        
        self.sc.blit(font.render(text, True, BLACK), (text_x, text_y))