from settings import *
from enums import *
from characters.adspace import Adspace
from characters.test_subject import TestSubject

class LevelOne():

    def __init__(self, game):

        self.game = game
        self.tilemap = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,4,2,1,1,1,1,1,1,2,5,1,1,1,1],
            [1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,2,5,1,1,1],
            [1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,2,5,1,1],
            [1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,4,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
        ]
        self.scrnwidth, self.scrnheight = get_render_width(), get_render_height()
        self.blockwidth, self.blockheight = int(self.scrnwidth/len(self.tilemap[0]) +1), int(self.scrnheight/len(self.tilemap) +1)
        

    def assign_character(self, selection):

        match selection:
            case Characters.ADSPACE:
                character = Adspace(self.game, self, Vector2(self.scrnwidth//2, self.scrnheight//9 * 8))
            case Characters.TESTSUBJECT:
                character = TestSubject(self.game, self, Vector2(self.scrnwidth//2, self.scrnheight//9 * 8))

        self.character = character

    def startup(self):
        self.sheet = load_texture("assets/tilemap.png")
        self.bg = load_texture("assets/lvl1_bg.png")

    def update(self):
        self.character.update()

    def draw(self):

        draw_texture_ex(self.bg,Vector2(0,0),0,int(self.scrnwidth/320 + 1), WHITE)

        for ix, row in enumerate(self.tilemap):
            for ix2, tile in enumerate(row):
                match tile:
                    case World.AIR:
                        pass
                    #draw_rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight, SKYBLUE)

                    case World.SOLID:
                        if ix2%2 == 0:
                        #draw_rectangle_pro(Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [], 0, GREEN)
                            draw_texture_pro(self.sheet, LIGHT_COBBLE_A, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)
                        else:
                            draw_texture_pro(self.sheet, DARK_COBBLE_B, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)
                    
                    case World.SLOPELEFT:
                        draw_texture_pro(self.sheet, SLOPER_LEFT, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)

                    case World.SLOPERIGHT:
                        draw_texture_pro(self.sheet, SLOPER_RIGHT, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)


        draw_text(str(self.blockwidth), 100,200,20,BLACK)
        draw_text(str(self.blockheight), 100,220,20,BLACK)
        self.character.draw()

    def shutdown(self):
        unload_texture(self.sheet)        
        unload_texture(self.bg)