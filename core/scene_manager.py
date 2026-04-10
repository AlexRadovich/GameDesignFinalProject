from enums import *

class SceneManager():


    def __init__(self, game):

        self.game = game
        self.current_scene = Scenes.TITLE
        self.screens = {}


    def change_scenes(self,scene):
        self.current_scene = scene


    def add_scene(self, screen, scene):
        self.screens[screen] = scene


    def update(self):
        self.screens[self.current_scene].update()


    def draw(self):
        self.screens[self.current_scene].draw()


