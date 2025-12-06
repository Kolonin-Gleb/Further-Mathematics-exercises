import numpy as np
import matplotlib.pyplot as plt

# Определение системы
def system(X, Y):
    dX = X - 3*Y
    dY = 5*X + 9*Y
    return dX, dY

# Создание сетки
x_range = np.linspace(-10, 10, 20)
y_range = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x_range, y_range)

# Вычисление векторов
U, V = system(X, Y)

# Нормализация стрелок для красоты графика
N = np.sqrt(U**2 + V**2)
U, V = U/N, V/N

plt.figure(figsize=(8, 8))

# Построение векторного поля
plt.quiver(X, Y, U, V, angles='xy', color='blue', alpha=0.5)

# Построение собственных векторов (асимптот)
x_vals = np.array([-10, 10])
# v2 = (-1, 1) -> y = -x
plt.plot(x_vals, -x_vals, 'g--', linewidth=2, label='v2 (y=-x, lambda=4)')
# v1 = (-3, 5) -> y = -(5/3)x
plt.plot(x_vals, -(5/3)*x_vals, 'r--', linewidth=2, label='v1 (y=-5/3x, lambda=6)')

# Настройки графика
plt.title('Фазовый портрет: Неустойчивый узел')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.legend()
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.show()