import pygame as pg
from settings import *

class Map:
    def __init__(self, sc):
        self.sc = sc
        self.world_map = set()
        self.not_free_tiles = set()
        self.text_map = [
                '..WWWWWWWWWWWW......',
                '....WWWWW.....FFF...',
                '.............FFFFF..',
                '...........FFFFFFFF.',
                '............FFFFFF..',
                '...WWW........FFF...',
                '....................',
                '...s......W.....SSS.',
                '..ssss....WW....SS..',
                '..sss.....WWW.......',
                '..sss.....WWWW......',
                '..........WWWW......',
                '..........WW.W......',
                '..........W......s..',
                '.....W...........ss.',
                '....WWW.........sss.',
                '...SSSSSS........ss.',
                '......SSSSs.......s.',
                '....SSSSS.s.........',
                '...SSSS...s.........'
        ]

        

    def update_map(self):
        for j, row in enumerate(self.text_map):
            for i, char in enumerate(row):
                self.world_map.add((i * TILE_SIZE, j * TILE_SIZE, char))


    def draw_map(self):
        for x, y, c in self.world_map:
            if c == '#':
                pg.draw.rect(self.sc, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 5)
            elif c == "W":
                pg.draw.rect(self.sc, WATER, (x, y, TILE_SIZE, TILE_SIZE))
                self.not_free_tiles.add((x // TILE_SIZE, y // TILE_SIZE))
            elif c == "S":
                pg.draw.rect(self.sc, SAND, (x, y, TILE_SIZE, TILE_SIZE))
                self.not_free_tiles.add((x // TILE_SIZE, y // TILE_SIZE))
            elif c == "s":
                pg.draw.rect(self.sc, STONE, (x, y, TILE_SIZE, TILE_SIZE))
                self.not_free_tiles.add((x // TILE_SIZE, y // TILE_SIZE))
            elif c == "F":
                pg.draw.rect(self.sc, FOREST, (x, y, TILE_SIZE, TILE_SIZE))
                self.not_free_tiles.add((x // TILE_SIZE, y // TILE_SIZE))

        for i in range(20):
            pg.draw.line(self.sc, BLACK, ((i+1)*TILE_SIZE, 0), ((i+1)*TILE_SIZE, WIDTH))
        for i in range(20):
            pg.draw.line(self.sc, BLACK, (0, (i+1)*TILE_SIZE), (WIDTH, (i+1)*TILE_SIZE))
                                        
                            