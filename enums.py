from enum import IntEnum


class Scenes(IntEnum):

    TITLE = 1
    CHARACTER_SELECT = 2
    LEVEL_ONE = 3

class Characters(IntEnum):

    ADSPACE = 1
    TESTSUBJECT = 2

class World(IntEnum):

    AIR = 1
    LIGHTCOBBLE = 2
    ROPE = 3
    SLOPELEFT = 4
    SLOPERIGHT = 5
    BRICK = 6
    DARKCOBBLE = 7
    CRATE = 8
    WINDOW = 9
    DOOR = 10
    HARD_WINDOW = 11
    SOLID = 12
    WINDOW_TRANSPARENT = 13
    POT = 14
    POT_PLANT = 15
    ARROW = 16
    SEED = 17

class Anims(IntEnum):

    WALKING = 1
    IDLE = 2
    LAUNCHING = 3
    AIRBORNE = 4