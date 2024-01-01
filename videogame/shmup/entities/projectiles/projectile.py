import pygame

from shmup.config import cfg_item, Config
from shmup.entities.gameobject import GameObject

class Projectile(GameObject):

    def __init__(self, spritesheet, name, position, velocity):
        super().__init__()
        self._position = position
        self.__velocity = velocity

        self._name = name

        self._spritesheet = spritesheet
        _, rect = spritesheet.get_image(self._name)

        self._render_rect = rect.copy()
        self._rect = rect.copy()

        self._center()

    def handle_input(self, key, is_pressed):
        pass

    def update(self, delta_time):
        distance = self.__velocity * delta_time

        if self._in_bounds(distance):
            self._position += distance
            self._center()
        else:
            self.kill()

    def render(self, surface):
        image, rect = self._spritesheet.get_image(self._name)

        surface.blit(image, self._render_rect, rect)

        if Config.get_instance().debug:
            self._render_debug(surface)

    def release(self):
        pass