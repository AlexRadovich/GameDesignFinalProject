from settings import *
from enums import *
from characters.adspace import Adspace
from characters.test_subject import TestSubject

class LevelOne():

    def __init__(self, game):

        self.game = game
        self.scrnwidth, self.scrnheight = get_render_width(), get_render_height()

        self.tilemap = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
        ]

    def assign_character(self, selection):
        match selection:
            case Characters.ADSPACE:
                character = Adspace(self.game)
            case Characters.TESTSUBJECT:
                character = TestSubject(self.game)
        self.character = character

    def startup(self):
        pass

    def update(self):
        self.character.update()

    def draw(self):
        self.character.draw()
        draw_text(str(self.character), 100,100,20,BLACK)

        for ix, row in enumerate(self.tilemap):
            for ix2, tile in enumerate(row):
                if tile == 1:
                    draw_rectangle(ix2*50, ix*50, 50, 50, SKYBLUE)

                elif tile == 2:
                    draw_rectangle(ix2*50, ix*50, 50, 50, GRAY)

    def shutdown(self):
        pass