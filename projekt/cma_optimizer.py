import cma
import random
import csv
import time
from run_simulation import run_simulation

csv_filename = "cmaes_results.csv"
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["EvalNumber", "Fitness", "TimeElapsed"] + [
        "initialGrass", "initialBunny", "initialFox", "bunnyStart", "bunnyFood", "bunnyCooldown",
        "bunnyFed", "bunnyChildren", "bunnyLiveLength", "foxStart", "foxCooldown", "foxFed",
        "foxChildren", "foxLiveLength", "grassFood", "grassCooldown", "grassChildren", "grassLiveLength"
    ])

eval_counter = 0

def objective_function(params):
    global eval_counter
    eval_counter += 1

    int_params = list(map(int, params))
    start_time = time.time()
    fitness = run_simulation(int_params)
    elapsed_time = time.time() - start_time

    print(f"Ewaluacja {eval_counter}: Parametry: {int_params} => Wynik: {fitness}, czas: {elapsed_time:.4f}s")

    with open(csv_filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([eval_counter, fitness, round(elapsed_time, 4)] + int_params)

    return -fitness 

SIGMA = 10
BOUNDS = [
    (1, 50), (1, 50), (1, 50),
    (1, 50), (1, 50), (1, 50),
    (1, 50), (1, 5), (1, 50),
    (1, 50), (1, 50), (1, 50),
    (1, 5), (1, 50),
    (1, 50), (1, 50), (1, 5),
    (1, 50)
]
lower_bounds = [lo for lo, _ in BOUNDS]
upper_bounds = [hi for _, hi in BOUNDS]
START = [(lo + hi) / 2 for lo, hi in BOUNDS]

es = cma.CMAEvolutionStrategy(START, SIGMA, {
    'bounds': [list(x) for x in zip(*BOUNDS)],
    'popsize': 20,
    'maxfevals': 20*1000,
    'verb_disp': 1
})

es.optimize(objective_function)

best_params = list(map(int, es.result.xbest))
best_fitness = -es.result.fbest

print("\n=== Najlepsze parametry (CMA-ES) ===")
print("Wynik symulacji:", best_fitness)
print("Parametry:", best_params)

run_simulation(best_params, simulation=False)
