# SNAKE GAME with Machine Learning  🐍🍎

<p float="center">
    <img src  = "https://github.com/kiana-jahanshid/Snake-Game-ML/blob/main/assets/Capture6.JPG" width=400 /> 
    <img src  = "https://github.com/kiana-jahanshid/Snake-Game-ML/blob/main/assets/Capture5.JPG" width=400 /> 
</p>

# Description 
In this game we let our Neural Network play the game , without user interfere . but first we need to get help from  if-else rules to be able to train our model . 

# How to install 
```
pip install -r requirements.txt 
```


# How to run 

+ ## step1 : generate dataset 
For generating dataset , we should play game and collect some features during game . 
first you have to run `Generate_dataset.py` , then a csv file will generated  , or else use this command :
```
python Generate_dataset.py
```
when you want to quit the game , press `Q` key on keyboard to exit the game .
Now , our dataset has been created and ready to use in the next part . 

+ ## step2 :  Start training 
Next step  , we use our dataset to train our Neural Network .
Hence , Run file `train.py` to start training . or else run this command :
```
python train.py
```
At the end , you can see the Accuracy & Loss results .

+ ## step3 : play game using MLP
In first step we played game using (if , else , ...) rules .
Now it's time to play game using Multi-Layer Perceptron (MLP) , which is a Fully-Connected Artificial Neural Network . 
For this , run `main_ML_snake.py` file or run below command :
```
python main_ML_snake.py
```

# RESULTS 
Here is our loss and accuracy resuls :

<p float="center">
    <img src  = "https://github.com/kiana-jahanshid/Snake-Game-ML/blob/main/assets/ACCLOSS1.JPG" width=500 /> 
</p>

<p float="center">
    <img src  = "https://github.com/kiana-jahanshid/Snake-Game-ML/blob/main/assets/ACCLOSS.JPG" width=500 /> 
</p>

