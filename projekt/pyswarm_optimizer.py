import pyswarms as ps 
import numpy as np
import math
import csv
import time
from pyswarms.utils.plotters import plot_cost_history 
import matplotlib.pyplot as plt
from run_simulation import run_simulation

# Plik logujący cząstki
with open("pyswarm_particles.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Iteration", "Particle", "Fitness","TimeElapsed"] + [f"Param{i}" for i in range(18)])
current_iteration = 0


def fitness(input): 
    output = []
    with open("pyswarm_particles.csv", mode='a', newline='') as file:
        writer = csv.writer(file)

        global current_iteration
        current_iteration+=1
        for i, particle in enumerate(input):
            rounded_particle = [int(round(x)) for x in particle]
            start_time = time.time()
            fitness_value = -run_simulation(rounded_particle)
            elapsed_time = time.time() - start_time

            print(f"Iteracja {current_iteration}, cząstka {i}, fitness: {-fitness_value}, czas: {elapsed_time:.4f}s")

            writer.writerow(
                [current_iteration, i, -fitness_value, round(elapsed_time, 4)] + rounded_particle
            )
            output.append(fitness_value)  # negatyw bo PSO minimalizuje
    return output

options = {'c1': 0.3, 'c2': 0.9, 'w': 0.9}


my_bounds = (
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # dolne granice
    [50, 50, 50, 50, 50, 50, 50, 5, 50, 50, 50, 50, 5, 50, 50, 50, 5, 50]   # górne granice
)

optimizer = ps.single.GlobalBestPSO(n_particles=20, dimensions=18, options=options, bounds=my_bounds)


best_cost, best_pos = optimizer.optimize(fitness, iters=1000)

best_params = [int(round(x)) for x in best_pos]
print(f"\nNajlepsze parametry: {best_params}")
print(f"Najlepszy fitness: {-best_cost}")


run_simulation(best_params,simulation=False)


# Wykres kosztu
plot_cost_history(optimizer.cost_history)
plt.title("Historia funkcji celu (negatywna wartość)")
plt.show()
