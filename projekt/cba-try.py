import cma
import random
import subprocess

# Funkcja celu: negatywny wynik symulacji (bo CMA-ES minimalizuje)
def objective_function(params):
    int_params = list(map(int, params))
    fitness = run_simulation(int_params)
    print(f"Testowane parametry: {int_params} => Wynik: {fitness}")
    return -fitness  # bo CMA-ES minimalizuje

# Twoja istniejąca funkcja do uruchomienia symulacji
def run_simulation(params, simulation=True):
    cmd = [
        "./symulacja",
        "-initialGrass", str(params[0]),
        "-initialBunny", str(params[1]),
        "-initialFox", str(params[2]),
        "-bunnyStart", str(params[3]),
        "-bunnyFood", str(params[4]),
        "-bunnyCooldown", str(params[5]),
        "-bunnyFed", str(params[6]),
        "-bunnyChildren", str(params[7]),
        "-bunnyLiveLength", str(params[8]),
        "-foxStart", str(params[9]),
        "-foxCooldown", str(params[10]),
        "-foxFed", str(params[11]),
        "-foxChildren", str(params[12]),
        "-foxLiveLength", str(params[13]),
        "-grassFood", str(params[14]),
        "-grassCooldown", str(params[15]),
        "-grassChildren", str(params[16]),
        "-grassLiveLength", str(params[17]),
        "-turnLimit", str(1000),
    ]
    if simulation:
        cmd.append("-worldAmount")
        cmd.append(str(100))  # liczba symulacji
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        return int(output.strip())
    except Exception as e:
        print(f"Błąd w symulacji: {e}")
        return 0

# Parametry startowe i zakresy
SIGMA = 10              # rozrzut początkowy
BOUNDS = [              # dolne i górne ograniczenia
    (1, 50), (1, 50), (1, 50),     # initialGrass, initialBunny, initialFox
    (1, 50), (1, 50), (1, 50),     # bunnyStart, bunnyFood, bunnyCooldown
    (1, 50), (1, 5), (1, 50),      # bunnyFed, bunnyChildren, bunnyLiveLength
    (1, 50), (1, 50), (1, 50),     # foxStart, foxCooldown, foxFed
    (1, 5), (1, 50),               # foxChildren, foxLiveLength
    (1, 50), (1, 50), (1, 5),      # grassFood, grassCooldown, grassChildren
    (1, 50),                      # grassLiveLength
]
lower_bounds = [lo for lo, _ in BOUNDS]
upper_bounds = [hi for _, hi in BOUNDS]
START         = [(lo + hi) / 2 for lo, hi in BOUNDS]

# Uruchamiamy CMA-ES z ograniczeniami
es = cma.CMAEvolutionStrategy(START, SIGMA, {
    'bounds': [list(x) for x in zip(*BOUNDS)],  # rozdziel dolne i górne granice
    'popsize': 10,
    'maxfevals': 500,
    'verb_disp': 1
})

# Główna pętla optymalizacji
es.optimize(objective_function)

# Najlepsze rozwiązanie
best_params = list(map(int, es.result.xbest))
best_fitness = -es.result.fbest  # odwrócone, bo minimalizowaliśmy

print("\n=== Najlepsze parametry (CMA-ES) ===")
print("Wynik symulacji:", best_fitness)
print("Parametry:", best_params)

# (Opcjonalnie) ostatni test bez -worldAmount
final_result = run_simulation(best_params, simulation=False)
# print(f"Wynik końcowy bez uśrednienia: {final_result}")
