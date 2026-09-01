import pygame as pg
from main_scripts.settings import *

class Action_menu_HUD:
    def __init__(self, sc):
        self.sc = sc
        self.font = pg.font.Font(None, 25)
        self.is_open = False
        self.actions_list = ['1. Построить', '2. Инфо', '3. Разобрать']

    def check_open(self, events, mouse_pos):
        for event in events:
            if event.type == pg.MOUSEBUTTONUP and event.button == 3:
                if self.is_open:
                    self.is_open = False
                else:
                    self.is_open = True
                    self.open_x, self.open_y = mouse_pos
                    self.rect = pg.rect.Rect(self.open_x, self.open_y, 125, 100)

            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                if self.is_open:
                    self.rect = pg.rect.Rect(self.open_x, self.open_y, 125, 100)
                    if self.rect.collidepoint(pg.mouse.get_pos()) == False:
                        self.is_open = False

    def check_pressed(self, events):
        for event in events:        
            if event.type == pg.KEYUP:
                if self.is_open:
                    tile = self.open_x // TILE_SIZE, self.open_y // TILE_SIZE
                    if event.key == pg.K_1:
                        return 1, tile
                    if event.key == pg.K_2:
                        return 2, tile
                    if event.key == pg.K_3:
                        return 3, tile

    def draw_hud(self):
        if self.is_open:
            pg.draw.rect(self.sc, WHITE, self.rect)
            pg.draw.rect(self.sc, BLACK, self.rect, 4)

            y_diff = 1
            for line in self.actions_list:
                rendered_line = self.font.render(line, True, BLACK)
                self.sc.blit(rendered_line, (self.open_x + 7, self.open_y - 10 + y_diff * 20))
                y_diff = y_diff + 1
