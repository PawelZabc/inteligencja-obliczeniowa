import math
import datetime


# Definiowanie długości cykli fal dla różnych typów
wave_lengths = {
    "fizyczna": 23,
    "intelektualna": 28,
    "emocjonalna": 33
}

# Funkcja obliczająca wartość fali w danym czasie
def calculate_wave(t, cycle_length):
    return math.sin((2 * math.pi / cycle_length) * t)

# Funkcja wyświetlająca komunikaty w zależności od wartości fali
def display_wave_message(wave_type, t):
    wave_value = calculate_wave(t, wave_lengths[wave_type])
    print(f"Twoja fala {wave_type} wynosi {wave_value:.2f}")
    
    # Sprawdzanie stanu fali i wyświetlanie odpowiednich komunikatów
    if wave_value <= -0.5:
        print("Wygląda na to, że masz pod tym względem słabszy dzień. Dasz radę! :)")
        if wave_value > calculate_wave(t + 1, wave_lengths[wave_type]):
            print("Patrz pozytywnie! Jutro będzie lepiej! :D")
    elif wave_value >= 0.5:
        print("Wygląda na to, że masz dobry dzień pod tym względem! :)")

# Wprowadzenie danych użytkownika
name = input("Podaj swoje imię: ")
year = int(input("Podaj rok swojego urodzenia: "))
month = int(input("Podaj miesiąc swojego urodzenia: "))
day = int(input("Podaj dzień swojego urodzenia: "))

# Obliczanie liczby dni od urodzin
current_date = datetime.datetime.now().date()
birth_date = datetime.date(year, month, day)
days_lived = (current_date - birth_date).days

print(f"Cześć {name}! Żyjesz już {days_lived} dni!")

# Wyświetlanie komunikatów o falach
for wave_type in wave_lengths:
    display_wave_message(wave_type, days_lived)