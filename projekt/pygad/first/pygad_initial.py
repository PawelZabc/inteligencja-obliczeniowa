import subprocess
import pygad

def run_simulation(params):
    # Konwersja genów na int, zabezpieczenie przed 0 i wartościami ujemnymi
    initialGrass = max(1, int(round(params[0])))
    initialBunny = max(1, int(round(params[1])))
    initialFox = max(1, int(round(params[2])))

    cmd = [
        "./symulacja",
        "-initialGrass", str(initialGrass),
        "-initialBunny", str(initialBunny),
        "-initialFox", str(initialFox)
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
]

# ga_instance = pygad.GA(
#     num_generations=20,
#     num_parents_mating=5,
#     fitness_func=fitness_func,
#     sol_per_pop=10,
#     num_genes=3,
#     gene_space=gene_space,
#     mutation_percent_genes=20,
# )

# ga_instance.run()

# solution, solution_fitness, _ = ga_instance.best_solution()
# print(f"Najlepsze parametry: initialGrass={int(round(solution[0]))}, initialBunny={int(round(solution[1]))}, initialFox={int(round(solution[2]))}")
# print(f"Maksymalna liczba tur: {solution_fitness}")
import numpy as np







# Define chromosome parameters
# Genes are either 0 or 1
# gene_space = [0, 1]


fitness_function = fitness_func

# Number of chromosomes in the population
sol_per_pop = 10

# Number of genes (length of the array S)
num_genes = 3

# Number of parents to "mate" (around 50% of population)
num_parents_mating = 2

# Number of generations
num_generations = 30

# How many parents to keep for the next generation
keep_parents = 2

# Parent selection type: "sss" (steady state), "rws" (roulette wheel), "rank", "tournament"
parent_selection_type = "sss"

# Crossover type: "single_point"
crossover_type = "single_point"

# Mutation settings
mutation_type = "random"
mutation_percent_genes = 8  # 8% of genes

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
                       mutation_percent_genes=mutation_percent_genes)

# Run the GA algorithm
ga_instance.run()

# Summary: Best solution found (chromosome + fitness)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Parameters of the best solution: {solution}")
print(f"Fitness value of the best solution = {solution_fitness}")
ga_instance.plot_fitness()