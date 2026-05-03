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
        self.bonusx = 0


        self.jump_indicator = Vector2(self.rect.x + .5*(self.rect.width), self.rect.y)
        self.launching = False
        self.time_since_launch = 0
        self.launch_angle = Vector2(0,0)

        self.facing_right = False
        self.grounded = True
        self.sliding = False
        self.cheats = False

        self.timing = 0
        self.frame = 1
        self.anim = Anims.IDLE




    def startup(self):
        self.tiles = load_texture("assets/adspace_tiles.png")

    def launch(self):
        self.vy -= PLAYER_JUMP_SPEED


    def update(self):
        dt = get_frame_time()
        self.timing += dt
        if is_key_pressed(KeyboardKey.KEY_C):
            self.cheats = not self.cheats

        if self.timing > PLAYER_ANIMATION_FPS:
            self.timing = 0
            self.frame += 1
        
        self.bonusx = 0


        if self.grounded:
            self.vx = 0

        left = is_key_down(KeyboardKey.KEY_A) or is_key_down(KeyboardKey.KEY_LEFT)
        right = is_key_down(KeyboardKey.KEY_D) or is_key_down(KeyboardKey.KEY_RIGHT)
        if(left and (((not self.launching) and self.grounded) or self.cheats)):
            self.vx -= self.speed  
            self.facing_right = False
            self.anim = Anims.WALKING
            if self.cheats:
                self.vx = max(self.vx,-100)

        elif(left and (not self.launching)):
            self.bonusx = self.speed * -PLAYER_JUMP_MOVEMENT

        if(right and (((not self.launching) and self.grounded) or self.cheats)):
            self.vx += self.speed      
            self.facing_right = True
            self.anim = Anims.WALKING
            if self.cheats:
                self.vx = min(self.vx,100)

        elif(right and (not self.launching)):
            self.bonusx = self.speed * PLAYER_JUMP_MOVEMENT

        elif(not is_key_down(KeyboardKey.KEY_A) and not is_key_down(KeyboardKey.KEY_D)):
            self.anim = Anims.IDLE

        if(not self.grounded and self.vx == 0 and self.vy == 0):
            self.vx += self.speed
        
        if(self.grounded and self.vx == 0):
            self.anim = Anims.IDLE


        if(self.launching):
            self.anim = Anims.LAUNCHING

        if not self.grounded:
            self.anim = Anims.AIRBORNE


        if(self.grounded):
            self.vy = 0
            pass

        if(is_key_pressed(KeyboardKey.KEY_W) and self.grounded and not self.launching):
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

            if not self.facing_right:
                iter += 7*math.pi/8
            else:
                iter -= math.pi /8

            launch_y = math.cos((math.pi/2)*math.sin(iter)) * -LAUNCH_INDICATOR_SCALE
            launch_x = math.sin((math.pi/2)*math.sin(iter)) * LAUNCH_INDICATOR_SCALE

            self.launch_angle = (Vector2(launch_x,launch_y))




        

        self.grounded = False

        if not self.cheats:
            self.vy += GRAVITY 
        else:
            self.vy -= 10

        #self.vx += self.bonusx
        if self.vx > 0:
            self.facing_right = True


        self.rect.y += self.vy * dt
        self.handle_collision(self.level.maps[self.level.current_screen], 'y')
        self.rect.x += (self.vx ) * dt
        self.handle_collision(self.level.maps[self.level.current_screen], 'x')



        self.rect.x = max(0, min(self.level.scrnwidth - self.rect.width, self.rect.x))

    def handle_collision(self, level, axis):
        
        min_tile_x = max(0, int(self.rect.x / self.level.blockwidth))
        max_tile_x = min(len(level[0])-1, int((self.rect.x+self.rect.width) / self.level.blockwidth))

        min_tile_y = max(0, int(self.rect.y / self.level.blockheight))
        max_tile_y = min(len(level)-1, int((self.rect.y+self.rect.height) / self.level.blockheight) + 1)

        for row in range(min_tile_y, max_tile_y + 1):
            for col in range(min_tile_x,max_tile_x + 1):

                if level[row][col] == World.POT:
                    level[row][col] = World.POT_PLANT
                    self.level.victory()


                if level[row][col] == World.DOOR:
                    self.level.current_screen += 1
                    self.rect.x = self.level.scrnwidth//2
                    self.vx = 0
                    self.vy = 0
                    self.rect.y = self.level.scrnheight * 7/8
                    #self.rect.y -= self.level.scrnheight


                # ── SLOPERIGHT: \ hypotenuse from (tile_left, tile_top) → (tile_right, tile_bottom) ──
                if level[row][col] == World.SLOPERIGHT:
                    tile_left   = col  * self.level.blockwidth
                    tile_top    = row  * self.level.blockheight
                    tile_right  = (col + 1) * self.level.blockwidth
                    tile_bottom = (row + 1) * self.level.blockheight
                    bw = self.level.blockwidth
                    bh = self.level.blockheight

                    player_left   = self.rect.x
                    player_right  = self.rect.x + self.rect.width
                    player_top    = self.rect.y
                    player_bottom = self.rect.y + self.rect.height

                    # Fast AABB reject — skip if bounding boxes don't overlap at all
                    if not (player_right > tile_left and player_left < tile_right and
                            player_bottom > tile_top  and player_top  < tile_bottom):
                        continue

                    # Surface formula for \ slope:
                    #   slope_y(x) = tile_top  + (x - tile_left) * (bh / bw)
                    #   slope_x(y) = tile_left + (y - tile_top)  * (bw / bh)   ← inverted ratio!

                    if axis == 'y':
                        # Use right foot for \ (right side sits lower on the slope)
                        foot_x  = max(tile_left, min(player_right, tile_right))
                        slope_y = tile_top + (foot_x - tile_left) * (bh / bw)

                        if self.vy >= 0 and player_bottom >= slope_y:
                            self.rect.y = slope_y - self.rect.height  # push up onto surface
                            self.vy     = 0
                            self.sliding = True

                        elif axis == 'x':
                            if self.vx > 0:
                                foot_x = min(player_right, tile_right)
                                slope_y_at_foot = tile_top + (foot_x - tile_left) * (bh / bw)
                                if player_right > tile_left and player_bottom > slope_y_at_foot:
                                    self.rect.x = tile_left - self.rect.width
                                    self.vx = 0

                        # Moving left into the hypotenuse is NOT a wall — the y-axis pass
                        # handles snapping the player onto the surface. No x correction needed.


                # ── SLOPELEFT: / hypotenuse from (tile_right, tile_top) → (tile_left, tile_bottom) ──
                elif level[row][col] == World.SLOPELEFT:
                    tile_left   = col  * self.level.blockwidth
                    tile_top    = row  * self.level.blockheight
                    tile_right  = (col + 1) * self.level.blockwidth
                    tile_bottom = (row + 1) * self.level.blockheight
                    bw = self.level.blockwidth
                    bh = self.level.blockheight

                    player_left   = self.rect.x
                    player_right  = self.rect.x + self.rect.width
                    player_top    = self.rect.y
                    player_bottom = self.rect.y + self.rect.height

                    if not (player_right > tile_left and player_left < tile_right and
                            player_bottom > tile_top  and player_top  < tile_bottom):
                        continue

                    # Surface formula for / slope:
                    #   slope_y(x) = tile_top  + (tile_right - x) * (bh / bw)
                    #   slope_x(y) = tile_right - (y - tile_top)  * (bw / bh)

                    if axis == 'y':
                        # Use left foot for / (left side sits lower on the slope)
                        foot_x  = max(tile_left, min(player_left, tile_right))
                        slope_y = tile_top + (tile_right - foot_x) * (bh / bw)

                        if self.vy >= 0 and player_bottom >= slope_y:
                            self.rect.y = slope_y - self.rect.height
                            self.vy     = 0
                            self.sliding = True

                        elif axis == 'x':
                            if self.vx < 0:
                                foot_x = max(player_left, tile_left)
                                slope_y_at_foot = tile_top + (tile_right - foot_x) * (bh / bw)
                                if player_left < tile_right and player_bottom > slope_y_at_foot:
                                    self.rect.x = tile_right
                                    self.vx = 0

                if (level[row][col] == World.LIGHTCOBBLE  or level[row][col] == World.BRICK or level[row][col] == World.DARKCOBBLE or level[row][col] == World.CRATE or level[row][col] == World.HARD_WINDOW or level[row][col] == World.SOLID):
                    block = Rectangle(col * self.level.blockwidth, row * self.level.blockheight, self.level.blockwidth, self.level.blockheight)

                    if check_collision_recs(self.rect, block):
                        
                        if axis == 'x':
                            if self.vx > 0: #move right
                                self.rect.x = block.x - self.rect.width

                            elif self.vx < 0: #move left
                                self.rect.x = block.x + self.level.blockwidth
                            self.vx *= -BOUNCE_COEFF
                            


                        elif axis == 'y':
                            if self.vy > 0:
                                self.rect.y = block.y - self.rect.height
                                self.grounded = True
                            elif self.vy < 0:
                                self.rect.y = block.y + self.level.blockheight
                            self.vy = 0





    def draw(self):



        draw_rectangle_rec(self.rect, TRANSPARENT)
        draw_text(f"posy:{self.rect.y}" , 500, 500, 30, RED)
        draw_text(f"vy:{self.vy}" , 500, 550, 30, RED)
        draw_text(f"grounded:{self.grounded}" , 500, 600, 30, RED)
        draw_text(f"vx:{self.vx}" , 500, 650, 30, RED)
        draw_text(f"sliding:{self.sliding}" , 500, 700, 30, RED)
        draw_text("ADSPACE", 100, 300, 20, BLACK)
        #scaled = Rectangle(self.rect.x + (self.rect.width/12), self.rect.y + (self.rect.height/6), self.rect.width * 5/6, self.rect.height * 5/6)
        #draw_rectangle_rec(scaled,GREEN)
        draw_text(f"{self.anim=}", 600,600,30,GREEN)
        rec = Rectangle(self.rect.x -5, self.rect.y - 10, self.rect.width + 10, self.rect.height+10)
        match self.anim:

            case Anims.AIRBORNE:
                if self.facing_right:
                    draw_texture_pro(self.tiles,Rectangle(((self.frame %1) * 32), 96, 32, 32 ), rec, Vector2(0,0),0,WHITE)
                else:
                    draw_texture_pro(self.tiles,Rectangle(((self.frame %1) * 32), 96, -32, 32 ), rec, Vector2(0,0),0,WHITE)


            case Anims.LAUNCHING:
                if self.facing_right:
                    draw_texture_pro(self.tiles,Rectangle(0,64,32,32),rec, Vector2(0,0),0,WHITE)
                else:
                    draw_texture_pro(self.tiles,Rectangle(0,64,-32,32),rec, Vector2(0,0),0,WHITE)


            case Anims.IDLE:
                if self.facing_right:
                    draw_texture_pro(self.tiles,Rectangle(((self.frame %2) * 32) ,32,32,32 ), rec, Vector2(0,0),0,WHITE)
                else:
                    draw_texture_pro(self.tiles,Rectangle(((self.frame %2) * 32) ,32,-32,32 ), rec, Vector2(0,0),0,WHITE)

            case Anims.WALKING:
                if self.facing_right:
                    draw_texture_pro(self.tiles,Rectangle(((self.frame %4) * 32) ,0,32,32 ), rec, Vector2(0,0),0,WHITE)
                else:
                    draw_texture_pro(self.tiles,Rectangle(((self.frame %4) * 32) ,0,-32,32 ), rec, Vector2(0,0),0,WHITE)


        draw_text(f"{(self.launch_angle.x), (self.launch_angle.y)}", 400,400,20,RED)

        if self.launching:
            draw_circle_v(self.jump_indicator, 10, RED)

            draw_line_ex(self.jump_indicator, vector2_add(self.launch_angle,self.jump_indicator), 3,RED)

            #draw_line_v(self.jump_indicator, vector2_add(self.launch_angle,self.jump_indicator), RED)

    def shutdown(self):
        unload_texture(self.tiles)
