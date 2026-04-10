from pyray import *
from core.game import Game
from settings import *


game = Game()

if __name__ == "__main__":

    init_window(WINDOW_WIDTH,WINDOW_HEIGHT,"game")
    set_target_fps(120)

    toggle_fullscreen()

    game.startup()


    while not window_should_close():

        game.update()
      
        begin_drawing()
        clear_background(WHITE)

        game.draw()

        end_drawing()

close_window()
  
game.shutdown()






