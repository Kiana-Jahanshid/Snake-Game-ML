import random 
import arcade 

class Fruit(arcade.Sprite):
    def __init__(self , game , fr):
        super().__init__(fr)
        self.width = 30
        self.height = 30
        self.center_x = random.randint(10 , game.width-10)
        self.center_y = random.randint(10 , game.height-10)
        self.change_x = 0 
        self.change_y = 0