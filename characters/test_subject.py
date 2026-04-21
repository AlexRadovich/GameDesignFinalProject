from settings import *
from enums import *
from pyray import * 

class TestSubject():

    def __init__(self, game, level, position):
        self.game = game
        self.level = level
        self.position = position

    def startup(self):
        pass

    def update(self):
        pass

    def draw(self):
        draw_text("TESTSUBJECT", 100, 300, 20, BLACK)

    def shutdown(self):
        pass
