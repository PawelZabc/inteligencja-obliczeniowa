import subprocess
import pygad

TARGET_FITNESS = 1000
simulations = 100

def run_simulation(params):
    # Konwersja genów na int, zabezpieczenie przed 0 i wartościami ujemnymi

    # llGrass = max(1, int(round(params[3])))
    # llBunny = max(1, int(round(params[4])))
    # llFox   = max(1, int(round(params[5])))

    cmd = [
        "./symulacja",
        "-initialGrass", str(max(1, int(round(params[0])))),
        "-initialBunny", str(max(1, int(round(params[1])))),
        "-initialFox", str(max(1, int(round(params[2])))),

        "-bunnyStart", str(max(1, int(round(params[3])))),
        "-bunnyFood", str(max(1, int(round(params[4])))),
        "-bunnyCooldown", str(max(1, int(round(params[5])))),
        "-bunnyFed", str(max(1, int(round(params[6])))),
        "-bunnyChildren", str(max(1, int(round(params[7])))),
        "-bunnyLiveLength", str(max(1, int(round(params[8])))),

        "-foxStart", str(max(1, int(round(params[9])))),
        "-foxCooldown", str(max(1, int(round(params[10])))),
        "-foxFed", str(max(1, int(round(params[11])))),
        "-foxChildren", str(max(1, int(round(params[12])))),
        "-foxLiveLength", str(max(1, int(round(params[13])))),

        "-grassFood", str(max(1, int(round(params[14])))),
        "-grassCooldown", str(max(1, int(round(params[15])))),
        "-grassChildren", str(max(1, int(round(params[16])))),
        "-grassLiveLength", str(max(1, int(round(params[17])))),
        "-worldAmount",str(simulations),
        "-turnLimit",str(TARGET_FITNESS)
    ]

    try:
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        result = int(output.strip())
        return result
    except Exception as e:
        print(f"Error: {e} with params {params}")
        return 0

def fitness_func(i,solution, solution_idx):
    # PyGAD oczekuje fitness jako float, więc zwracamy wynik symulacji
    fitness = run_simulation(solution)
    return fitness

gene_space = [
    {"low": 1, "high": 100},  # initialGrass
    {"low": 1, "high": 100},   # initialBunny
    {"low": 1, "high": 100},   # initialFox
    {"low": 1, "high": 100},  # bunnyStart
    {"low": 1, "high": 100},   # bunnyFood
    {"low": 1, "high": 100},   # bunnyCooldown
    {"low": 1, "high": 100},  # bunnyFed
    {"low": 1, "high": 8},   # bunnyChildren
    {"low": 1, "high": 100},   # bunnyLiveLength
    {"low": 1, "high": 100},   # foxStart
    {"low": 1, "high": 100},   # foxCooldown
    {"low": 1, "high": 100},   # foxFed
    {"low": 1, "high": 8},  # foxChildren
    {"low": 1, "high": 100},   # foxLiveLength
    {"low": 1, "high": 100},   # grassFood
    {"low": 1, "high": 100},  # grassCoolown
    {"low": 1, "high": 8},   # grassChilren
    {"low": 1, "high": 100},   # grassLiveLength
]


import numpy as np







# Define chromosome parameters
# Genes are either 0 or 1
# gene_space = [0, 1]


fitness_function = fitness_func

# Number of chromosomes in the population
sol_per_pop = 10

# Number of genes 
num_genes = 18

# Number of parents to "mate" (around 50% of population)
num_parents_mating = 5

# Number of generations
num_generations = 1000

# How many parents to keep for the next generation
keep_parents = 4

# Parent selection type: "sss" (steady state), "rws" (roulette wheel), "rank", "tournament"
parent_selection_type = "sss"

# Crossover type: "single_point"
crossover_type = "single_point"
# Mutation settings
mutation_type = "random"
mutation_percent_genes = 40  # 8% of genes

def on_generation(ga_instance):
    best_fitness = ga_instance.best_solution()[1]
    print(f"Nowa epoka: {ga_instance.generations_completed + 1}")
    print(f"Epoka {ga_instance.generations_completed + 1} — najlepszy fitness: {best_fitness}")
    
    if best_fitness >= TARGET_FITNESS:
        print(f"Osiągnięto cel fitness ({TARGET_FITNESS}), zatrzymuję algorytm.")
        ga_instance.stop_run = True

# Initialize the algorithm with the above parameters
ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       on_generation=on_generation)

# Run the GA algorithm
ga_instance.run()

# Summary: Best solution found (chromosome + fitness)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Parameters of the best solution: {solution}")
print(f"Fitness value of the best solution = {solution_fitness}")
ga_instance.plot_fitness()

cmd = [
        "./symulacja",
        "-initialGrass", str(max(1, int(round(solution[0])))),
        "-initialBunny", str(max(1, int(round(solution[1])))),
        "-initialFox", str(max(1, int(round(solution[2])))),

        "-bunnyStart", str(max(1, int(round(solution[3])))),
        "-bunnyFood", str(max(1, int(round(solution[4])))),
        "-bunnyCooldown", str(max(1, int(round(solution[5])))),
        "-bunnyFed", str(max(1, int(round(solution[6])))),
        "-bunnyChildren", str(max(1, int(round(solution[7])))),
        "-bunnyLiveLength", str(max(1, int(round(solution[8])))),

        "-foxStart", str(max(1, int(round(solution[9])))),
        "-foxCooldown", str(max(1, int(round(solution[10])))),
        "-foxFed", str(max(1, int(round(solution[11])))),
        "-foxChildren", str(max(1, int(round(solution[12])))),
        "-bunnyLiveLength", str(max(1, int(round(solution[13])))),

        "-grassFood", str(max(1, int(round(solution[14])))),
        "-grassCooldown", str(max(1, int(round(solution[15])))),
        "-grassChildren", str(max(1, int(round(solution[16])))),
        "-grassLiveLength", str(max(1, int(round(solution[17])))),
    ]

output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)