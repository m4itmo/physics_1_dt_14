from time import sleep

import matplotlib.pyplot as plt
import numpy as np

permittivity_1 = float(input("Введите диэлектрическую проницаемость среды 1 (пример: 2): ") or 2)
permittivity_2 = float(input("Введите диэлектрическую проницаемость среды 2 (пример: 4): ") or 4)
E_magnitude = float(input("Введите величину электрического поля (пример: 5): ") or 5)
E_angle = float(input("Введите угол электрического поля (в градусах, пример: 45): ") or 45)

E_angle_rad = np.radians(E_angle)

E1_x = E_magnitude * np.cos(E_angle_rad)
E1_y = E_magnitude * np.sin(E_angle_rad)

D1n = permittivity_1 * E1_y
D2n = D1n / permittivity_2

E2_x = E1_x
E2_y = D2n / permittivity_2

E2_magnitude = np.sqrt(E2_x ** 2 + E2_y ** 2)
E2_angle = np.arctan2(E2_y, E2_x)

fig, ax = plt.subplots()

ax.quiver(-E1_x, -E1_y, E1_x, E1_y, angles='xy', scale_units='xy', scale=1, color='blue', label='E1 (входное поле)')

ax.quiver(0, 0, E2_x, E2_y, angles='xy', scale_units='xy', scale=1, color='red', label='E2 (преломленное поле)')

ax.axhline(0, color='black', linewidth=0.8, linestyle='--', label='Граница раздела')

ax.set_xlim(-E_magnitude, E_magnitude)
ax.set_ylim(-E_magnitude, E_magnitude)
ax.set_aspect('equal', adjustable='box')
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
plt.title('Преломление линий напряженности на границе диэлектриков')
sleep(10)
plt.show()
