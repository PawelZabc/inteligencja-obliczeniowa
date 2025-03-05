import math
import datetime



wave_length = {
    "fizyczna":23,
    "intelektualna":28,
    "emocjonalna":33}


def get_wave(t,cycle):
    return math.sin((2*math.pi/cycle)*t)

def wave_message(type,t):
    value = get_wave(t,wave_length[type])
    print(f"Twoja fala {type} wynosi {value}")
    if value <= -0.5:
        print("Wygląda na to że masz pod tym względem słaby dzień, dasz radę c:")
        if value > get_wave(t+1,wave_length[type]):
            print("I patrz pozytywnie! Jutro będzie lepiej :D")
    if value >= 0.5:
        print("Wygląda na to że masz dobry dzień pod tym względem :]")
    


print("Enter your name:")
name = input()
print("Enter your year of birth:")
year = int(input())
print("Enter your month of birth:")
month = int(input())
print("Enter your day of birth:")
day = int(input())

t=(datetime.datetime.now().date() - datetime.date(year,month,day)).days

print(f"Cześć {name}! Żyjesz już {t} dni!")

wave_message("fizyczna",t)
wave_message("intelektualna",t)
wave_message("emocjonalna",t)