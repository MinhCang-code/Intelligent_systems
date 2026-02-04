import numpy as np
import matplotlib.pyplot as plt

def trimf(x, a, b, c):
    return np.maximum(np.minimum((x - a) / (b - a + 1e-6), (c - x) / (c - b + 1e-6)), 0)

x_T = np.linspace(20, 35, 300)

mu_cold = trimf(x_T, 20, 22, 25)
mu_comfort = trimf(x_T, 24, 26, 28)
mu_hot = trimf(x_T, 27, 30, 35)

plt.figure(figsize=(8, 4))
plt.plot(x_T, mu_cold, label="Lạnh")
plt.plot(x_T, mu_comfort, label="Dễ chịu")
plt.plot(x_T, mu_hot, label="Nóng")
plt.title("Tập mờ cho T_in (°C)")
plt.xlabel("T_in (°C)")
plt.ylabel("Mức thuộc")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

