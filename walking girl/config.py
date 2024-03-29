from importlib import resources
import json

def cfg_item(*items):
  d = Config.get_instance().data
  for k in items:
    d = d[k]
  return d

class Config:

    __config_path, __config_filename = "shmup.assets.config", "config.json"
    __instance = None

    @staticmethod
    def get_instance():
        if Config.__instance is None:
            Config()
        return Config.__instance

    def __init__(self):
        if Config.__instance is None:
            Config.__instance = self
            with resources.path(Config.__config_path, Config.__config_filename) as json_path:
                with open(json_path) as f:
                    self.data = json.load(f)
            self.__debug = False
        else:
            raise Exception("Config Doesn't Allow Multiple Instances")

    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, value):
        self.__debug = value