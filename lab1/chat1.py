import datetime
import math

# Funkcja obliczająca biorytm
def oblicz_biorytm(okres, t):
    return math.sin((2 * math.pi / okres) * t)

# Funkcja obliczająca liczbę dni od urodzin
def dni_od_urodzin(rok_urodzenia, miesiac_urodzenia, dzien_urodzenia):
    data_urodzin = datetime.date(rok_urodzenia, miesiac_urodzenia, dzien_urodzenia)
    dzisiaj = datetime.date.today()
    return (dzisiaj - data_urodzin).days

# Główna część programu
def main():
    # Pobranie danych od użytkownika
    imie = input("Podaj swoje imię: ")
    rok_urodzenia = int(input("Podaj rok urodzenia: "))
    miesiac_urodzenia = int(input("Podaj miesiąc urodzenia: "))
    dzien_urodzenia = int(input("Podaj dzień urodzenia: "))
    
    # Obliczanie liczby dni od urodzin
    dni = dni_od_urodzin(rok_urodzenia, miesiac_urodzenia, dzien_urodzenia)
    
    # Obliczanie biorytmów
    y_p = oblicz_biorytm(23, dni)  # Fala fizyczna (23 dni)
    y_e = oblicz_biorytm(28, dni)  # Fala emocjonalna (28 dni)
    y_i = oblicz_biorytm(33, dni)  # Fala intelektualna (33 dni)

    # Witaj użytkownika i wyświetl wyniki
    print(f"\nWitaj, {imie}!")
    print(f"Dziś jest Twój {dni}-ty dzień życia.")
    print(f"Twój biorytm fizyczny: {y_p:.2f}")
    print(f"Twój biorytm emocjonalny: {y_e:.2f}")
    print(f"Twój biorytm intelektualny: {y_i:.2f}")

if __name__ == "__main__":
    main()
