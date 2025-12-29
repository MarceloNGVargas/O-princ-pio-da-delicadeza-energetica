import matplotlib.pyplot as plt
from pathlib import Path

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.axis('off')

ax.text(0.1, 0.6, 'Macro\n(energia colossal)', fontsize=12, ha='center', va='center', bbox=dict(boxstyle='round', fc='#f0f0f0'))
ax.text(0.5, 0.6, 'Micro\n(nível sub-quântico)', fontsize=12, ha='center', va='center', bbox=dict(boxstyle='round', fc='#f0f0f0'))
ax.text(0.9, 0.6, 'Resolução mínima\n(energia mínima)', fontsize=12, ha='center', va='center', bbox=dict(boxstyle='round', fc='#f0f0f0'))

ax.annotate('', xy=(0.4, 0.6), xytext=(0.2, 0.6), arrowprops=dict(arrowstyle='->', lw=2))
ax.annotate('', xy=(0.8, 0.6), xytext=(0.6, 0.6), arrowprops=dict(arrowstyle='->', lw=2))

ax.text(0.5, 0.3, 'T ↓   ε ↓   N ↑   τ ↑   α ↑', fontsize=13, ha='center', va='center')

images_dir = Path(__file__).resolve().parents[1] / "images"
images_dir.mkdir(parents=True, exist_ok=True)
out = images_dir / "diagram_macro_micro_resolucao.png"
fig.savefig(out, dpi=160, bbox_inches='tight')
print("Diagrama salvo em:", out)
