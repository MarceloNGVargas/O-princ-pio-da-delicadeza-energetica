import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pathlib import Path

C = 1
alpha = 1
k_B = 1.38e-23
gamma = 1

T_fixed = 300
epsilon_fixed = 1e-21
N_fixed = 1e6
tau_fixed = 1e-3

def delta_x_min(T, epsilon, N, tau):
    numerator = np.sqrt(k_B * T + gamma * epsilon)
    denominator = np.sqrt(N * tau)
    return (C / alpha) * (numerator / denominator)

T_vals = np.linspace(1, 1000, 200)
dx_T = delta_x_min(T_vals, epsilon_fixed, N_fixed, tau_fixed)

epsilon_vals = np.linspace(1e-24, 1e-20, 200)
dx_epsilon = delta_x_min(T_fixed, epsilon_vals, N_fixed, tau_fixed)

N_vals = np.logspace(3, 9, 200)
dx_N = delta_x_min(T_fixed, epsilon_fixed, N_vals, tau_fixed)

tau_vals = np.logspace(-6, 0, 200)
dx_tau = delta_x_min(T_fixed, epsilon_fixed, N_fixed, tau_vals)

T_grid, epsilon_grid = np.meshgrid(np.linspace(1, 1000, 100), np.linspace(1e-24, 1e-20, 100))
dx_surface = delta_x_min(T_grid, epsilon_grid, N_fixed, tau_fixed)

try:
    plt.style.use('seaborn-v0_8')
except Exception:
    try:
        plt.style.use('seaborn')
    except Exception:
        pass

images_dir = Path(__file__).resolve().parents[1] / "images"
images_dir.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(6, 4))
plt.plot(T_vals, dx_T, color='blue')
plt.xlabel('Temperatura T (K)')
plt.ylabel('δx_min (m)')
plt.title('δx_min vs Temperatura T')
plt.grid(True)
plt.tight_layout()
plt.savefig(images_dir / 'dx_vs_t.png')

plt.figure(figsize=(6, 4))
plt.plot(epsilon_vals, dx_epsilon, color='green')
plt.xlabel('Energia por probe ε (J)')
plt.ylabel('δx_min (m)')
plt.title('δx_min vs Energia ε')
plt.grid(True)
plt.tight_layout()
plt.savefig(images_dir / 'dx_vs_epsilon.png')

plt.figure(figsize=(6, 4))
plt.semilogx(N_vals, dx_N, color='red')
plt.xlabel('Número de probes N')
plt.ylabel('δx_min (m)')
plt.title('δx_min vs Número de probes N')
plt.grid(True)
plt.tight_layout()
plt.savefig(images_dir / 'dx_vs_n.png')

plt.figure(figsize=(6, 4))
plt.semilogx(tau_vals, dx_tau, color='purple')
plt.xlabel('Tempo de coerência τ (s)')
plt.ylabel('δx_min (m)')
plt.title('δx_min vs Tempo de coerência τ')
plt.grid(True)
plt.tight_layout()
plt.savefig(images_dir / 'dx_vs_tau.png')

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(T_grid, epsilon_grid, dx_surface, cmap='viridis')
ax.set_xlabel('Temperatura T (K)')
ax.set_ylabel('Energia ε (J)')
ax.set_zlabel('δx_min (m)')
ax.set_title('δx_min vs T e ε')
plt.tight_layout()
plt.savefig(images_dir / 'dx_surface_t_epsilon.png')

print("Gráficos salvos em:", images_dir)
