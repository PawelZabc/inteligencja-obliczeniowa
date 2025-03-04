import tkinter as tk
import math

# Tworzymy okno
root = tk.Tk()
root.title("Wykres sinusoidy")

# Ustalamy wymiary okna
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Ustawienia układu współrzędnych
center_x = 200
center_y = 200
scale = 50  # Skala, żeby wykres nie był za duży

# Rysujemy wykres sinusoidy
for x in range(-180, 180):
    # Przemiana kąta w radiany
    radian = math.radians(x)
    y = math.sin(radian)

    # Rysowanie punktów na wykresie
    canvas.create_oval(center_x + x, center_y - y * scale, center_x + x + 1, center_y - y * scale + 1, fill="blue")

# Uruchamiamy główną pętlę aplikacji
root.mainloop()
