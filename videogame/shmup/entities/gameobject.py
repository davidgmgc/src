from abc import ABC, abstractmethod

import pygame

from shmup.config import cfg_item

class GameObject(pygame.sprite.Sprite, ABC):

    def __init__(self):
        super().__init__()
        self._name = ""
        self._position = pygame.math.Vector2(0.0, 0.0)
        self._render_rect = pygame.Rect(0,0,0,0)
        self._rect = pygame.Rect(0,0,0,0)

    @abstractmethod
    def handle_input(self, key, is_pressed):
        pass

    @abstractmethod
    def update(self, delta_time):
        pass

    @abstractmethod
    def render(self, surface):
        pass

    @abstractmethod
    def release(self):
        pass

    def _in_bounds(self, distance):
        _, rect = self._spritesheet.get_image(self._name)

        new_position = pygame.math.Vector2(self._position.x + distance.x + rect.width/2, self._position.y + distance.y + rect.height/2)

        return new_position.x >= 0 and new_position.x <= cfg_item("game", "screen_size")[0] and new_position.y >= 0 and new_position.y <= cfg_item("game", "screen_size")[1]

    def _center(self):
        self._rect.center = self._position.xy
        self._render_rect.center = self._position.xy

    def _render_debug(self, surface):
        pygame.draw.rect(surface, (255,0,0), self._rect, 1)
        pygame.draw.rect(surface, (0,0,255), self._render_rect, 1)