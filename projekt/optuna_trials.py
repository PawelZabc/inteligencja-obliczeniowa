import optuna
import subprocess

TARGET_FITNESS = 1000
simulations = 100

# Twoja funkcja symulacji
def run_simulation(params):
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

# Optuna objective
def objective(trial):
    # Zamiast ręcznie pisać listy zakresów, definiujemy je dynamicznie
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
    result = run_simulation(params)
    print(f"Trial result: {result} for params: {params}")
    return -result  # bo optuna minimalizuje

study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=30)

print("\n=== Najlepszy wynik (optuna) ===")
print("Najlepszy wynik:", -study.best_value)
print("Najlepsze parametry:", study.best_params)

# Jeśli chcesz uruchomić symulację jeszcze raz na najlepszych parametrach:
final_params = list(study.best_params.values())
result = run_simulation(final_params)
print(f"Wynik końcowej symulacji z optuna: {result}")
