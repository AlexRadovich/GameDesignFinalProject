from settings import *
from enums import *

class CharacterSelectScreen():

    def __init__(self, game):

        self.selection_index = 0
        self.game = game
        self.scrnwidth, self.scrnheight = get_render_width(), get_render_height()


    def startup(self):
        self.char_bg = load_texture("assets/character_select/char1_select_bg.png")
        self.adspace = load_texture("assets/character_select/adspace.png")
        self.test_subject = load_texture("assets/character_select/test_subject.png")
        self.bg = load_texture("assets/character_select/bg.png")
        self.header = load_texture("assets/character_select/headliner.png")
        self.lock = load_texture("assets/character_select/lock.png")

    def update(self):

        if is_key_pressed(KeyboardKey.KEY_ENTER):
            #self.game.scene_manager.change_scenes(Scenes.TITLE)
            self.game.scene_manager.start_level_one((self.selection_index % 2) + 1)
        if is_key_pressed(KeyboardKey.KEY_LEFT) or is_key_pressed(KeyboardKey.KEY_A):
            self.selection_index -= 1
        elif is_key_pressed(KeyboardKey.KEY_RIGHT) or is_key_pressed(KeyboardKey.KEY_D):
            self.selection_index += 1

    def draw(self):

        draw_texture_ex(self.bg, Vector2(0,0), 0, 7, GRAY)

        match self.selection_index % 3:

            case 0:
                draw_texture_ex(self.char_bg, Vector2(220,380), 0, 5, WHITE)
                draw_texture_ex(self.char_bg, Vector2(750,385), 0, 5, GRAY)
                draw_texture_ex(self.char_bg, Vector2(1280,385), 0, 5, GRAY)  

                draw_texture_ex(self.adspace, Vector2(264,392), 0, 2, WHITE)
                draw_texture_ex(self.test_subject, Vector2(794,395), 0, 2, GRAY)


            case 1:
                draw_texture_ex(self.char_bg, Vector2(220,385), 0, 5, GRAY)
                draw_texture_ex(self.char_bg, Vector2(750,380), 0, 5, WHITE)
                draw_texture_ex(self.char_bg, Vector2(1280,385), 0, 5, GRAY)  

                draw_texture_ex(self.adspace, Vector2(264,397), 0, 2, GRAY)
                draw_texture_ex(self.test_subject, Vector2(794,390), 0, 2, WHITE)      
  

            case 2:
                draw_texture_ex(self.char_bg, Vector2(220,385), 0, 5, GRAY)
                draw_texture_ex(self.char_bg, Vector2(750,385), 0, 5, GRAY)
                draw_texture_ex(self.char_bg, Vector2(1280,380), 0, 5, WHITE) 

                draw_texture_ex(self.adspace, Vector2(264,397), 0, 2, GRAY)
                draw_texture_ex(self.test_subject, Vector2(794,395), 0, 2, GRAY)      

        draw_texture_ex(self.lock, Vector2(1410,685), 0, 2, WHITE)      
        draw_texture_ex(self.header, Vector2(self.scrnwidth//2 - 700,40), 0, 7, WHITE)
        #draw_line(self.scrnwidth//2 ,0,self.scrnwidth//2 ,self.scrnheight, RED)


    def shutdown(self):
        unload_texture(self.char_bg)
        unload_texture(self.bg)
        unload_texture(self.header)
        unload_texture(self.adspace)
        unload_texture(self.test_subject)
        unload_texture(self.lock)
        
        