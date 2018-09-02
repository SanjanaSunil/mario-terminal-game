import os
import config
import scenes
import people
import global_var
import global_funct
import random
import time
import bullets
from colorama import init, Fore, Back, Style

if __name__ == "__main__":

    os.system('tput reset')
    print("Enter your name: ")
    global_var.username = input()
    os.system('tput reset')
    config.create_banner()

    mario = people.Person(config.mario, int(config.columns/2), global_var.scenery.ground_level-len(config.mario))
    # mario.posx = 1035
    # global_var.scenery.scene_start_index = 1030
    mario.render()

    # Generate enemies
    global_funct.generate_enemies()

    global_var.scenery.render()
    global_funct.create_footer()
    os.system('aplay newstart.wav&')

    while True:

        if global_var.lives <= 0:
            global_funct.display_ending("YOU LOST!")
            break

        if global_var.quit_flag:
            global_funct.display_ending("YOU LOST!")
            break

        global_funct.run_background(mario)

        mario.gravity() 

        global_funct.check_enemies(mario)

        event = config.get_key(config.get_input())

        if event == config.QUIT:
            global_funct.display_ending("YOU QUITTER!")
            break
    
        elif event == config.LEFT:
            mario.check_left()

        elif event == config.RIGHT:
            mario.check_right()

        elif event == config.UP:
            mario.jump()

        # Fire bullet at boss enemy 
        elif event == config.FIRE and mario.posx >= global_var.scenery.scene_length-config.columns:
            if not global_var.bullet_present:
                bullet = bullets.Bullet(mario.posx+mario.width, int(mario.posy+mario.height/2))
                global_var.bullet_present = True

        # Another bullet shouldn't fire until the previous one has disappeared
        if global_var.bullet_present:
            if bullet.posx >= global_var.scenery.scene_length-int(config.columns/2)+2:
                del bullet
                global_var.bullet_present = False
                global_var.dragon_lives -= 1
                global_var.score += 10
                if global_var.dragon_lives <= 0:
                    global_funct.display_ending("YOU WON!")
                    break
            else:
                bullet.move_right()      
                
        global_funct.draw_dragon_lives_bar()
        global_funct.reset_scenery()
