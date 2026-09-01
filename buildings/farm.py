import pygame as pg
from settings import *

class Farm:
    def __init__(self, sc):
        self.building_name = 'Ферма'
        self.description = 'Главное производственное здание.'
        self.sc = sc

        self.health_point = 500

        self.position = None

    def build(self):
        if not self.position:
            pass