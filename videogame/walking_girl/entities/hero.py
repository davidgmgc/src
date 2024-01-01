from importlib import resources

import pygame

from shmup.config import cfg_item, Config
from shmup.entities.projectiles.projectile_factory import ProjectileType
from shmup.entities.gameobject import GameObject

class Hero(GameObject):

    def __init__(self, spritesheet, spawn_projectile_callback):
        super().__init__()
        self._spritesheet = spritesheet
        self.__spawn_projectile_callback = spawn_projectile_callback

        self._name = cfg_item("entities", "hero", "name")

        self._position = pygame.math.Vector2(0.0, 0.0)

        _, rect = self._spritesheet.get_image(self._name)

        self._render_rect = rect.copy()
        self._rect = rect.copy()
        self._rect.inflate_ip(self._rect.width * -0.60, self._rect.height * -0.20)

        self._center()

        self.__is_moving_right = False
        self.__is_moving_left = False


    def handle_input(self, key, is_pressed):

        if key == pygame.K_LEFT:
            self.__is_moving_left = is_pressed
        if key == pygame.K_RIGHT:
            self.__is_moving_right = is_pressed

    def update(self, delta_time):
        velocity = pygame.math.Vector2(0.0, 0.0)
        speed = cfg_item("entities", "hero", "speed")

        if self.__is_moving_left:
            velocity.x -= speed
        if self.__is_moving_right:
            velocity.x += speed

        distance = velocity * delta_time

        if self._in_bounds(distance):
            self._position += distance

        self._center()

    def render(self, surface):
        hero_name = self._name
        if self.__is_moving_left:
            hero_name = cfg_item("entities", "hero", "name_left")
        if self.__is_moving_right:
            hero_name = cfg_item("entities", "hero", "name_right")

        image, rect = self._spritesheet.get_image(hero_name)
        surface.blit(image, self._render_rect, rect)

        if Config.get_instance().debug:
            self._render_debug(surface)

    def release(self):
        pass

    def __fire(self):
        self.__spawn_projectile_callback(ProjectileType.Allied, pygame.math.Vector2(self._render_rect.midtop))