import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("ventasMensuales.txt", delimiter=', ')

ventas_mes = data.groupby("Mes")["Ventas"].sum()
plt.figure(figsize=(10, 6))
plt.barh(ventas_mes.index, ventas_mes.values, color='green')
plt.xlabel('Cantidad de Ventas')
plt.ylabel('Meses')
plt.title('Distribución de Ventas por Mes')
plt.gca().invert_yaxis()
plt.show()
