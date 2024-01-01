import pygame

from shmup.entities.projectiles.projectile import Projectile
from shmup.config import cfg_item

class Projectile_Enemy(Projectile):

    def __init__(self, spritesheet, position):
        velocity = pygame.math.Vector2(cfg_item("entities", "projectiles", "enemy", "velocity"))
        name = cfg_item("entities", "projectiles", "enemy", "name")

        super().__init__(spritesheet, name, position, velocity)