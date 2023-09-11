import tensorflow as tf 
import pandas as pd 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


df  = pd.read_csv("dataset\dataset.csv")
df = df.fillna(0)
df = df.astype(int)

X = df[["snake_centx" , "snake_centy" , "snake_change_x" , "snake_change_y"  , "snake_choice" , "snake_choice_cx" , "snake_choice_cy" , "body1" , "body2" , "body3" ,  "body4" ]].values 
Y = df[["direction"]].values 
print(X.shape)
print(Y.shape)

X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size=0.1 )
Y_train = Y_train.reshape(-1,1)
Y_test  = Y_test.reshape(-1,1)
print(X_train.shape , X_test.shape , Y_train.shape , Y_test.shape)


model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(11 ),
        tf.keras.layers.Dense(300 , activation="relu"),
        tf.keras.layers.Dense(200 , activation="relu"),
        tf.keras.layers.Dense(300 , activation="relu"),
        tf.keras.layers.Dense(4  , activation="softmax")])

model.compile(optimizer= tf.keras.optimizers.Adamax() ,loss= tf.keras.losses.sparse_categorical_crossentropy , metrics=["accuracy"] )
output = model.fit(X_train , Y_train , epochs=200)
loss , acc =  model.evaluate(X_test , Y_test)
model.save("weights\AIsnake_model.h5")

print("TEST loss:" , loss)
print("TEST accuracy:" ,acc)    
plt.plot(output.history["loss"], label='loss')
plt.plot(output.history["accuracy"], label='accuracy')
plt.title("loss and accuracy for train")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()