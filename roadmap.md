Initial Commit 4/8/26

### 04/08/2026 Lab Session 10:50 a.m.

* Goal: 
implement scroll to zoom camera around the mouse via the previous implementation method using get_screen_to_world_2d() and get_mouse_position(). Also add the ability to drop through platforms via use of the down key, and adding a new tilemamp class.

* Implementation:
Technical Plan/Credit: [raylib tut](https://github.com/blep/pyray_examples/blob/main/raylib_official_examples/core/core_2d_camera_mouse_zoom.py)
platform is original implementation

* Commit message: 
feat(scroll to zoom & drop through platforms): Can zoom in/out around the cursor by scrolling up/down. Can drop through platforms when grounded on them by pressing down.

* Next/To-do:
Start final project out of lab, brainstorm game ideas

### 04/08/2026 6 p.m.

* Goal:
set up the file structure and hierarchy in such a way that I can easily modify or scale systems or ideas later. Get the base game state up and running.

* Implementation:
Using the previous semester projects to work out the basic structure/game loop. I might look up some things to help with more advanced file structure ideas.

* Commit message:
chore(files): set up file strucure and game skeleton

* Next/To-do:
Design screens and first character

### 04/12/2026 9 p.m.

* Goal:
implement the character select screen and maybe some of the actual characters that could be selected

* Implementation:
Use my Mid-semester menu select screen as an idea and build off of that. Drawings made using aseprite

* Commit message:
feat(character): added character select screen 

* Next/To-do:
Make title screen or level one, finish character designs


### 04/15/2026 10 a.m.

* Goal: 
start the development of level one, tie in the character select

* Implementation:
use the https://github.com/NguyenLe15325/Python-raylib/blob/main/11.2D_platformer_clone.py file as inspiration on how to encode a level into a tilemap, include my character selection logic

* Commit message:
chore(lvl1): add the core structure for level one and the basic foundations for getting the character in the level

* Next/To-do:
flesh out lvl 1 more

### 4/21/2026 3 p.m.

* Goal:
Flesh out the sizings and tilemap for level one, add basic movement functionality to the character so that they can interact with the level

* Implementation:
Use Aseprite for drawing and the tilemap implementation we saw in class and https://github.com/NguyenLe15325/Python-raylib/blob/main/11.2D_platformer_clone.py 

* Commit message:
feat(lvl1) implemented character movement within and interactions within level one.

* Next/To-do:
do lvl 1 art and begin either camera work or title screen art
