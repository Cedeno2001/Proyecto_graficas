import pandas as pd
import matplotlib.pyplot as plt

data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 73, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
    
}

df = pd.DataFrame(data)
plt.figure(figsize=(10, 6))
plt.boxplot([df[df['materia'] == materia]['nota'] for materia in df['materia'].unique()], labels=df['materia'].unique())
plt.title('distribucion de notas por materia')
plt.xlabel('materias')
plt.ylabel('notas')
plt.show()


aprobados_counts = df['aprobado'].value_counts()
labels = aprobados_counts.index
colors = ['turquoise', 'cornflowerblue']

plt.figure(figsize=(8, 8))
plt.pie(aprobados_counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('proporcion de estudiantes aprobados y no aprobados')
plt.show()