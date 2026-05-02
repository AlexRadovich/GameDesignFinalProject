from settings import *
from enums import *
from characters.adspace import Adspace
from characters.test_subject import TestSubject

class LevelOne():

    def __init__(self, game):

        self.game = game

        self.tilemap4 = [
            [1,1,1,1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,1,1,1],
            [1,1,1,1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,1,1,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
            [1,6,6,1,1,6,1,1,6,1,1,6,6,6,6,6,6,6,6,6,1,1,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,6,1,1,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,6,1,1,6,6,6,6,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,6,6,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,6,6,6,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,6,6,6,6,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
        self.tilemap3 = [
            [1,1,1,1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,1,1,1],
            [1,1,1,1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,1,1,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
            [1,6,6,1,1,6,1,1,6,1,1,6,6,6,6,6,6,6,6,6,1,1,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,6,1,1,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,6,1,1,6,6,6,6,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,6,6,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,6,6,6,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,6,6,6,6,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
        self.tilemap2 = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,6,6,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,6,6,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,6,6,6,6,6,6,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,6,6,6,6,6,6,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,6,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,6,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,6,6],
            [1,1,1,1,1,1,1,1,1,1,6,6,6,6,6,1,1,1,1,1,6,6,6],
            [1,1,1,1,1,1,1,6,6,6,6,6,6,6,6,1,1,1,1,1,6,6,6],
            [1,1,1,1,1,1,1,6,6,6,6,6,6,6,6,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
        self.tilemap = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [6,6,6,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [6,6,6,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [6,6,6,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [6,6,6,1,1,1,1,1,1,6,6,6,6,6,6,1,1,1,1,1,1,1,1],
            [6,6,6,1,1,1,1,1,1,6,6,6,6,6,6,1,1,1,1,1,1,1,1],
            [6,6,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,6,6],
            [6,6,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,6,6],
            [6,6,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,6,6],
            [6,6,6,1,1,1,1,1,1,6,6,6,6,6,6,1,1,1,1,1,6,6,6],
            [6,6,6,1,1,1,1,1,1,6,6,6,6,6,6,1,1,1,1,1,6,6,6],
            [6,6,6,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,6,6],
            [7,7,7,7,2,2,2,2,2,7,7,7,7,7,7,2,2,2,2,2,7,7,7]
        ]

        self.maps = [self.tilemap,self.tilemap2,self.tilemap3, self.tilemap4]
        
        self.current_screen = 0
        self.scrnwidth, self.scrnheight = get_render_width(), get_render_height()
        self.blockwidth, self.blockheight = int(self.scrnwidth/len(self.tilemap[0]) +1), int(self.scrnheight/len(self.tilemap) +1)
        

    def assign_character(self, selection):

        match selection:
            case Characters.ADSPACE:
                character = Adspace(self.game, self, Vector2(self.scrnwidth//2, self.scrnheight//9 * 8))
            case Characters.TESTSUBJECT:
                character = TestSubject(self.game, self, Vector2(self.scrnwidth//2, self.scrnheight//9 * 8))

        self.character = character
        self.character.startup()

    def startup(self):
        self.sheet = load_texture("assets/tilemap.png")
        self.bg = load_texture("assets/lvl1_bg.png")

    def update(self):
        self.character.update()


        if self.character.rect.y <= 0:
            self.current_screen += 1
            self.character.rect.y += self.scrnheight
            #print(f"UP {self.character.rect.y}")

        if self.character.rect.y > self.scrnheight+5:
            self.current_screen -= 1
            self.character.rect.y -= self.scrnheight
            #print(f"DOWN {self.character.rect.y}")


    def draw(self):

        draw_texture_ex(self.bg,Vector2(0,0),0,int(self.scrnwidth/320 + 1), WHITE)

        for ix, row in enumerate(self.maps[self.current_screen]):
            for ix2, tile in enumerate(row):
                match tile:
                    case World.AIR:
                        pass

                    case World.LIGHTCOBBLE:
                        if ix2%2 == 0:
                            draw_texture_pro(self.sheet, LIGHT_COBBLE_A, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)
                        else:
                            draw_texture_pro(self.sheet, LIGHT_COBBLE_B, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)

                    case World.DARKCOBBLE:
                        if ix2%2 == 0:
                            draw_texture_pro(self.sheet, DARK_COBBLE_A, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)
                        else:
                            draw_texture_pro(self.sheet, DARK_COBBLE_B, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)

                    case World.CRATE:
                        draw_texture_pro(self.sheet, CRATE, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)
                    
                    case World.BRICK:
                        draw_texture_pro(self.sheet, BRICK, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)
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
        self.character.shutdown()