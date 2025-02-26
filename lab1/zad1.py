import math
import datetime



month_days = [
    31,28,31,30,31,30,31,31,30,31,30,31
]
# print(today.year)


def get_wave(t,cycle):
    return math.sin((2*math.pi/cycle)*t)
def count_days(year,month,day):
    today = datetime.datetime.now()
    days = 0


    # months = today.month-int(month)
    years = (today.year-int(year))
    for i in range(years+1):
        current_year = today.year-i
        if i==0:
            for j in range(today.month-1):
                if j == 2 and (current_year)%4 == 0:
                    days+=29
                else:
                    days+=month_days[j]
            days += today.day
            print(f"now:{current_year}")
        elif i == years:
            days += month_days[month]-day
            for j in range(month,12,1):
                if j == 2 and (current_year)%4 == 0:
                    days+=29
                else:
                    days+=month_days[j]
            print(f"first:{current_year}")
        else:
            if (current_year)%4 == 0:
                days+= 366
            else:
                days+=365
            print(f"between:{current_year}")
    print(today.year-int(year)-1)
    print(today.month-int(month))
    print(today.day-int(day))
    return days

# print("Enter your name:")
# name = input()
# print("Enter your year of birth:")
# year = input()
# print("Enter your month of birth:")
# month = input()
# print("Enter your day of birth:")
# day = input()

name= "Paweł"
year = 2005
month= 3
day = 29

t = count_days(year,month,day)
# t= 7194
print(f"Hello {name} you have been alive for {t} days!")
print(f"Fizyczna fala {get_wave(t,23)}")
print(f"Intelektualna fala {get_wave(t,28)}")
print(f"Emocjonalna fala {get_wave(t,33)}")