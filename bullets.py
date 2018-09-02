import people
import config
import global_var


class Bullet(people.Person):

    """ BUllets that Mario fires """

    def __init__(self, x, y):
        people.Person.__init__(self, config.bullet, x, y)

    def __del__(self):
        self.clear()

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                global_var.scenery.scene_matrix[j+self.posy][i+self.posx] = "\033[32m" + "\033[40m" + "\033[1m" + config.bullet[j][i]

    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.posx <= global_var.scenery.scene_length-int(config.columns/2) - 1:
                    global_var.scenery.scene_matrix[j+self.posy][i+self.posx] = "\033[31m" + "\033[46m" + " "
                else:
                    global_var.scenery.scene_matrix[j+self.posy][i+self.posx] = "\033[31m" + "\033[40m" + " "
