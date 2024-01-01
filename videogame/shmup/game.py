from importlib import resources

import pygame

from shmup.config import cfg_item, Config
from shmup.fps_stats import FPSStats
from shmup.entities.hero import Hero
from shmup.assets.spritesheet import SpriteSheet
from shmup.entities.projectiles.projectile_factory import ProjectileType, ProjectileFactory
from shmup.entities.rendergroup import RenderGroup

class Game:

    def __init__(self):
        pygame.init()

        self.__screen = pygame.display.set_mode(cfg_item("game", "screen_size"), 0, 32)
        pygame.display.set_caption(cfg_item("game","caption"))
        pygame.mouse.set_visible(False)

        self.__is_running = False

        with resources.path(cfg_item("game","font_path"), cfg_item("game", "font_name")) as font_path:
            font = pygame.font.Font(font_path, 40)

        self.__clock = pygame.time.Clock()
        self.__fps_stats = FPSStats(font)

        self.__spritesheet = SpriteSheet(cfg_item("entities","image_path"), cfg_item("entities", "data_path"))

        self.__projectiles_allied = RenderGroup()
        self.__players = RenderGroup()
        self.__players.add(Hero(self.__spritesheet, self.spawn_projectile))

    def run(self):
        self.__is_running = True

        while self.__is_running:
            delta_time = self.__clock.tick(cfg_item("game", "sync", "fps"))
            self.__handle_input()
            self.__update(delta_time)
            self.__render()

        self.__release()

    def __handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__is_running = False
                if event.key == pygame.K_F5:
                    Config.get_instance().debug = not Config.get_instance().debug
                self.__players.handle_input(event.key, True)
                pass
            if event.type == pygame.KEYUP:
                self.__players.handle_input(event.key, False)
                pass

    def __update(self, delta_time):
        self.__players.update(delta_time)
        self.__projectiles_allied.update(delta_time)
        self.__fps_stats.update(delta_time)

    def __render(self):
        self.__screen.fill(cfg_item("game", "bg_color"))

        self.__players.draw(self.__screen)
        self.__projectiles_allied.draw(self.__screen)

        if Config.get_instance().debug:
            self.__fps_stats.render(self.__screen)

        pygame.display.update()

    def __release(self):
        self.__players.release()
        self.__projectiles_allied.release()
        self.__fps_stats.release()
        pygame.quit()

    def spawn_projectile(self, proj_type, position):
        if proj_type == ProjectileType.Allied:
            self.__projectiles_allied.add(ProjectileFactory.create_projectile(proj_type, self.__spritesheet, position))