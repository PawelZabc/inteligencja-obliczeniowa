import optuna


TARGET_FITNESS = 1000
simulations = 100
from run_simulation import run_simulation

import csv
import time

csv_filename = "optuna_results.csv"
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Trial", "Fitness", "TimeElapsed"] + [
        "initialGrass", "initialBunny", "initialFox", "bunnyStart", "bunnyFood", "bunnyCooldown",
        "bunnyFed", "bunnyChildren", "bunnyLiveLength", "foxStart", "foxCooldown", "foxFed",
        "foxChildren", "foxLiveLength", "grassFood", "grassCooldown", "grassChildren", "grassLiveLength"
    ])

def objective(trial):
    params = [
        trial.suggest_int("initialGrass", 1, 50),
        trial.suggest_int("initialBunny", 1, 50),
        trial.suggest_int("initialFox", 1, 50),
        trial.suggest_int("bunnyStart", 1, 50),
        trial.suggest_int("bunnyFood", 1, 50),
        trial.suggest_int("bunnyCooldown", 1, 50),
        trial.suggest_int("bunnyFed", 1, 50),
        trial.suggest_int("bunnyChildren", 1, 5),
        trial.suggest_int("bunnyLiveLength", 1, 50),
        trial.suggest_int("foxStart", 1, 50),
        trial.suggest_int("foxCooldown", 1, 50),
        trial.suggest_int("foxFed", 1, 50),
        trial.suggest_int("foxChildren", 1, 5),
        trial.suggest_int("foxLiveLength", 1, 50),
        trial.suggest_int("grassFood", 1, 50),
        trial.suggest_int("grassCooldown", 1, 50),
        trial.suggest_int("grassChildren", 1, 5),
        trial.suggest_int("grassLiveLength", 1, 50),
    ]
    
    start_time = time.time()
    result = run_simulation(params)
    elapsed_time = time.time() - start_time

    print(f"Trial {trial.number} result: {result} — czas: {elapsed_time:.4f}s")

    with open(csv_filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([trial.number, result, round(elapsed_time, 4)] + params)

    return -result 


study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=1000)

print("\n=== Najlepszy wynik (optuna) ===")
print("Najlepszy wynik:", -study.best_value)
print("Najlepsze parametry:", study.best_params)

final_params = list(study.best_params.values())
run_simulation(final_params,simulation=False)
