from importlib import resources
import json
from os import path

from importlib import resources
import json

import pygame

class SpriteSheet:

    def __init__(self, image_path, data_path):
        with resources.path(data_path[0], data_path[1]) as data_filename:
            with open(data_filename) as f:
                self.__data = json.load(f)

        with resources.path(image_path[0], image_path[1]) as image_filename:
            self.__image = pygame.image.load(image_filename).convert_alpha()

    def get_image(self, name):
        if name in self.__data:
            return self.__image, pygame.Rect(self.__data[name])
        else:
            pygame.Surface((0,0)), pygame.Rect(0,0,0,0)