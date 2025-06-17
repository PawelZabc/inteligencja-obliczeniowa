import sys

print("Wklej mapę (Ctrl+D aby zakończyć wklejanie):")

# Wczytywanie danych z stdin (Ctrl+D kończy wklejanie)
# lines = sys.stdin.read().splitlines()
lines = "......B....B.F..F....BB.B.BBBBB.FF.F.F.........B.B.FFFFF..B...B.BBB.B..FB.F.F.FFBB.B...BB..F.FFFF.F.....B..B...F.F.BF.F...B.BBFFFBF..F.BBBBB..BBB.FFF...F.BB.B.B.B....FFF.B....F......B...B.B.FFF..BFFF.......BB.BFFF..BFFF........B.BFFF...FFFF....FFF..B.B.BFFFGFG...BFFF.B.BBB.FFGFFF.B..FFF......FFFF...B..BFFF..B..BF...FF...B.BFFFFFFB.FFFB....BB.BBFG..F.BF....B.GB.BBFFFFFF..FFF.....BB.B.B........BB..."

# Liczenie
bunnies = sum(row.count('B') for row in lines)
foxes = sum(row.count('F') for row in lines)
grass = sum(row.count('G') for row in lines)

print(f"Bunnies: {bunnies}")
print(f"Foxes: {foxes}")
print(f"Grass: {grass}")