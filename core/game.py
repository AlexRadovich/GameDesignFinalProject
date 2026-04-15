from pyray import *
from core.scene_manager import SceneManager
from enums import *
from ui.title_screen import TitleScreen
from ui.character_select_screen import CharacterSelectScreen
from levels.level_one import LevelOne


class Game():

    def __init__(self):

        self.scene_manager = SceneManager(self)

    def update(self):
        self.scene_manager.update()

    def draw(self):
        self.scene_manager.draw()

    def startup(self):
        self.scene_manager.add_scene(Scenes.TITLE, TitleScreen(self))
        self.scene_manager.add_scene(Scenes.CHARACTER_SELECT, CharacterSelectScreen(self))
        self.scene_manager.add_scene(Scenes.LEVEL_ONE, LevelOne(self))

    def shutdown(self):
        pass