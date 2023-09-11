import math
import arcade
import numpy as np
import tensorflow as tf 
from snake import Snake
from apple import Apple
from pear import Pear 
from onion import Onion

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
        self.model = tf.keras.models.load_model("weights\AIsnake_model.h5")
        self.a = 0 
        self.b = 0 
        self.c = 0
        self.d = 0
        self.snake.change_x = 0 
        self.snake.change_y = 0

    def on_draw(self):
        arcade.start_render()
        self.snake.mydraw()
        self.apple.draw()
        self.pear.draw()
        self.onion.draw()
        arcade.draw_text(f"Score : {self.snake.score}", 370, 15, arcade.color.WHITE, font_size= 17 ,font_name= 'arial', bold=True)
        if self.flag == 0 :
            arcade.draw_text("Game Over", 15 , 210  , arcade.color.RED , 65 ,  bold=True)
            arcade.close_window()
            exit(0)

    def on_key_press(self , symbol : int , modifiers : int):
        pass

    def on_update(self, delta_time : float) :

        data = {}
        x_difference_as =float(self.snake.center_x - self.apple.center_x )
        y_difference_as =float(self.snake.center_y - self.apple.center_y )
        x_difference_ps =float(self.snake.center_x - self.pear.center_x )
        y_difference_ps =float(self.snake.center_y - self.pear.center_y    ) 
        
        snake_apple_dist = math.hypot(x_difference_as, y_difference_as) # mohasebe fasele oghlidosi beine mar va do ta mive , va entekhabe mive nazdik tar
        snake_pear_dist = math.hypot(x_difference_ps , y_difference_ps)
        
        if snake_apple_dist < snake_pear_dist:
            snake_choice = self.apple
            snake_choice_binary = 0
        else : 
            snake_choice = self.pear
            snake_choice_binary = 1


        for part in self.snake.body : 
            if self.snake.center_x == part["x"]  and  self.snake.center_y < part["y"]:
                self.a  = part["y"]-self.snake.center_y
            if self.snake.center_x == part["x"]  and  self.snake.center_y > part["y"]:
                self.b = part["y"]-self.snake.center_y
            if self.snake.center_x < part["x"]  and  self.snake.center_y == part["y"]:
                self.c = part["x"]-self.snake.center_x 
            if self.snake.center_x > part["x"]  and  self.snake.center_y == part["y"]:
                self.d = part["x"]-self.snake.center_x

        data = np.array([[self.snake.center_x , self.snake.center_y , self.snake.change_x , self.snake.change_y  , snake_choice_binary , snake_choice.center_x , snake_choice.center_y , self.a , self.b , self.c ,  self.d ]])
        print(data)
        output = self.model.predict([data])
        direction = output.argmax()
        print("direction" , direction)

        if direction == 0 and self.snake.change_y != -1: # snake goes up 
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif direction == 1 and self.snake.change_x != -1:  # snake goes right
            self.snake.change_x = 1
            self.snake.change_y = 0

        elif direction == 2 and self.snake.change_y != 1:  # snake goes down 
            self.snake.change_x = 0
            self.snake.change_y = -1

        elif direction == 3 and self.snake.change_x != 1:  # snake goes left
            self.snake.change_x = -1
            self.snake.change_y = 0

        if self.snake.center_x == (self.width - 5) :
            self.snake.change_x = -1
        elif self.snake.center_x <= 5 :
            self.snake.change_x = 1
        if self.snake.center_y == (self.height - 5) :
            self.snake.change_y = -1
        elif self.snake.center_y <= 5 :
            self.snake.change_y = 1


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

        # GAMEOVER IN CASE OF GAME BORDER COLLISION
        if self.snake.center_x <-5 or self.snake.center_y < -5 or self.snake.center_x >self.width+5  or self.snake.center_y > self.height+5:
            self.flag = 0

        # GAMEOVER IN CASE OF NEGATIVE SCORE 
        if self.snake.score == 0 and len(self.snake.body)>0 : 
            self.flag = 0        


if __name__ == "__main__" :
    window = Game()
    arcade.run()