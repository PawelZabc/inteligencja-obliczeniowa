import math
import random
import matplotlib.pyplot as plt
import numpy as np

class Vector():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def __repr__(self):
        return f"x:{self.x}, y:{self.y}"

    def times(self, number):
        return Vector(self.x * number, self.y * number)

    def array(self):
        return [self.x, self.y]


def starting_velocity(alpha, v0):
    x = math.sin(alpha) * v0
    y = math.cos(alpha) * v0
    return Vector(x, y)


def shoot(angle, goal, v0=50, y0=100, x0=0, gravity=Vector(0, -9.8)):
    velocity = starting_velocity(math.radians(angle), v0)
    position = Vector(x0, y0)

    x_pos = []
    y_pos = []

    def step(seconds=0.01):
        # Aktualizacja prędkości i pozycji
        velocity.add(gravity.times(seconds))
        position.add(velocity.times(seconds))

    while position.y >= 0:
        x_pos.append(position.x)
        y_pos.append(position.y)
        step()

    # Rysowanie wykresu
    if abs(position.x - goal) <= 5:
        plt.axline((position.x, 0), (position.x, 1), linewidth=1, color='r', ls="--")
        plt.axline((goal, 0), (goal, 1), linewidth=1, color='black', ls="--")
        plt.plot(x_pos, y_pos)
        plt.axline((0, 0), (1, 0), linewidth=2, color='black')
        plt.grid()
        plt.title("Trajectory")
        plt.xlabel("Distance (m)")
        plt.ylabel("Height (m)")
        plt.savefig("trajektoria.png")
        plt.show()

        print(f"Uderzyłeś na odległość {position.x}")
        print("Udało ci się!")
        return True
    return False


def main():
    goal = random.randint(50, 340)
    print(f"Twój cel to {goal} m")

    num_of_shots = 0
    while True:
        num_of_shots += 1
        try:
            angle = float(input("Wpisz kąt (w stopniach): "))
            if not (0 <= angle <= 90):  # Kąt w zakresie 0-90 stopni
                print("Kąt musi być w zakresie 0-90 stopni.")
                continue
        except ValueError:
            print("Podaj poprawną liczbę.")
            continue

        end = shoot(angle, goal)
        if end:
            print(f"Ilość strzałów: {num_of_shots}")
            break
        else:
            print("Pudło :[")


if __name__ == "__main__":
    main()
