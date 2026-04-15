from enums import *

class SceneManager():


    def __init__(self, game):

        self.game = game
        self.current_scene = Scenes.TITLE
        self.screens = {}


    def change_scenes(self,scene):
        self.current_scene = scene

    def start_level_one(self, character):
        self.current_scene = Scenes.LEVEL_ONE
        self.screens[self.current_scene].assign_character(character)

    def add_scene(self, screen, scene):
        self.screens[screen] = scene
        self.screens[screen].startup()


    def update(self):
        self.screens[self.current_scene].update()


    def draw(self):
        self.screens[self.current_scene].draw()

    def shutdown(self):
        for scene in self.screens:
            scene.shutdown()


