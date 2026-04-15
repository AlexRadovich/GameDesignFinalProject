import settings
import enums
from pyray import * 

class TestSubject():

    def __init__(self, game):
        self.game = game

    def startup(self):
        pass

    def update(self):
        pass

    def draw(self):
        draw_text("TESTSUBJECT", 100, 300, 20, BLACK)

    def shutdown(self):
        pass
