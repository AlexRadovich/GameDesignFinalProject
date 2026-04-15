from settings import *
from enums import *

class TitleScreen():

    def __init__(self, game):

        self.game = game


    def startup(self):
        self.image = load_texture("assets/title_screen.png")
        self.scrnwidth, self.scrnheight = get_render_width(), get_render_height()
        self.image_scale = int((self.scrnwidth / 320) + 1)  #320 == image width


    def update(self):

        if is_key_pressed(KeyboardKey.KEY_ENTER):
            self.game.scene_manager.change_scenes(Scenes.CHARACTER_SELECT)


    def draw(self):
        draw_texture_ex(self.image, Vector2(0,0), 0,self.image_scale,WHITE)
        draw_text("TITLESCRN DRAW", 100, 100, 30, RED)


    def shutdown(self):
        unload_texture(self.image)
        