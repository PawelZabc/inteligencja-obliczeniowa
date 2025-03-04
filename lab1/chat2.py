import math
import random
import matplotlib.pyplot as plt

# Stałe
v0 = 50  # Prędkość początkowa w m/s
h = 100  # Wysokość początkowa w metrach
g = 9.81  # Przyspieszenie ziemskie w m/s^2

# Funkcja do obliczania zasięgu
def oblicz_zasieg(v0, h, alpha):
    alpha_rad = math.radians(alpha)  # Zamiana kąta na radiany
    v_x0 = v0 * math.cos(alpha_rad)
    v_y0 = v0 * math.sin(alpha_rad)
    
    # Obliczanie czasu lotu
    t = (v_y0 + math.sqrt(v_y0**2 + 2*g*h)) / g
    
    # Obliczanie zasięgu
    d = v_x0 * t
    return d

# Funkcja do rysowania trajektorii
def narysuj_trajektorie(v0, h, alpha):
    t_max = 2 * v0 * math.sin(math.radians(alpha)) / g + math.sqrt(2 * h / g)
    t = [i * t_max / 100 for i in range(101)]
    
    x = [v0 * math.cos(math.radians(alpha)) * ti for ti in t]
    y = [h + v0 * math.sin(math.radians(alpha)) * ti - 0.5 * g * ti**2 for ti in t]
    
    plt.plot(x, y)
    plt.title('Trajektoria lotu pocisku')
    plt.xlabel('Odległość (m)')
    plt.ylabel('Wysokość (m)')
    plt.grid(True)
    plt.savefig("trajektoria-chat.png")
    plt.show()

# Funkcja główna
def strzelaj():
    # Losowanie celu w zakresie [50, 340]
    cel = random.randint(50, 340)
    print(f"Celem jest odległość: {cel} metrów.")
    
    # Liczba prób
    liczba_prob = 0
    
    while True:
        # Wczytanie kąta od użytkownika
        alpha = float(input("Podaj kąt strzału (w stopniach): "))
        
        # Obliczanie zasięgu
        zasieg = oblicz_zasieg(v0, h, alpha)
        print(f"Twój pocisk doleci na odległość: {zasieg:.2f} metrów.")
        
        # Sprawdzanie, czy pocisk trafił w cel
        if abs(cel - zasieg) <= 5:
            liczba_prob += 1
            print(f"Cel trafiony! Liczba prób: {liczba_prob}")
            # Rysowanie trajektorii
            narysuj_trajektorie(v0, h, alpha)
            break
        else:
            liczba_prob += 1
            print(f"Chybiono! Spróbuj ponownie.")
            
# Uruchomienie gry
strzelaj()
