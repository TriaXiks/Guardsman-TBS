import pygame as pg
from settings import *

class Astronomican:
    def __init__(self, sc):
        self.building_name = 'Астрономикон'
        self.description = 'Сердце и оплот города.'
        self.sc = sc

        self.health_point = 1000

        self.position = None

    def build(self, tiles, events):
        if not self.position:
            mouse_pos = pg.mouse.get_pos()
            mouse_x_tile = (mouse_pos[0] // TILE_SIZE)
            mouse_y_tile = (mouse_pos[1] // TILE_SIZE)

            pg.draw.rect(self.sc, GREEN, (mouse_x_tile * TILE_SIZE, mouse_y_tile * TILE_SIZE, TILE_SIZE, TILE_SIZE), 4)
            is_occupied = (mouse_x_tile, mouse_y_tile) in tiles

            if is_occupied:
                pg.draw.rect(self.sc, RED, (mouse_x_tile * TILE_SIZE, mouse_y_tile * TILE_SIZE, TILE_SIZE, TILE_SIZE), 4)
            else:
                pg.draw.rect(self.sc, GREEN, (mouse_x_tile * TILE_SIZE, mouse_y_tile * TILE_SIZE, TILE_SIZE, TILE_SIZE), 4)
                
            for event in events:
                if event.type == pg.MOUSEBUTTONUP and event.button == 3:
                    if not is_occupied:
                        self.position = (mouse_x_tile, mouse_y_tile)
                        tiles.add((mouse_x_tile, mouse_y_tile)) 

    def draw_build(self):
        if self.position:
            pg.draw.circle(self.sc, BROWN, (self.position[0] * TILE_SIZE + TILE_SIZE//2, self.position[1] * TILE_SIZE + TILE_SIZE//2), TILE_SIZE//2-2)
            self.sc.blit(pg.font.Font(None, 45).render('А', True, WHITE), (self.position[0] * TILE_SIZE + 9, self.position[1] * TILE_SIZE + 7))    
                    