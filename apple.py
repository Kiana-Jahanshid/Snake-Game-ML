import arcade 
from fruit import Fruit

class Apple(Fruit):
    def __init__(self ,  game):
        super().__init__(game ,"assets/apple.png")