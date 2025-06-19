import pygad
import numpy as np
import csv
import time
from run_simulation import run_simulation

TARGET_FITNESS = 1000
simulations = 100

csv_filename = "pygad_results.csv"

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Generation", "Fitness", "TimeElapsed"])

previous_time = time.time()

def fitness_func(pygad, solution, solution_idx):
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

sol_per_pop = 20
num_genes = 18
num_parents_mating = 10
num_generations = 1000
keep_parents = 2
parent_selection_type = "tournament"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 40

def on_generation(ga_instance):
    global previous_time
    current_time = time.time()
    elapsed_time = current_time - previous_time
    previous_time = current_time

    generation = ga_instance.generations_completed
    best_fitness = ga_instance.best_solution()[1]
    
    print(f"Epoka {generation + 1} — najlepszy fitness: {best_fitness} — czas: {elapsed_time:.4f} s")

    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([generation, best_fitness, round(elapsed_time, 4)])

    if best_fitness >= TARGET_FITNESS:
        print(f"Osiągnięto cel fitness ({TARGET_FITNESS}), zatrzymuję algorytm.")
        ga_instance.stop_run = True

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

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Najlepsze parametry: {solution}")
print(f"Wartość fitness: {solution_fitness}")

ga_instance.plot_fitness()

run_simulation(solution, simulation=False)
