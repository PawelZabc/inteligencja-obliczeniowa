import math
import datetime





def get_wave(t,cycle):
    return math.sin((2*math.pi/cycle)*t)

print("Enter your name:")
name = input()
print("Enter your year of birth:")
year = int(input())
print("Enter your month of birth:")
month = int(input())
print("Enter your day of birth:")
day = int(input())

t=(datetime.datetime.now().date() - datetime.date(year,month,day)).days

print(f"Hello {name} you have been alive for {t} days!")
print(f"Fizyczna fala {get_wave(t,23)}")
print(f"Intelektualna fala {get_wave(t,28)}")
print(f"Emocjonalna fala {get_wave(t,33)}")