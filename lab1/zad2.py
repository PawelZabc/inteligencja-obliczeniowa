import math
import random

import matplotlib.pyplot as plt
import numpy as np



class Vector():
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    def add(self,vector):
        self.x += vector.x
        self.y += vector.y
    def __repr__(self):
        return f"x:{self.x},y:{self.y}"
    def times(self,number):
        return Vector(self.x * number,self.y * number)
    def array(self):
        return [self.x,self.y]

def starting_velocity(alpha):
        x = math.sin(alpha)*v0
        y = math.cos(alpha)*v0
        return Vector(x,y)  

y0=100
v0=50
x0=0
gravity = Vector(0,-9.8) 

    
def shoot(angle,goal):
    velocity = starting_velocity(math.radians(angle))
    position = Vector(x0,y0)
    def step(seconds = 1):
        velocity.add(gravity.times(seconds))
        position.add(velocity.times(seconds))
    x_pos = []
    y_pos = []
    while position.y >= 0:
        x_pos.append(position.x)
        y_pos.append(position.y)
        step(0.01)
    
    plt.axline((position.x, 0), (position.x, 1), linewidth=1, color='r', ls="--")
    plt.axline((goal, 0), (goal, 1), linewidth=1, color='black', ls="--")
    xpoints = np.array(x_pos)
    ypoints = np.array(y_pos)
    plt.plot(xpoints,ypoints)
    plt.axline((0,0), (1, 0), linewidth=2, color='black')
    plt.grid()
    plt.show()

    return position





goal = random.randint(0,350)
print(f"Twój cel to {goal}")
num_of_shots = 0
while (True):
    num_of_shots+=1
    print("Wpisz kąt:")
    angle = int(input())
    end = shoot(angle,goal)
    print(f"Uderzyłeś na odległość {end.x}")
    if abs(end.x-goal)<=10:
        print("Udało ci się!")
        break
    else:
        print("Pudło :[")



