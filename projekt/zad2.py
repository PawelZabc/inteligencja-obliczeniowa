import pyswarms as ps 
import numpy as np
import math
from pyswarms.utils.plotters import plot_cost_history 
import matplotlib.pyplot as plt
import subprocess

TARGET_FITNESS = 1000
simulations = 100

def run_simulation(params):
    # Wszystkie parametry są już int, z zakresów gene_space
    cmd = [
        "./symulacja",
        "-initialGrass", str(int(params[0])),
        "-initialBunny", str(int(params[1])),
        "-initialFox", str(int(params[2])),
        "-bunnyStart", str(int(params[3])),
        "-bunnyFood", str(int(params[4])),
        "-bunnyCooldown", str(int(params[5])),
        "-bunnyFed", str(int(params[6])),
        "-bunnyChildren", str(int(params[7])),
        "-bunnyLiveLength", str(int(params[8])),
        "-foxStart", str(int(params[9])),
        "-foxCooldown", str(int(params[10])),
        "-foxFed", str(int(params[11])),
        "-foxChildren", str(int(params[12])),
        "-foxLiveLength", str(int(params[13])),
        "-grassFood", str(int(params[14])),
        "-grassCooldown", str(int(params[15])),
        "-grassChildren", str(int(params[16])),
        "-grassLiveLength", str(int(params[17])),
        "-worldAmount", str(simulations),
        "-turnLimit", str(TARGET_FITNESS),
    ]

    try:
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        result = int(output.strip())
        return result
    except Exception as e:
        print(f"Error: {e} with params {params}")
        return 0

def fitness(input): 
    output = []
    for i, particle in enumerate(input):
        rounded_particle = [int(round(x)) for x in particle]
        fitness_value = -run_simulation(rounded_particle)
        print(f"Generacja: cząstka {i}, fitness: {-fitness_value}")
        output.append(fitness_value)  # negatyw bo PSO minimalizuje
    return output

options = {'c1': 0.5, 'c2': 0.9, 'w': 0.7} 

# bounds (18 wymiarów)
my_bounds = (
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # dolne granice
    [50, 50, 50, 50, 50, 50, 50, 5, 50, 50, 50, 50, 5, 50, 50, 50, 5, 50]   # górne granice
)

# Uwaga! Tu musi być 18 dimensions, nie 6
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=18, options=options, bounds=my_bounds)

# Optymalizacja
best_cost, best_pos = optimizer.optimize(fitness, iters=30)

# Wyniki końcowe
best_params = [int(round(x)) for x in best_pos]
print(f"\nNajlepsze parametry: {best_params}")
print(f"Najlepszy fitness: {-best_cost}")

# Uruchomienie symulacji z najlepszymi parametrami

# final_result = run_simulation(best_params)

cmd = [
        "./symulacja",
        "-initialGrass", str(int(best_params[0])),
        "-initialBunny", str(int(best_params[1])),
        "-initialFox", str(int(best_params[2])),
        "-bunnyStart", str(int(best_params[3])),
        "-bunnyFood", str(int(best_params[4])),
        "-bunnyCooldown", str(int(best_params[5])),
        "-bunnyFed", str(int(best_params[6])),
        "-bunnyChildren", str(int(best_params[7])),
        "-bunnyLiveLength", str(int(best_params[8])),
        "-foxStart", str(int(best_params[9])),
        "-foxCooldown", str(int(best_params[10])),
        "-foxFed", str(int(best_params[11])),
        "-foxChildren", str(int(best_params[12])),
        "-foxLiveLength", str(int(best_params[13])),
        "-grassFood", str(int(best_params[14])),
        "-grassCooldown", str(int(best_params[15])),
        "-grassChildren", str(int(best_params[16])),
        "-grassLiveLength", str(int(best_params[17])),
        "-turnLimit", str(TARGET_FITNESS),
    ]
print(f"Wynik końcowej symulacji z najlepszymi parametrami: {subprocess.check_output(cmd, stderr=subprocess.DEVNULL)}")


# Wykres kosztu
plot_cost_history(optimizer.cost_history)
plt.title("Historia funkcji celu (negatywna wartość)")
plt.show()
