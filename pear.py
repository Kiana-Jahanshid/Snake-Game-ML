import arcade  
from fruit import Fruit

class Pear(Fruit):
    def __init__(self , game):
        super().__init__(game , "assets\pear.png")