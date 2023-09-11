import arcade
from snake import Snake
from apple import Apple
from pear import Pear 
from onion import Onion
import math
import pandas as pd 

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width= 500 , height=450 , title="Snake Game - MLP")
        arcade.set_background_color(arcade.color.GENERIC_VIRIDIAN)
        self.apple = Apple(self) 
        self.pear  = Pear(self)        
        self.snake = Snake(self)
        self.onion = Onion(self)
        self.flag = 1
        self.dataset = []
        self.body1 = 0
        self.body2 = 0 
        self.body3 = 0
        self.body4 = 0 

    def on_draw(self):
        arcade.start_render()
        self.snake.mydraw()
        self.apple.draw()
        self.pear.draw()
        self.onion.draw()
        arcade.draw_text(f"Score : {self.snake.score}", 370, 15, arcade.color.WHITE, font_size= 17 ,font_name= 'arial', bold=True)
        if self.flag == 0 :
            arcade.draw_text("Game Over", 20 , 210  , arcade.color.RED , 80 ,  bold=True)


    # press Q to save csv file and exit game 
    def on_key_press(self , symbol : int , modifiers : int):
        if symbol == arcade.key.Q :
            df = pd.DataFrame(self.dataset)
            df.to_csv("dataset\dataset.csv" , index=False)
            arcade.close_window()
            exit(0)

    
    def on_update(self, delta_time : float) :

        data = { "snake_centx" : None ,
                 "snake_centy" : None ,
                 "snake_change_x"  : None ,
                 "snake_change_y"  : None ,
                 "snake_choice"    : None ,
                 "snake_choice_cx" : None ,
                 "snake_choice_cy" : None ,
                 "body1" : None ,
                 "body2" : None ,
                 "body3" : None ,
                 "body4" : None ,
                 "direction" : None}

        x_difference_as =float(self.snake.center_x  - self.apple.center_x )
        y_difference_as =float(self.snake.center_y - self.apple.center_y )
        x_difference_ps =float(self.snake.center_x  - self.pear.center_x )
        y_difference_ps =float(self.snake.center_y - self.pear.center_y  ) 
        
        snake_apple_dist = math.hypot(x_difference_as, y_difference_as)
        snake_pear_dist = math.hypot(x_difference_ps , y_difference_ps)
        
        if snake_apple_dist < snake_pear_dist:
            snake_choice = self.apple
            snake_choice_binary = 0
        else : 
            snake_choice = self.pear
            snake_choice_binary = 1

        if  snake_choice.center_x > self.snake.center_x  and self.snake.change_x != -1 :
            self.snake.change_x = 1 
            self.snake.change_y = 0 
            data["direction"] = 1
        elif snake_choice.center_x < self.snake.center_x  and self.snake.change_x != 1 :
            self.snake.change_x =  -1
            self.snake.change_y =  0
            data["direction"] = 3
        elif snake_choice.center_y < self.snake.center_y  and self.snake.change_y != 1  : 
            self.snake.change_x = 0
            self.snake.change_y = -1
            data["direction"] = 2
        elif snake_choice.center_y > self.snake.center_y  and self.snake.change_y != -1  :
            self.snake.change_x = 0
            self.snake.change_y = 1
            data["direction"]  = 0
        if snake_choice.center_x == self.snake.center_x and snake_choice.center_y < self.snake.center_y :
            self.snake.change_x = 0
            self.snake.change_y = -1      
            data["direction"] = 2
        elif snake_choice.center_x == self.snake.center_x and snake_choice.center_y > self.snake.center_y :
            self.snake.change_x = 0
            self.snake.change_y = 1 
            data["direction"] = 0
        elif snake_choice.center_x < self.snake.center_x and snake_choice.center_y == self.snake.center_y :
            self.snake.change_x = -1
            self.snake.change_y = 0 
            data["direction"] = 3
        elif snake_choice.center_x > self.snake.center_x and snake_choice.center_y == self.snake.center_y :
            self.snake.change_x = 1
            self.snake.change_y = 0 
            data["direction"] = 1


        for part in self.snake.body : 
            if self.snake.center_x == part["x"]  and  self.snake.center_y < part["y"]:
                self.body1  = abs(part["y"]-self.snake.center_y)
            if self.snake.center_x == part["x"]  and  self.snake.center_y > part["y"]:
                self.body2 = abs(part["y"]-self.snake.center_y)
            if self.snake.center_x < part["x"]  and  self.snake.center_y == part["y"]:
                self.body3 = abs(part["x"]-self.snake.center_x) 
            if self.snake.center_x > part["x"]  and  self.snake.center_y == part["y"]:
                self.body4 = abs(part["x"]-self.snake.center_x) 

        data["snake_centx"]  =  self.snake.center_x
        data["snake_centy"]  =  self.snake.center_y
        data["snake_change_x"]  =  self.snake.change_x
        data["snake_change_y"]  =  self.snake.change_y
        data["snake_choice"]  =  snake_choice_binary
        data["snake_choice_cx"]  =  snake_choice.center_x
        data["snake_choice_cy"]  =  snake_choice.center_y 
        data["body1"]  =  self.body1
        data["body2"]  =  self.body2
        data["body3"]  =  self.body3
        data["body4"]  =  self.body4

        self.dataset.append(data)
        
        self.snake.move()
        if arcade.check_for_collision(self.snake , self.apple ):
            self.snake.eat_apple(self.apple)
            self.apple = Apple(self)

        if arcade.check_for_collision(self.snake , self.pear ):
            self.snake.eat_pear(self.pear)
            self.pear = Pear(self)

        if arcade.check_for_collision(self.snake , self.onion ):
            self.snake.eat_onion(self.onion)
            self.onion = Onion(self)

        if self.snake.center_x <-10 or self.snake.center_y < -10 or self.snake.center_x >self.width+10  or self.snake.center_y > self.height+10:
            self.flag = 0

        if self.snake.score == 0 and len(self.snake.body)>0 : 
            self.flag = 0        


if __name__ == "__main__" :
    window = Game()
    arcade.run()