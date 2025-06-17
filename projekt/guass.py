import numpy as np

# Wektory v1, v2, v3
A = np.array([
    [1, 2, -1],
    [1, 2, 2],
    [0, 2, 3],
    [1, 0, 1]
], dtype=float)

# Wektor po prawej stronie
w = np.array([-3, 4, 9, 5], dtype=float)

# Próba znalezienia rozwiązania układu A * x = w
try:
    solution = np.linalg.lstsq(A, w, rcond=None)[0]
    residuals = np.linalg.lstsq(A, w, rcond=None)[1]
    print("Rozwiązanie (a,b,c):", solution)
    print("Reszty (błąd):", residuals)
except np.linalg.LinAlgError:
    print("Układ jest sprzeczny lub niewłaściwie określony")
