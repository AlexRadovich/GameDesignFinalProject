from settings import *
from enums import *

class TitleScreen():

    def __init__(self, game):

        self.game = game


    def startup(self):
        pass


    def update(self):

        if is_key_pressed(KeyboardKey.KEY_ENTER):
            self.game.scene_manager.change_scenes(Scenes.CHARACTER_SELECT)


    def draw(self):
        draw_text("TITLESCRN DRAW", 100, 100, 30, RED)


    def shutdown(self):
        pass
        