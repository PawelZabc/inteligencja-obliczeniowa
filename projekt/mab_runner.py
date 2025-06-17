import random
import subprocess
from collections import defaultdict
from mabwiser.mab import MAB, LearningPolicy

TARGET_FITNESS = 1000
N_ARMS = 20
N_TRIALS = 2000
SIMULATIONS = 1000
   # Liczba iteracji uczenia

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
        "-turnLimit", str(TARGET_FITNESS),
    ]
    if simulation:
        cmd.append("-worldAmount" )
        cmd.append(str(SIMULATIONS))
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        # print(f"RAW output: {output}")
        return int(output.strip())
    except Exception as e:
        print(f"Error: {e}")
        return 0

def generate_parameter_space(n=100):
    space = []
    for _ in range(n):
        combo = [
            random.randint(1, 50),  # initialGrass
            random.randint(2, 50),  # initialBunny
            random.randint(2, 50),  # initialFox
            random.randint(1, 50),  # bunnyStart
            random.randint(1, 50),  # bunnyFood
            random.randint(1, 50),  # bunnyCooldown
            random.randint(1, 50),  # bunnyFed
            random.randint(1, 5),   # bunnyChildren
            random.randint(5, 50),  # bunnyLiveLength
            random.randint(1, 50),  # foxStart
            random.randint(1, 50),  # foxCooldown
            random.randint(1, 50),  # foxFed
            random.randint(1, 5),   # foxChildren
            random.randint(5, 50),  # foxLiveLength
            random.randint(1, 50),  # grassFood
            random.randint(1, 50),  # grassCooldown
            random.randint(1, 5),   # grassChildren
            random.randint(5, 50),  # grassLiveLength
        ]
        space.append(combo)
    return space

def main():
    param_space = generate_parameter_space(N_ARMS)
    arms = list(range(len(param_space)))

    # ✅ Używamy UCB1 – obsługuje wartości rzeczywiste
    mab = MAB(arms=arms, learning_policy=LearningPolicy.UCB1(), seed=42)
    # mab = MAB(arms=arms, learning_policy=LearningPolicy.EpsilonGreedy(epsilon=0.1), seed=42)

    mab.fit([], [])

    rewards = defaultdict(list)

    for t in range(N_TRIALS):
        arm = mab.predict()
        params = param_space[arm]
        result = run_simulation(params)
        rewards[arm].append(result)

        mab.partial_fit([arm], [result])  # bez normalizacji – UCB1 obsługuje to

        print(f"[{t+1}/{N_TRIALS}] Ramię {arm} | Wynik: {result}")

    # Analiza najlepszego ramienia
    best_arm = max(rewards, key=lambda a: sum(rewards[a]) / len(rewards[a]))
    best_params = param_space[best_arm]
    best_avg_result = sum(rewards[best_arm]) / len(rewards[best_arm])

    print("\n=== Najlepsze parametry (UCB1) ===")
    print("Średni wynik:", best_avg_result)
    print("Parametry:", best_params)

    final_result = run_simulation(best_params,simulation=False)
    print(f"Wynik końcowy symulacji z najlepszymi parametrami: {final_result}")

if __name__ == "__main__":
    main()
