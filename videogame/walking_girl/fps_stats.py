from shmup.config import cfg_item

class FPSStats:

    def __init__(self, font):
        self.__frames = 0
        self.__update_time = 0
        self.__font = font
        self.__set_fps_surface()

    def update(self, delta_time):
        self.__frames += 1
        self.__update_time += delta_time

        if self.__update_time >= cfg_item("game", "sync", "update_time"):
            self.__set_fps_surface()
            self.__frames = 0
            self.__update_time -= cfg_item("game", "sync", "update_time")

    def render(self, surface):
        surface.blit(self.__text_image, cfg_item("game", "sync", "fps_pos"))

    def release(self):
        pass

    def __set_fps_surface(self):
        self.__text_image = self.__font.render(f"{self.__frames}", True, cfg_item("game", "sync", "fps_color"))