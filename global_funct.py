import config
import random
import os
import people
import global_var
from colorama import Fore, Back, Style

# Display score and lives at the bottom
def create_footer():
    print("\033[" + str(config.rows) + ";1H" + Fore.WHITE + Back.RED + Style.BRIGHT + ("SCORE: " + str(global_var.score) + "   |  LIVES: " + str(global_var.lives)).center(config.columns), end='')
    print(Style.RESET_ALL)


# Redraw scenery
def reset_scenery():
    config.create_banner()
    global_var.scenery.render()
    create_footer()


# Display final results
def display_ending(message):
    os.system('tput reset')
    print(Fore.CYAN + Style.BRIGHT + "FINAL STANDINGS:".center(config.columns))
    print(Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + ("SCORE: " + str(global_var.score)).center(config.columns))
    print(Fore.CYAN + Style.BRIGHT + ("LIVES: " + str(global_var.lives)).center(config.columns))
    print(Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + (message).center(config.columns))
    print(Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + ("GOODBYE " + global_var.username + "!").center(config.columns))
    print(Style.RESET_ALL)
    global_var.quit_flag = 1
    return


# Draw lives of dragon
def draw_dragon_lives_bar():
    
    startx = global_var.scenery.scene_length - int(config.columns/4) - 6 - 5
    starty = global_var.scenery.scene_height - len(config.dragon) - 8

    instruction = list("Press the spacebar to shoot")
    for i in range(len(instruction)):
        global_var.scenery.scene_matrix[starty-3][startx-8+i] = "\033[37m" + "\033[40m" + "\033[1m" + instruction[i]
    
    global_var.scenery.scene_matrix[starty][startx] = "\033[37m" + "\033[40m" + "\033[1m" + "["
    global_var.scenery.scene_matrix[starty][startx+11] = "\033[37m" + "\033[40m" + "\033[1m" + "]"
    
    for i in range(1, global_var.dragon_lives+1):
        global_var.scenery.scene_matrix[starty][startx+i] = "\033[32m" + "\033[42m" + " "
    for i in range(global_var.dragon_lives+1, 11):
        global_var.scenery.scene_matrix[starty][startx+i] = "\033[32m" + "\033[40m" + " "


# Generate enemies
def generate_enemies():
    x = int(config.columns*2/3)
    while x < (global_var.scenery.scene_length-2*config.columns):
        if x >= 500:
            offset = random.randint(10, 40)
        else:
            offset = random.randint(10, config.columns-5)
        global_var.enemy_list.append(people.Enemy(x+offset, 1))
        direction = random.randint(0, 1)
        if direction:
            global_var.enemy_dir.append('right')
        else:
            global_var.enemy_dir.append('left')
        x += offset 
        global_var.enemy_list[-1].render()
    for j in range(config.rows):
        for i in range(len(global_var.enemy_list)):
            global_var.enemy_list[i].gravity()


# Check collisioin in the background
def run_background(character):

    for i in range(character.height-1):
        if global_var.scenery.scene_matrix[character.posy+i][character.posx+character.width] == "\033[31m" + "\033[40m" + "a":
            character.die()
        elif global_var.scenery.scene_matrix[character.posy+i][character.posx+character.width] == "\033[31m" + "\033[40m" + "k":
            character.die()

    for i in range(character.height-1):
        if global_var.scenery.scene_matrix[character.posy+i][character.posx-1] == "\033[31m" + "\033[40m" + "l":
            character.die()
        elif global_var.scenery.scene_matrix[character.posy+i][character.posx-1] == "\033[31m" + "\033[40m" + "r":
            character.die()
        elif global_var.scenery.scene_matrix[character.posy+i][character.posx-1] == "\033[31m" + "\033[40m" + "k":
            character.die()


# Move and check collision wih enemies
def check_enemies(character):

    for i in range(len(global_var.enemy_list)):
        flag = 0
        for j in range(global_var.enemy_list[i].width):
            y = global_var.enemy_list[i].posy
            x = global_var.enemy_list[i].posx
            if y - character.posy == character.height and abs(x-character.posx) <= character.width:
                del global_var.enemy_list[i]
                del global_var.enemy_dir[i]
                global_var.score += 10
                flag = 1
                break
        if flag:
            break
        if global_var.enemy_dir[i] == 'right':
            global_var.enemy_list[i].check_right(i, character)
        else:
            global_var.enemy_list[i].check_left(i, character)

    for i in range(len(global_var.enemy_list)):
        global_var.enemy_list[i].gravity()


# Check input while jumping
def check_input(character):

    if global_var.lives <= 0:
        global_var.quit_flag = 1  
        return

    run_background(character)
    check_enemies(character)

    event = config.get_key(config.get_input())
    if event == config.LEFT:
        character.check_left()
    elif event == config.RIGHT:
        character.check_right()
    elif event == config.QUIT:
        global_var.quit_flag = 1  
        return

    reset_scenery()