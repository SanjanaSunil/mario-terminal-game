import config
import random
from colorama import init, Fore, Back, Style


class Scene(object):

    """ Scenes and levels """

    scene_height = int(config.rows)
    scene_length = int(config.columns*10)
    ground_level = int(config.rows/1.3)

    def __init__(self):
        self.scene_start_index = 0
        self.scene_matrix = [[" " for x in range(Scene.scene_length)] for y in range(Scene.scene_height)]
        self.create_sky()
        self.create_clouds()
        self.create_coins()
        self.create_powerup()
        self.create_ground()
        self.create_holes()
        self.draw_dragon()
        self.create_layer1_platforms()
        self.create_layer2_platforms()


    def render(self):
        for y in range(3, Scene.scene_height):
            pr = []
            for x in range(self.scene_start_index, self.scene_start_index+config.columns):
                pr.append(self.scene_matrix[y][x]+Style.RESET_ALL)
                # print(self.scene_matrix[y][x] + Style.RESET_ALL, end='')
            print(''.join(pr))


    def create_ground(self):
        for y in range(Scene.ground_level, Scene.scene_height):
            for x in range(500):
                self.scene_matrix[y][x] = "\033[37m" + "\033[42m" + " "
        for y in range(Scene.ground_level, Scene.scene_height):
            for x in range(500, Scene.scene_length):
                self.scene_matrix[y][x] = "\033[37m" + "\033[44m" + "-"
        for y in range(Scene.ground_level, Scene.scene_height):
            for x in range(Scene.scene_length-int(config.columns/2), Scene.scene_length):
                self.scene_matrix[y][x] = "\033[37m" + "\033[40m" + " "

    
    def create_holes(self):
        x = 1
        while x < (500 - config.columns*2):
            offset = random.randint(config.columns, config.columns*2)
            x += offset
            for i in range(Scene.ground_level, Scene.ground_level+3):
                for j in range(10):
                    self.scene_matrix[i][x+j] = "\033[31m" + "\033[40m" + " "
            for i in range(Scene.ground_level+3, Scene.ground_level+5):
                for j in range(10):
                    self.scene_matrix[i][x+j] = "\033[37m" + "\033[41m" + "~"


    def create_sky(self): 
        for y in range(1, Scene.ground_level):
            for x in range(Scene.scene_length):
                self.scene_matrix[y][x] = "\033[37m" + "\033[46m" + " "
        for y in range(1, Scene.ground_level):
            for x in range(Scene.scene_length-int(config.columns/2), Scene.scene_length):
                self.scene_matrix[y][x] = "\033[37m" + "\033[40m" + " "


    def create_clouds(self):
        x = 1
        while x < (Scene.scene_length-2*int(config.columns/2)):
            offset = random.randint(3, int(config.columns/2.5))
            x += offset
            y = random.randint(3, int(Scene.scene_height/3)-3)
            for i in range(len(config.cloud)):
                for j in range(len(config.cloud[0])):
                    self.scene_matrix[y+i][x+j] = "\033[37m" + "\033[46m" + config.cloud[i][j]


    def create_coins(self):
        x = 1
        while x < (Scene.scene_length-2*config.columns):
            offset = random.randint(5, int(config.columns/2.5))
            x += offset
            y = random.randint(int(Scene.scene_height/3)-3, self.ground_level)
            for i in range(len(config.coin)):
                for j in range(len(config.coin[0])):
                    self.scene_matrix[y+i][x+j] = "\033[33m" + "\033[46m" + "\033[1m" + config.coin[i][j]


    def create_powerup(self):
        x = 1
        while x < (Scene.scene_length-(config.columns*3)):
            offset = random.randint(50, 60)
            x += offset
            y = random.randint(int(Scene.scene_height/3)-3, self.ground_level)
            for i in range(len(config.powerup)):
                for j in range(len(config.powerup[0])):
                    self.scene_matrix[y+i][x+j] = "\033[31m" + "\033[47m" + "\033[1m" + config.powerup[i][j]


    def draw_dragon(self):
        dragony = self.scene_height - len(config.dragon) - 5
        dragonx = Scene.scene_length-int(config.columns/2)
        for y in range(len(config.dragon)):
            for x in range(len(config.dragon[0])):
                self.scene_matrix[y+dragony][x+dragonx] = "\033[33m" + "\033[40m" + "\033[1m" + config.dragon[y][x]


    def create_layer1_platforms(self):
        x = int(config.columns*2/3)
        while x < (Scene.scene_length-int(1.5*config.columns)):
            offset = random.randint(0, int(config.columns/2))
            x += offset
            y = Scene.ground_level - len(config.platform)
            for i in range(len(config.platform)):
                for j in range(len(config.platform[0])):
                    self.scene_matrix[y+i][x+j] = "\033[33m" + "\033[45m" + config.platform[i][j]

    
    def create_layer2_platforms(self):
        x = int(config.columns*2/3)
        while x < (Scene.scene_length-2*config.columns):
            offset = random.randint(0, int(config.columns/2))
            x += offset 
            y = Scene.ground_level - 2*len(config.platform)
            for i in range(len(config.platform)):
                for j in range(len(config.platform[0])):
                    self.scene_matrix[y+i][x+j] = "\033[33m" + "\033[45m" + config.platform[i][j]
