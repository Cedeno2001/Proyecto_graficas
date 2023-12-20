import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]


plt.figure(figsize=(8, 6))
plt.scatter(matematicas, ciencias, color='red', alpha=0.7)
plt.title('relacion entre graficas de matematicas y ciencias')
plt.xlabel('clasificacion de matematicas')
plt.ylabel('clasificacion de ciencias')
plt.grid(True)
plt.show()


materias = ['Matematicas', 'Ciencias', 'Literatura']
promedios = [np.mean(matematicas), np.mean(ciencias), np.mean(literatura)]
errores = np.array([errores_matematicas, errores_ciencias, errores_literatura]).T
plt.figure(figsize=(10, 6))
plt.bar(materias, promedios, yerr=errores, capsize=5, color=['coral', 'yellowgreen', 'mediumaquamarine'])
plt.title('clasificacion de promedios con barras de error')
plt.xlabel('materias')
plt.ylabel('clasificacion promedio')
plt.legend(['clasificacion promedio'])
plt.grid(axis='y')
plt.show()


plt.figure(figsize=(8, 6))
plt.hist(matematicas, bins=10, color='dodgerblue', edgecolor='black', alpha=0.7)
plt.title('distribucion de clasificacion de matematicas')
plt.xlabel('calificaciones de Matemáticas')
plt.ylabel('frecuencia')
plt.grid(axis='y')
plt.show()
