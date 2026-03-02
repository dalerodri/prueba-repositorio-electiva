#grafica 1
import matplotlib.pyplot as plt
import numpy as np

# Generamos tres grupos de datos
np.random.seed(42)
grupo1 = np.random.normal(10, 2, 200)
grupo2 = np.random.normal(11, 2.9, 150)
grupo3 = np.random.normal(20, 3, 180)

datos = [grupo1, grupo2, grupo3]

plt.figure(figsize=(8, 6))
plt.boxplot(datos, labels=["Grupo 1", "Grupo 2", "Grupo 3"])
plt.title("Diagrama de cajas y bigotes")
plt.ylabel("Valores")
plt.xlabel("Grupos")
plt.grid(True, alpha=0.3)
plt.show()


#grafica 2
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(8, 6))

# Crear la elipse: centro (0,0), ancho=6, alto=4, rotada 30°, color azul claro
elipse = Ellipse(xy=(9, 8), width=6, height=4, angle=30,
                 edgecolor='darkblue', facecolor='lightblue', 
                 linewidth=2, alpha=0.6)

ax.add_patch(elipse)
ax.set_xlim(-4, 4)
ax.set_ylim(-3, 3)
ax.set_title('Gráfico de una elipse')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.grid(True, alpha=0.3)
ax.axis('equal')  
plt.savefig('elipse.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.tight_layout()
plt.show()


#GRAFICA 3
import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo: matriz 10x12 (ej: ventas por mes y producto)
np.random.seed(42)
data = np.random.rand(10, 12) * 100  # Valores 0-100

# Crear el mapa de calor
plt.figure(figsize=(10, 7))
im = plt.imshow(data, cmap='YlOrRd', interpolation='nearest')  # 'hot', 'viridis', 'plasma'

# Barra de colores
plt.colorbar(im, label='Valor')

# Etiquetas
plt.title('Mapa de calor (heatmap) - Ejemplo ventas', fontsize=16)
plt.xlabel('Meses')
plt.ylabel('Productos')
plt.xticks(np.arange(12), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.yticks(np.arange(10), [f'Prod {i+1}' for i in range(10)])
plt.savefig('mapa_calor.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.tight_layout()
plt.show()
