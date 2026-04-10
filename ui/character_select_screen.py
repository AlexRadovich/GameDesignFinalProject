from settings import *
from enums import *

class CharacterSelectScreen():

    def __init__(self, game):
        
        self.game = game

    def update(self):
        if is_key_pressed(KeyboardKey.KEY_ENTER):
            self.game.scene_manager.change_scenes(Scenes.TITLE)

    def draw(self):
        draw_text("CHARSELECT DRAW", 100, 100, 30, RED)