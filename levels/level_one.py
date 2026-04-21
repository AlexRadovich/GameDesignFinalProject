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
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1],
            [1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1],
            [2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2],
            [2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2],
            [2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
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
        pass

    def update(self):
        self.character.update()

    def draw(self):


        for ix, row in enumerate(self.tilemap):
            for ix2, tile in enumerate(row):
                if tile == World.AIR:
                    draw_rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight, SKYBLUE)

                elif tile == World.SOLID:
                    draw_rectangle(ix2*self.blockwidth, ix*self.blockheight, self.blockwidth, self.blockheight, GRAY)



        draw_text(str(self.blockwidth), 100,200,20,BLACK)
        draw_text(str(self.blockheight), 100,220,20,BLACK)
        self.character.draw()

    def shutdown(self):
        pass