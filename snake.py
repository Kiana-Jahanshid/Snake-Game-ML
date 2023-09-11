import random 
import arcade


class Snake(arcade.Sprite):
    def __init__(self , game):
        super().__init__()
        self.width = 30
        self.height = 30
        self.center_x = game.width //  2  #makan mar
        self.center_y = game.height // 2
        self.color  = arcade.color.GUPPIE_GREEN
        self.change_x = 0 
        self.change_y = 0 
        self.speed = 5
        self.score= 0 
        self.body = []
        self.radius = 10

    def move(self):
        self.body.append({"x" : self.center_x , "y" : self.center_y})
        if len(self.body) > self.score :
            self.body.pop(0)
        self.center_x += self.change_x * self.speed 
        self.center_y += self.change_y * self.speed 



    def mydraw(self) :
        arcade.draw_circle_filled(self.center_x  , self.center_y , radius= self.radius , color= self.color)
        i = 0 
        for part in self.body :
            if i % 2 == 0 :
                arcade.draw_circle_filled(part["x"] , part["y"] , radius= self.radius  , color= self.color)
            else :
                arcade.draw_circle_filled(part["x"] , part["y"] , radius= self.radius  , color= arcade.color.DARK_BLUE)
            i += 1

    def eat_apple(self , apple):
        del apple
        self.score += 1
        print("score :",self.score)

    def eat_pear(self , pear):
        del pear
        self.score += 2
        print("score :",self.score)

    def eat_onion(self , onion):
        del onion
        self.score -= 1
        if self.score < 0 :
            print("score :",self.score)
            arcade.draw_text("Game Over", 20 , 210  , arcade.color.RED , 80 ,  bold=True)
            arcade.close_window()
            exit(0)
        print("score :",self.score)