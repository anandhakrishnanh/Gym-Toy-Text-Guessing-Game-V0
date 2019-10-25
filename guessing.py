#IIITMK AI course Gym Toy Text Guesing Game V0 Solution

#FIrst we import gym and numpy to store our value
import gym
import numpy as np

total_episodes=200

#initialize the environment
env=gym.make("GuessingGame-v0")
env.reset()

#set the initial parameters
a=1000
b=-1000

for episodes in range(total_episodes):
    print("Episode:",episodes)

    #Choosing the value between the ranges
    guess=((a+b)/2)


    observation, reward, done, info = env.step(np.array([guess]))

    #Chaing parameters depending on if the guess is higher or lower
    if(observation==1):
        print(guess," is lower than the target")
        b=guess
    if(observation==2):
        print("Correct Value reached:",guess)
        break
    if(observation==3):
        print(guess," is higher than the target")
        a=guess

env.close()

#Anandha Krishnan H MI
