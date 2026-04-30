from pyray import *

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800

PLAYER_HITBOX_SCALE      = .6
PLAYER_SPEED             =  300
PLAYER_JUMP_SPEED        =  1750
PLAYER_JUMP_MOVEMENT     =  .7

LAUNCH_ROTATION_SPEED    =  2
LAUNCH_INDICATOR_SCALE   =  300

GRAVITY                  =  70

BOUNCE_COEFF             =  .4

LIGHT_COBBLE_A           =  Rectangle(32,32,32,32)
LIGHT_COBBLE_B           =  Rectangle(64,32,32,32)
DARK_COBBLE_A            =  Rectangle(32,0,32,32)
DARK_COBBLE_B            =  Rectangle(64,0,32,32)
SLOPER_RIGHT             =  Rectangle(96,32,32,32)
SLOPER_LEFT              =  Rectangle(96,0,32,32)