import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("puntaje.txt", delimiter=', ')

plt.figure(figsize=(10, 8))
plt.fill_between(data["Examen1"], data["Examen2"], color='yellow', alpha=0.8)
plt.xlabel('Puntajes Examen 1')
plt.ylabel('Puntajes Examen 2')
plt.title('Comparación de Puntos en dos exámenes')
plt.show()
