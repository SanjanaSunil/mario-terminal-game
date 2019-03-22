# (Not So Super) Mario Bros. Game

<details><summary>Table of Contents</summary><p>

- [1. Running the game](#running-the-game)
- [2. Features](#features)
	- [2.1. Characters](#characters)
	- [2.2. Levels](#levels)
    - [2.3. Coins and Powerups](#coins-and-powerups)
- [3. Controls](#controls)
- [4. Playing the game](#playing-the-game)
- [5. Additional features](#additional-features)

</p></details><p></p>

## Running the game

```
    pip3 install -r requirements.txt
    python3 main.py
```

## Features

### Characters

* Mario is a stickman generated in the middle of the screen at the start. Mario is allowed to move left, move right and jump. If mario is at the center of the screen, the screen dynamically changes.

* Regular enemies are indicated by a black robots with red marks. They can move left or right. On passing through them, Mario dies. If Mario jumps on the enemies, they die and disappear and the score increases by 10. 

* The Boss Enemy is a dragon generated at the end of the game. It has ten lives and Mario has to keep shooting at the enemy to kill it to win the game (the score increments by 10 each time it manages to shoot).

### Levels

* Ground level. The level has platforms that Mario can jump on. It also has holes filled with lava in it that Mario dies if it fall into it. 
* Water level (NOTE: Mario can walk on water). The water level has more enemies on it than the previous levels and has platforms, but no holes.
* At the ending, Mario has to defeat the boss enemy. 

### Coins and Powerups

* There are coins ($) in the game. Collecting one coin increments the score by one.
* There are health tokens (+) in the game. Collecting them increases Mario's health by one (with a maximum health limit being 5).

## Controls

* Press 'w' to jump.
* Press 'a' to move left.
* Press 'd' to move right.
* Press 'q' at any time to quit.
* When the dragon boss enemy appears at the end, Mario is given the functionality to shoot bullets by pressing the spacebar.

## Playing the game

* When the game starts, enter your name and press enter.

* Start moving Mario using the control keys. 

* Make sure you don't collide with an enemy! If you do, you'll respawn from the top of the screen and lose a life as indicated at the bottom of the screen. If you jump on an enemy, it will die and you'll gain 10 points.

* Collect powerups to increase number of lives and coins to increase score. Number of lives can at any time be maximum five. 

* At the end of the game, you'll have to destroy the dragon by pressing the spacebar key multiple times.

* After the game ends, your score will be displayed on your terminal.

## Additional features

* Colorama module has been used to generate colors.
* Music plays in the background at the start of the game and whenever Mario loses a life.
