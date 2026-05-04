# Concrete Climb
## By Alex Radovich


## Table of Contents

- [Concrete Climb: Game Design Document](#unnamed-dystopian-platformer)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Game Summary Pitch](#game-summary-pitch)
    - [Inspiration](#inspiration)
    - [Player Experience](#player-experience)
    - [Genre](#genre)
    - [Target Audience](#target-audience)
    - [Technicals](#technical)

  - [Concept](#concept)
    - [Gameplay Overview](#gameplay-overview)
    - [Theme Interpretation](#theme-interpretation)
    - [Mechanics](#mechanics)

  - [Art](#art)
    - [Theme Interpretation](#theme-interpretation-1)
    - [Design](#design)
  - [Audio](#audio)
    - [Sound Effects](#sound-effects)
  - [Game Experience](#game-experience)
    - [UI](#ui)
    - [Controls](#controls)

  - [References](#references)

---


## Introduction

### Game Summary Pitch

In a future version of Colgate where education is overrun and expoited by industry, the only way to survive as a student is to pick up an extra job as a bottom-level worker for a corporation, doing whatever they require for barely any pay.

You've spent your entire time here at the lowest levels of the city block, where no sunlight ever reaches, and pollution sleeps alongside you. 

You study the environment, but after years of living like this, you've all but resigned yourself to your lot in life. But one day, a small seed falls down to you, from the upper levels.

You decide that, even if you would never do it for yourself, this seed deserves to go back to where it came from, to take in the sunlight and sprout.

And so begins the climb.

### Inspiration



**Jump King**

Jump king has a similar idea, where you want to get to the top of a tall tower, and at any point you could fall all the way back down if you take a wrong step.

![Jump King](/assets/GDD/jk.jpg)

**Risk of Rain Returns**

Risk of Rain Returns is a roguelike game with levels, and is about traveling through the world with the goal of reaching a spaceship. It has great level designs and visual storytelling. I really like the variety of enemies and how combat is handled alongside character selection.

![RoRR](/assets/GDD/rorr.webp)


**Cyberpunk and Bladerunner**

These cities and the politics behind their construction in-universe mirror the background for this game, and I think hold a lot of potential for social commentary today, and otherwise are very interesting to look at and make for rich level design.
![Cyberpunk City](/assets/GDD/cyberpunk.jpeg)

![Bladerunner City](/assets/GDD/blade.jpeg)

In general, I ended up opting for a design more inspired by jump king and aesthetic designs that were kind of inspired by the cyberpunk cities, but incorporated into a Colgate theme

### Player Experience

The player clicks through the title screen, selects a character, gets a bit of visual storytelling, then wakes up on the floor at the bottom of a huge, dark metropolis.
There is a seed nearby, which must have fallen down. The player goes to get it, then begins the climb to get the seed to the sun.

![Example Screenshot](/assets/GDD/ex_ss.png)

Demo vid (w/o audio):
https://drive.google.com/file/d/1UaaqbA4x1iTq4WX7zkassLTddmnBkxL4/view?usp=sharing
### Platform

Mac and Windows via Pyray

### Software

- VSCode
- Aseprite

### Genre

Platformer, Frustrating

### Target Audience

Our class, and also any people who are fans of climbing games like Jump King

### Technical

- The crouch/launch mechanic was a really interesting technical thing. It took a lot of debugging and I consulted ChatGPT to get the equations right. I wanted the launch indicator line to move left and right, tracing out a semicircle above the player, but also ease in and out of the motion on the left and right. I used two equations, one for the y value of the line's endpoint, and one for the x value of the endpoint, and anchored the other end of the line at the player's head. This resulted in a vector that I could then scale and add to the player's velocity vector depending on the values of the line when space was pressed again. The equations, usually in terms of x, are in terms of a variable that increments with delta time in order to normalize to frame rate
- The ice block mechanic was also very difficult to get right, and took a lot of debugging. I implemented them by using a special modification of the collision function in adspace.py. If the player is below the diagonal line of a block, (depending on if the slope goes to the right or to the left), the variable "sliding" gets set to true, which locks the player out of moving or jumping manually, and the movement of the player is forced to be horizontally off the edge of the slope, and vertically, gravity draws it back down to the diagonal line. 

## Concept

### Gameplay Overview
The player jumps, and runs around the  levels of a massive city in order to climb up. After ascending high enough, the player leaves the lower levels and reaches an office building, which is the second level. Here the gameplay is more difficult and there are new mechanics with ice. There is also thought given to the hitbox size of the player, which is slightly larger than the player's sprite, so as to implement a version of "coyote time" for the player to make things easier to learn.




### Theme Interpretation
The player selects a character that an environmental studies student, but lives and works and studies in the lowest levels of a massive city. They have never actually seen the nature they study, but they know that a seed needs sun to grow, so when one falls down to them, they decide to do whatever it takes to get it away from the awful world they know. 

The levels are based around climbing and trying again to climb back up when one inevitably falls down.


### Mechanics

* Level One Mechanics:

| Mechanic | Description |
| --- | --- |
| **Small Jump** | Pressing W will initiate a small jump |
| **Launch Stance** | Pressing Space will lock you into a launching animation, and begin showing a launching indicator that moves back and forth. |
| **Launch Jump** | While in launch stance, pressing space will launch you in the direction of the launch indicator |
| **Bonking** | Hitting the side of a block while midair will "bonk" you off of it, reversing your horizontal velocity and having often devastating consequences, or necessary benefits within the level|

---
---


* Level Two Mechanics:

| Mechanic | Description |
| --- | --- |
| **Ice** | Ice blocks are introduced, which will force your movement and restict jumping ability while on them |
| **Flower pot** | Reaching the flower pot and touching it will plant the seed that you have, creating a small plant,which triggers the victory condition |

## Art

### Theme Interpretation
There will be a dark, grimy, background and broken cobblestones all around the lower levels. It will be dark and everything will be stone. In the upper levels, in the office building, there is visible light and things are much brighter. It is clearly far above where you started. The blocks here are clean concrete and cold ice. 


### Design
I used Aseprite to design all of the art for this game. The design largely follows the aesthetics of the cities in Cyberpunk and Bladerunner, as interpreted by my own artstyle and incorporated into the narrative of an overrun Colgate. 


## Audio


### Sound Effects
Jumping and walking will have basic foley noises attached to them, sourced from other, similar games.


### UI

The user will have an experience that is very similar to Jump King, but with a different core skill (control of the launching mechanic)

### Controls


- A and D for left and right movement
- W to small jump
- Space bar to enter crouch mode
- Space bar again to launch out of crouch mode

---


## References

- [Owl Chemist GDD](https://docs.google.com/document/d/1_iPOdIFm9iiRNyMTM2WL3YTD0CGeOks3YKBjTsDJvd8/edit?tab=t.0#heading=h.k2hqrk99qjg6)
- https://evilduckk.itch.io/hel-circle-sfx-and-music (for sound effects)
- https://github.com/NguyenLe15325/Python-raylib/blob/main/11.2D_platformer_clone.py (for some basic code structure and implementation ideas)
- I used Claude once for some debugging on the ice block collision, but I ended up editing what it wrote anyway
- I used ChatGPT to generate the equations to use for the sinusoidal motion of the launch indicator