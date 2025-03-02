import math
import time


class Vector():
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    def add(self,vector):
        self.x += vector.x
        self.y += vector.y
    def set(self,x:None,y:None):
        if x!=None:
            self.x = x
        if y!=None:
            self.y = y
    def string(self):
        return f"x:{self.x},y:{self.y}"
    def times(self,number):
        return Vector(self.x * number,self.y * number)
        
        

y0 = 100
v0 = 50
x0 = 0
velocity = Vector()
gravity = Vector(0,-10)
position = Vector(0,100)

def step(seconds = 1):
    velocity.add(gravity.times(seconds))
    position.add(velocity.times(seconds))

def starting_velocity(alpha):
    x = math.sin(alpha)*v0
    y = math.cos(alpha)*v0
    return Vector(x,y)


velocity = starting_velocity(math.radians(45))
print(velocity.string())

while position.y >= 0:
    step(0.01)
    # step()
    # time.sleep(0.0)
    print("-"*80)
    print(position.string())
    print(velocity.string())
    x=math.floor(position.x/5)
    y=math.floor(position.y/10)
    print(x,y)
    for i in range(20,0,-1):
        string = "|"
        for j in range(80):
            if i == y and j == x:
                string+="0"
            else:
                string+=" "
        print(string)