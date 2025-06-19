import pandas as pd
import matplotlib.pyplot as plt
import os

pygad_df = pd.read_csv("pygad_results.csv")
pyswarm_df = pd.read_csv("pyswarm_particles.csv")
optuna_df = pd.read_csv("optuna_results.csv")
cmaes_df = pd.read_csv("cmaes_results.csv")


def prepare_df(df, iter_col, fitness_col, time_col, label):
    df_clean = df[[iter_col, fitness_col, time_col]].copy()
    df_clean.columns = ["Iteration", "Fitness", "TimeElapsed"]
    df_clean["Method"] = label
    return df_clean

pygad_data = prepare_df(pygad_df, "Generation", "Fitness", "TimeElapsed", "PyGAD")
pyswarm_data = prepare_df(pyswarm_df, "Iteration", "Fitness", "TimeElapsed", "PySwarm")
optuna_data = prepare_df(optuna_df, "Trial", "Fitness", "TimeElapsed", "Optuna")
cmaes_data = prepare_df(cmaes_df, "EvalNumber", "Fitness", "TimeElapsed", "CMA-ES")


all_data = pd.concat([pygad_data, pyswarm_data, optuna_data, cmaes_data], ignore_index=True)


os.makedirs("wykresy_algorytmów", exist_ok=True)


plt.figure(figsize=(12, 6))
for method, group in all_data.groupby("Method"):
    plt.plot(group["Iteration"], group["Fitness"], label=method, alpha=0.7)
plt.xlabel("Iteracja / Próba / Ewaluacja")
plt.ylabel("Fitness")
plt.title("Porównanie wyników fitness dla różnych optymalizatorów")
plt.legend()
plt.grid(True)
plt.savefig("wykresy_algorytmów/fitness_porownanie.png")
plt.show()

mean_times = all_data.groupby("Method")["TimeElapsed"].mean()
mean_times.plot(kind="bar", figsize=(8,5), color=["blue", "orange", "green", "red"])
plt.ylabel("Średni czas [s]")
plt.title("Średni czas działania na iterację")
plt.savefig("wykresy_algorytmów/sredni_czas.png")
plt.show()

plt.figure(figsize=(10,6))
all_data.boxplot(column="Fitness", by="Method")
plt.title("Rozkład wyników fitness")
plt.suptitle("")
plt.xlabel("Metoda")
plt.ylabel("Fitness")
plt.savefig("wykresy_algorytmów/boxplot_fitness.png")
plt.show()


plt.figure(figsize=(12, 6))
for method, group in all_data.groupby("Method"):
    plt.scatter(group["TimeElapsed"].cumsum(), group["Fitness"], label=method, alpha=0.6)
plt.xlabel("Skumulowany czas [s]")
plt.ylabel("Fitness")
plt.title("Fitness względem skumulowanego czasu")
plt.legend()
plt.grid(True)
plt.savefig("wykresy_algorytmów/fitness_vs_czas_suma.png")
plt.show()

plt.figure(figsize=(12, 6))
for method, group in all_data.groupby("Method"):
    group_sorted = group.sort_values("TimeElapsed")
    plt.plot(group_sorted["TimeElapsed"], group_sorted["Fitness"], label=method, alpha=0.7)
plt.xlabel("Czas jednej próby [s]")
plt.ylabel("Fitness")
plt.title("Fitness względem czasu jednej iteracji")
plt.legend()
plt.grid(True)
plt.savefig("wykresy_algorytmów/fitness_vs_czas_jednostkowy.png")
plt.show()

for method in all_data["Method"].unique():
    subset = all_data[all_data["Method"] == method]

    plt.figure(figsize=(10, 5))
    plt.plot(subset["Iteration"], subset["Fitness"], marker='o')
    plt.xlabel("Iteracja")
    plt.ylabel("Fitness")
    plt.title(f"{method}: Fitness vs Iteracja")
    plt.grid(True)
    plt.savefig(f"wykresy_algorytmów/{method}_fitness_iteracja.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(subset["TimeElapsed"].cumsum(), subset["Fitness"], marker='.')
    plt.xlabel("Skumulowany czas [s]")
    plt.ylabel("Fitness")
    plt.title(f"{method}: Fitness vs Skumulowany czas")
    plt.grid(True)
    plt.savefig(f"wykresy_algorytmów/{method}_fitness_czas_suma.png")
    plt.close()

    plt.figure(figsize=(5, 5))
    subset.boxplot(column="Fitness")
    plt.title(f"{method}: Rozkład Fitness")
    plt.ylabel("Fitness")
    plt.savefig(f"wykresy_algorytmów/{method}_boxplot_fitness.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(subset["Iteration"], subset["TimeElapsed"], marker='o', color='orange')
    plt.xlabel("Iteracja")
    plt.ylabel("Czas [s]")
    plt.title(f"{method}: Czas jednej iteracji")
    plt.grid(True)
    plt.savefig(f"wykresy_algorytmów/{method}_czas_na_iteracje.png")
    plt.close()

 
best_by_method = all_data.groupby("Method")["Fitness"].max().sort_values(ascending=False)
print("\n Najlepsze fitnessy:")
print(best_by_method)
plt.figure(figsize=(12, 6))
for method, group in all_data.groupby("Method"):
    plt.plot(group["Iteration"], group["TimeElapsed"], label=method, alpha=0.7)
plt.xlabel("Iteracja / Próba / Ewaluacja")
plt.ylabel("Czas jednej iteracji [s]")
plt.title("Czas jednej iteracji dla różnych optymalizatorów")
plt.legend()
plt.grid(True)
plt.savefig("wykresy_algorytmów/czas_na_iteracje_porownanie.png")
plt.show()
