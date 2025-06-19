import subprocess

TARGET_FITNESS = 500
SIMULATIONS = 100

def run_simulation(params, simulation=True):
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
        "-foxLiveLength", str(int(params[13])),
        "-grassFood", str(int(params[14])),
        "-grassCooldown", str(int(params[15])),
        "-grassChildren", str(int(params[16])),
        "-grassLiveLength", str(int(params[17])),
        "-turnLimit", str(TARGET_FITNESS),
    ]
    if simulation:
        cmd.append("-worldAmount")
        cmd.append(str(SIMULATIONS))
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        return int(output.strip())
    except Exception as e:
        if not simulation:
            return
        print(f"Błąd w symulacji: {e}")
        return 0