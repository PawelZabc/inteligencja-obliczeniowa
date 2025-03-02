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

# Funkcja sprawdzająca, co zrobić w zależności od wyniku biorytmu
def sprawdz_biorytm(y, nazwa):
    if y > 0.5:
        print(f"Twój biorytm {nazwa} jest wysoki ({y:.2f}). Gratulacje! Czujesz się świetnie!")
    elif y < -0.5:
        print(f"Twój biorytm {nazwa} jest niski ({y:.2f}). Przykro mi, ale nie martw się!")
        print("Sprawdzimy, czy jutro będzie lepiej...")
        # Sprawdź biorytm na następny dzień
        if y < oblicz_biorytm(23, dni + 1) if nazwa == "fizyczny" else oblicz_biorytm(28, dni + 1) if nazwa == "emocjonalny" else oblicz_biorytm(33, dni + 1) > y:
            print("Nie martw się. Jutro będzie lepiej!")
        else:
            print("Jutro może być podobnie, ale daj sobie czas.")
    else:
        print(f"Twój biorytm {nazwa} jest w normie ({y:.2f}). Możesz poczuć się dobrze.")

# Główna część programu
def main():
    # Pobranie danych od użytkownika
    imie = input("Podaj swoje imię: ")
    rok_urodzenia = int(input("Podaj rok urodzenia: "))
    miesiac_urodzenia = int(input("Podaj miesiąc urodzenia: "))
    dzien_urodzenia = int(input("Podaj dzień urodzenia: "))
    
    # Obliczanie liczby dni od urodzin
    global dni
    dni = dni_od_urodzin(rok_urodzenia, miesiac_urodzenia, dzien_urodzenia)
    
    # Obliczanie biorytmów
    y_p = oblicz_biorytm(23, dni)  # Fala fizyczna (23 dni)
    y_e = oblicz_biorytm(28, dni)  # Fala emocjonalna (28 dni)
    y_i = oblicz_biorytm(33, dni)  # Fala intelektualna (33 dni)

    # Witaj użytkownika i wyświetl wyniki
    print(f"\nWitaj, {imie}!")
    print(f"Dziś jest Twój {dni}-ty dzień życia.")
    
    # Sprawdzanie biorytmów
    sprawdz_biorytm(y_p, "fizyczny")
    sprawdz_biorytm(y_e, "emocjonalny")
    sprawdz_biorytm(y_i, "intelektualny")

if __name__ == "__main__":
    main()
