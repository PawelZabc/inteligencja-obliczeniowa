import subprocess
import pygad
import numpy as np

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
        "-foxLiveLength", str(int(params[13])),  # poprawione
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

def fitness_func(pygad,solution, solution_idx):
    # PyGAD oczekuje, że fitness_func przyjmuje solution i solution_idx
    fitness = run_simulation(solution)
    return fitness

gene_space = [
    list(range(1, 51)),  # initialGrass
    list(range(1, 51)),  # initialBunny
    list(range(1, 51)),  # initialFox
    list(range(1, 51)),  # bunnyStart
    list(range(1, 51)),  # bunnyFood
    list(range(1, 51)),  # bunnyCooldown
    list(range(1, 51)),  # bunnyFed
    list(range(1, 6)),   # bunnyChildren
    list(range(1, 51)),  # bunnyLiveLength
    list(range(1, 51)),  # foxStart
    list(range(1, 51)),  # foxCooldown
    list(range(1, 51)),  # foxFed
    list(range(1, 6)),   # foxChildren
    list(range(1, 51)),  # foxLiveLength
    list(range(1, 51)),  # grassFood
    list(range(1, 51)),  # grassCooldown
    list(range(1, 6)),   # grassChildren
    list(range(1, 51)),  # grassLiveLength
]

# Parametry algorytmu genetycznego
sol_per_pop = 20
num_genes = 18
num_parents_mating = 10
num_generations = 30
keep_parents = 8
parent_selection_type = "tournament"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 10  # mutujemy 10% genów na osobnika

def on_generation(ga_instance):
    best_fitness = ga_instance.best_solution()[1]
    print(f"Epoka {ga_instance.generations_completed + 1} — najlepszy fitness: {best_fitness}")
    if best_fitness >= TARGET_FITNESS:
        print(f"Osiągnięto cel fitness ({TARGET_FITNESS}), zatrzymuję algorytm.")
        ga_instance.stop_run = True

# Inicjalizacja GA
ga_instance = pygad.GA(
    gene_space=gene_space,
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_func,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    parent_selection_type=parent_selection_type,
    keep_parents=keep_parents,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_percent_genes=mutation_percent_genes,
    on_generation=on_generation
)

ga_instance.run()

# Najlepsze rozwiązanie
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Najlepsze parametry: {solution}")
print(f"Wartość fitness: {solution_fitness}")

ga_instance.plot_fitness()

# Wywołanie symulacji na najlepszym rozwiązaniu (możesz usunąć jeśli niepotrzebne)
cmd = [
    "./symulacja",
    "-initialGrass", str(int(solution[0])),
    "-initialBunny", str(int(solution[1])),
    "-initialFox", str(int(solution[2])),
    "-bunnyStart", str(int(solution[3])),
    "-bunnyFood", str(int(solution[4])),
    "-bunnyCooldown", str(int(solution[5])),
    "-bunnyFed", str(int(solution[6])),
    "-bunnyChildren", str(int(solution[7])),
    "-bunnyLiveLength", str(int(solution[8])),
    "-foxStart", str(int(solution[9])),
    "-foxCooldown", str(int(solution[10])),
    "-foxFed", str(int(solution[11])),
    "-foxChildren", str(int(solution[12])),
    "-foxLiveLength", str(int(solution[13])),
    "-grassFood", str(int(solution[14])),
    "-grassCooldown", str(int(solution[15])),
    "-grassChildren", str(int(solution[16])),
    "-grassLiveLength", str(int(solution[17])),
    "-turnLimit", str(TARGET_FITNESS),
]

try:
    output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
    print(f"Wynik symulacji dla najlepszego rozwiązania: {output.decode().strip()}")
except Exception as e:
    print(f"Błąd przy wywołaniu symulacji: {e}")
