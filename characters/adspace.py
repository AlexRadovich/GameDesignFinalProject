from settings import *
from enums import *
from pyray import * 
import math

class Adspace():

    def __init__(self, game, level, position):
        self.game = game
        self.level = level

        self.rect = Rectangle(position.x,position.y,self.level.blockwidth * PLAYER_HITBOX_SCALE, self.level.blockheight * PLAYER_HITBOX_SCALE)
        self.speed = PLAYER_SPEED

        self.vx = 0
        self.vy = 0

        self.grounded = True

        self.jump_indicator = Vector2(self.rect.x + .5*(self.rect.width), self.rect.y)
        self.launching = False
        self.time_since_launch = 0
        self.launch_angle = Vector2(0,0)


    def startup(self):
        pass

    def launch(self):
        self.vy -= PLAYER_JUMP_SPEED


    def update(self):
        dt = get_frame_time()
        if self.grounded:
            self.vx = 0

        if(is_key_down(KeyboardKey.KEY_A)and (not self.launching) and self.grounded):
            self.vx -= self.speed  
        elif(is_key_down(KeyboardKey.KEY_A)and (not self.launching)):
            self.vx -= self.speed * PLAYER_JUMP_MOVEMENT

        if(is_key_down(KeyboardKey.KEY_D) and (not self.launching)and self.grounded):
            self.vx += self.speed       
        elif(is_key_down(KeyboardKey.KEY_D)and (not self.launching)):
            self.vx += self.speed * PLAYER_JUMP_MOVEMENT


        if(self.grounded):
            self.vy = 0
            pass

        if(is_key_pressed(KeyboardKey.KEY_W) and self.grounded):
            self.vy -= PLAYER_JUMP_SPEED

        ##Launch logic
        if(is_key_pressed(KeyboardKey.KEY_SPACE) and self.grounded and (not self.launching)):
            self.jump_indicator = Vector2(self.rect.x + .5*(self.rect.width), self.rect.y)
            self.time_since_launch = 0
            self.launching = True

        elif(is_key_pressed(KeyboardKey.KEY_SPACE) and self.launching):
            self.vx = self.launch_angle.x * 10
            self.vy = self.launch_angle.y * 10
            self.launching = False

        elif(self.launching):
            self.time_since_launch += dt
            iter = self.time_since_launch * LAUNCH_ROTATION_SPEED

            launch_y = math.cos((math.pi/2)*math.sin(iter)) * -LAUNCH_INDICATOR_SCALE
            launch_x = math.sin((math.pi/2)*math.sin(iter)) * LAUNCH_INDICATOR_SCALE

            self.launch_angle = (Vector2(launch_x,launch_y))




        

        self.grounded = False

        self.vy += GRAVITY


        self.rect.x += self.vx * dt
        self.handle_collision(self.level.tilemap, 'x')


        self.rect.y += self.vy * dt
        self.handle_collision(self.level.tilemap, 'y')

        self.rect.x = max(0, min(self.level.scrnwidth - self.rect.width, self.rect.x))

    def handle_collision(self, level, axis):
        
        min_tile_x = max(0, int(self.rect.x / self.level.blockwidth))
        max_tile_x = min(len(level[0])-1, int((self.rect.x+self.rect.width) / self.level.blockwidth))

        min_tile_y = max(0, int(self.rect.y / self.level.blockheight))
        max_tile_y = min(len(level)-1, int((self.rect.y+self.rect.height) / self.level.blockheight) + 1)

        for row in range(min_tile_y, max_tile_y + 1):
            for col in range(min_tile_x,max_tile_x + 1):

                if level[row][col] == World.SOLID:
                    block = Rectangle(col * self.level.blockwidth, row * self.level.blockheight, self.level.blockwidth, self.level.blockheight)

                    if check_collision_recs(self.rect, block):
                        
                        if axis == 'x':
                            if self.vx > 0:
                                self.rect.x = block.x - self.rect.width
                            elif self.vx < 0:
                                self.rect.x = block.x + self.level.blockwidth
                            self.vx = 0


                        elif axis == 'y':
                            if self.vy > 0:
                                self.rect.y = block.y - self.rect.height
                                self.grounded = True
                            elif self.vy < 0:
                                self.rect.y = block.y + self.level.blockheight
                            self.vy = 0





    def draw(self):



        draw_rectangle_rec(self.rect, RED)
        draw_text(f"posy:{self.rect.y}" , 500, 500, 30, RED)
        draw_text(f"vy:{self.vy}" , 500, 550, 30, RED)
        draw_text(f"grounded:{self.grounded}" , 500, 600, 30, RED)
        draw_text("ADSPACE", 100, 300, 20, BLACK)

        draw_circle_v(self.jump_indicator, 10, RED)
        draw_text(f"{(self.launch_angle.x), (self.launch_angle.y)}", 400,400,20,RED)
        draw_line_v(self.jump_indicator, vector2_add(self.launch_angle,self.jump_indicator), RED)

    def shutdown(self):
        pass
