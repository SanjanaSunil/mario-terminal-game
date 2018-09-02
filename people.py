import config
import global_var
import global_funct
import random
import os
from colorama import init, Fore, Back, Style

class Person(object):

    """ Characters of the game """

    def __init__(self, character, x, y):
        self.width = len(character[0])
        self.height = len(character)
        self.posx = x
        self.posy = y


    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                global_var.scenery.scene_matrix[j+self.posy][i+self.posx] = "\033[31m" + "\033[46m" + "\033[1m" + config.mario[j][i]


    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                global_var.scenery.scene_matrix[j+self.posy][i+self.posx] = "\033[31m" + "\033[46m" + " "


    def die(self):
        os.system('aplay mariodies.wav&')
        global_var.lives -= 1
        self.clear()
        self.posy = 5

    def move_left(self):
        for i in range(self.height):
            if global_var.scenery.scene_matrix[self.posy+i][self.posx-1] == "\033[33m" + "\033[45m" + " ":
                return
        self.clear()
        self.posx -= 1
        self.render()

    
    def check_left(self):
        for i in range(self.height-1):
            if global_var.scenery.scene_matrix[self.posy+i][self.posx-1] == "\033[31m" + "\033[40m" + "l":
                self.die()
                return
            elif global_var.scenery.scene_matrix[self.posy+i][self.posx-1] == "\033[31m" + "\033[40m" + "r":
                self.die()
                return
            elif global_var.scenery.scene_matrix[self.posy+i][self.posx-1] == "\033[31m" + "\033[40m" + "k":
                self.die()      
                return
            if global_var.scenery.scene_matrix[self.posy+i][self.posx-1] == "\033[33m" + "\033[46m" + "\033[1m" + "$":
                global_var.score += 1
            if global_var.scenery.scene_matrix[self.posy+i][self.posx-1] == "\033[31m" + "\033[47m" + "\033[1m" + "+":
                if global_var.lives < 5: 
                    global_var.lives += 1
        if self.posx == global_var.scenery.scene_start_index:
            return
        self.move_left()


    def move_right(self):
        for i in range(self.height):
            if global_var.scenery.scene_matrix[self.posy+i][self.posx+self.width] == "\033[33m" + "\033[45m" + " ":
                return
        self.clear()
        self.posx += 1
        self.render()

    def check_right(self):
        for i in range(self.height-1):
            if global_var.scenery.scene_matrix[self.posy+i][self.posx+self.width] == "\033[31m" + "\033[40m" + "a":
                self.die()
                return
            elif global_var.scenery.scene_matrix[self.posy+i][self.posx+self.width] == "\033[31m" + "\033[40m" + "k":
                self.die()
                return
        for i in range(self.height):
            if global_var.scenery.scene_matrix[self.posy+i][self.posx+self.width] == "\033[33m" + "\033[45m" + " ":
                return
            if global_var.scenery.scene_matrix[self.posy+i][self.posx+self.width] == "\033[33m" + "\033[46m" + "\033[1m" + "$":
                global_var.score += 1
            if global_var.scenery.scene_matrix[self.posy+i][self.posx+self.width] == "\033[31m" + "\033[47m" + "\033[1m" + "+":
                if global_var.lives < 5:
                    global_var.lives += 1
        if self.posx + self.width >= global_var.scenery.scene_length - int(config.columns/2) - 2:
            return
        if (self.posx - global_var.scenery.scene_start_index) >= int(config.columns/2):
            self.clear()
            global_var.scenery.scene_start_index += 1
            self.posx += 1
            self.render()
            return
        self.move_right()

        
    def gravity(self):
        for i in range(self.width):
            if global_var.scenery.scene_matrix[self.posy+self.height][self.posx+i] == "\033[33m" + "\033[45m" + " ":
                return
            if global_var.scenery.scene_matrix[self.posy+self.height][self.posx+i] == "\033[33m" + "\033[46m" + "\033[1m" + "$":
                global_var.score += 1
            if global_var.scenery.scene_matrix[self.posy+self.height][self.posx+i] == "\033[31m" + "\033[47m" + "\033[1m" + "+":
                if global_var.lives < 5:
                    global_var.lives += 1
            if global_var.scenery.scene_matrix[self.posy+self.height][self.posx+i] == "\033[31m" + "\033[40m" + " ":
                self.die()
                return
        if self.posy == global_var.scenery.ground_level - self.height:
            return
        self.clear()
        self.posy += 1
        self.render()


    def jump(self):
        y = self.posy
        while self.posy > y - 2*len(config.platform) - 2 and self.posy > 4:
            flag = 1
            for i in range(self.width):
                if global_var.scenery.scene_matrix[self.posy-1][self.posx+i] == "\033[33m" + "\033[45m" + " ":
                    flag = 0
                    break
                if global_var.scenery.scene_matrix[self.posy-1][self.posx+i] == "\033[33m" + "\033[46m" + "\033[1m" + "$":
                    global_var.score += 1
                if global_var.scenery.scene_matrix[self.posy+i][self.posx-1] == "\033[31m" + "\033[47m" + "\033[1m" + "+":
                    if global_var.lives < 5:
                        global_var.lives += 1
            if not flag:
                break
            self.clear()
            self.posy -= 1
            self.render()
            global_funct.check_input(self)
            if global_var.quit_flag:
                return
        while self.posy != y:
            y = self.posy
            self.gravity()
            global_funct.check_input(self)
            if global_var.quit_flag:
                break


class Enemy(Person):

    def __init__(self, x, y):
        Person.__init__(self, config.enemy, x, y)

    def __del__(self):
        self.clear()
        
    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if config.enemy[j][i] != " ":
                    global_var.scenery.scene_matrix[j+self.posy][i+self.posx] = "\033[31m" + "\033[40m" + config.enemy[j][i]

    
    def check_left(self, index, mario):
        if self.posx <= 3:
            global_var.enemy_dir[index] = 'right'
            return
        for i in range(self.height):
            if global_var.scenery.scene_matrix[self.posy+i][self.posx-1] == "\033[33m" + "\033[45m" + " ":
                global_var.enemy_dir[index] = 'right'
        self.move_left()
        

    def check_right(self, index, mario):
        if self.posx+self.width == global_var.scenery.scene_length - int(config.columns/2) - 4:
            global_var.enemy_dir[index] = 'left'
            return
        if self.posx+self.width >= global_var.scenery.scene_length-2:
            global_var.enemy_dir[index] = 'left'
            return
        for i in range(self.height):
            if global_var.scenery.scene_matrix[self.posy+i][self.posx+self.width] == "\033[33m" + "\033[45m" + " ":
                global_var.enemy_dir[index] = 'left'
        self.move_right()

    def gravity(self):
        for i in range(self.width):
            if global_var.scenery.scene_matrix[self.posy+self.height][self.posx+i] == "\033[33m" + "\033[45m" + " ":
                return
        if self.posy == global_var.scenery.ground_level - self.height:
            return
        self.clear()
        self.posy += 1
        self.render()
