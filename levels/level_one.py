from settings import *
from enums import *
from characters.adspace import Adspace
from characters.test_subject import TestSubject

class LevelOne():

    def __init__(self, game):

        self.game = game
        self.won = False
        self.start = True

        self.tilemap11 = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,16,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,14,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,1,1,1],
        ]
        self.tilemap10 = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,14,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,10,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,12,12,12,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,12,12,12,12,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,12,12,12,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
        ]
        self.tilemap9 = [
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,12,12,12,1,1,1,1,1,1,1,1,13,1,1,1],
            [1,1,1,11,1,1,1,1,12,12,12,12,12,12,12,1,1,1,1,13,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,13,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,13,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,13,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,13,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,13,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,12],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,12,12,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,12,12,12,12,1,1,1,1,11,1,1,1],
        ]

        self.tilemap8 = [
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,12,12,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,12,12,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,12,12,12,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,12,12,12,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,12,12,12,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
        ]
        self.tilemap7 = [
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,12,12,12,12,12,12,12,12,12,12,12,12,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,12,1,1,12,1,1,12,1,1,12,12,12,1,1,11,1,1,1],
            [1,1,1,11,1,12,1,1,12,1,1,12,1,1,1,1,12,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,12,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,12,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,4,12,12,12,1,1,1,1,11,1,1,1],
        ]
        self.tilemap6 = [
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,8,8,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,12,12,12,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,12,12,12,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,12,12,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,12,5,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,12,12,5,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,12,12,12,5,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,12,12,12,12,1,1,12,12,1,1,1,1,1,1,1,11,1,1,1]
        ]
        self.tilemap5 = [
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,12,12,12,12,12,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,12,12,12,12,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,12,12,12,12,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1],
            [1,1,1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,1,1,1]
        ]
        self.tilemap4 = [
            [1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,9,9,1,1,1,1,1,1],
            [1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,9,9,1,1,1,1,1,1],
            [1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,9,9,1,1,1,1,1,1],
            [1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,9,9,1,1,1,1,1,1],
            [1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,9,9,1,1,1,1,1,1],
            [1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,9,9,1,1,1,1,1,1],
            [1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,9,9,1,1,1,1,1,1],
            [1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,9,9,1,1,1,1,1,1],
            [1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,9,9,1,1,1,1,1,1],
            [1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,9,9,1,1,1,1,1,1],
            [1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,9,9,1,1,1,1,1,1],
            [1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,10,9,1,1,1,1,1,1],
            [1,1,1,1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,1,1,1,1]
        ]
        self.tilemap3 = [
            [1,1,1,1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,1,1,1],
            [1,1,1,1,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,1,1,6],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
            [8,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
            [6,6,6,1,1,6,1,1,6,1,1,6,6,6,6,6,6,6,6,6,1,1,6],
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
            [6,6,6,1,1,1,1,1,1,6,6,6,6,6,6,1,16,1,1,1,6,6,6],
            [6,6,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,6,6],
            [6,6,6,8,1,1,1,1,1,1,1,1,1,1,1,1,17,1,1,1,6,6,6],
            [7,7,7,7,2,2,2,2,2,7,7,7,7,7,7,2,2,2,2,2,7,7,7]
        ]

        self.maps = [self.tilemap,self.tilemap2,self.tilemap3, self.tilemap4, self.tilemap5, self.tilemap6, self.tilemap7, self.tilemap8, self.tilemap9, self.tilemap10, self.tilemap11]
        
        self.current_screen = 0
        self.scrnwidth, self.scrnheight = get_render_width(), get_render_height()
        self.blockwidth, self.blockheight = int(self.scrnwidth/len(self.tilemap[0]) +1), int(self.scrnheight/len(self.tilemap) +1)
        


    def victory(self):
        self.won = True
         
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
        self.bg2 = load_texture("assets/lvl2_bg.png")
        self.bg2_end = load_texture("assets/lvl2_end_bg.png")

    def update(self):
        self.character.update()


        if self.character.rect.y <= 0:
            self.current_screen += 1
            self.character.rect.y += self.scrnheight
            self.start = False
            #print(f"UP {self.character.rect.y}")

        if self.character.rect.y > self.scrnheight+5:
            self.current_screen -= 1
            self.character.rect.y -= self.scrnheight
            #print(f"DOWN {self.character.rect.y}")


    def draw(self):





        if self.current_screen <= 3:
            draw_texture_ex(self.bg,Vector2(0,0),0,int(self.scrnwidth/320 + 1), WHITE)
        elif self.current_screen == 10:
            draw_texture_ex(self.bg2_end,Vector2(0,0),0,int(self.scrnwidth/320 + 1), WHITE)

        else:
            draw_texture_ex(self.bg2,Vector2(0,0),0,int(self.scrnwidth/320 + 1), WHITE)
        if self.won:
            draw_text("CONGRATULATIONS!",self.scrnwidth//2-300, self.scrnheight//2 - 10 , 70 , WHITE)
        #draw_text(f"{self.won=}", 300,300,30,RED)
        #draw_text(f"HI", 0,0,30,RED)
        for ix, row in enumerate(self.maps[self.current_screen]):
            for ix2, tile in enumerate(row):
                match tile:
                     
                    case World.SEED:
                            draw_texture_pro(self.sheet, SEED, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)
                     
                    case World.ARROW:
                            draw_texture_pro(self.sheet, ARROW, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)

                    case World.POT:
                            draw_texture_pro(self.sheet, POT, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)

                    case World.POT_PLANT:
                            draw_texture_pro(self.sheet, POT_PLANT, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)

                    case World.WINDOW_TRANSPARENT:
                            draw_texture_pro(self.sheet, WINDOW_T, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)


                    case World.SOLID:
                            draw_texture_pro(self.sheet, SOLID, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)


                    case World.HARD_WINDOW:
                            draw_texture_pro(self.sheet, WINDOW, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)

                    case World.DOOR:
                            draw_texture_pro(self.sheet, DOOR, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)


                    case World.WINDOW:
                            draw_texture_pro(self.sheet, WINDOW, Rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight), [],0,WHITE)


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


        #draw_text(str(self.blockwidth), 100,200,20,BLACK)
        #draw_text(str(self.blockheight), 100,220,20,BLACK)

        if self.start:
            draw_text("GET THE SEED TO THE SUN!", self.scrnwidth//2,self.scrnheight//3*2,40, GREEN)
        self.character.draw()

    def shutdown(self):
        unload_texture(self.sheet)        
        unload_texture(self.bg)
        unload_texture(self.bg2)
        self.character.shutdown()