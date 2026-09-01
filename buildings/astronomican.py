import pygame as pg
from main_scripts.settings import *

class Astronomican:
    def __init__(self, sc, img_path):
        self.building_name = 'Астрономикон'
        self.description = 'Сердце и оплот города.'
        self.sc = sc

        self.health_point = 1000

        self.position = None
        self.wait_timer = FPS/10
        if img_path:
            self.image = pg.image.load(f'{img_path}').convert_alpha()
            self.image = pg.transform.scale(self.image, (TILE_SIZE-1, TILE_SIZE-1))

    def build(self, tiles, events, mouse_pos):
        if not self.position:
            if self.wait_timer <= 0:
                mouse_x_tile = (mouse_pos[0] // TILE_SIZE)
                mouse_y_tile = (mouse_pos[1] // TILE_SIZE)

                pg.draw.rect(self.sc, GREEN, (mouse_x_tile * TILE_SIZE, mouse_y_tile * TILE_SIZE, TILE_SIZE, TILE_SIZE), 4)
                is_occupied = (mouse_x_tile, mouse_y_tile) in tiles

                if is_occupied:
                    pg.draw.rect(self.sc, RED, (mouse_x_tile * TILE_SIZE, mouse_y_tile * TILE_SIZE, TILE_SIZE, TILE_SIZE), 4)
                else:
                    pg.draw.rect(self.sc, GREEN, (mouse_x_tile * TILE_SIZE, mouse_y_tile * TILE_SIZE, TILE_SIZE, TILE_SIZE), 4)

                for event in events:
                    if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                        if not is_occupied:
                            self.position = (mouse_x_tile, mouse_y_tile)
            self.wait_timer = self.wait_timer - 1

    def draw_build(self):
        if self.position:
            if self.image:
                self.sc.blit(self.image, (self.position[0] * TILE_SIZE + 1, self.position[1] * TILE_SIZE + 1))
            else:
                pg.draw.circle(self.sc, BROWN, (self.position[0] * TILE_SIZE + TILE_SIZE//2, self.position[1] * TILE_SIZE + TILE_SIZE//2), TILE_SIZE//2-2)
                self.sc.blit(pg.font.Font(None, 45).render('А', True, WHITE), (self.position[0] * TILE_SIZE + 9, self.position[1] * TILE_SIZE + 7))    