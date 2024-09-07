import numpy as np
import statistics
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

sync = np.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6])

asyncr = np.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2])

#MAXIMO E MINIMO
max_sync = max(sync)
min_sync = min(sync)
print(f"max sync: {max_sync}; min sync: {min_sync}\n")

max_asyncr = max(asyncr)
min_asyncr = min(asyncr)
print(f"max asyncr: {max_asyncr}; min asyncr: {min_asyncr}\n")


#HISTOGRAMA
plt.hist(sync, 5, (65, 95))
plt.show()

plt.hist(asyncr, 5, (65, 95))
plt.show()


#BOXPLOT
sns.boxplot(sync)
plt.show()

sns.boxplot(asyncr)
plt.show()


#BOXPLOT com gráficos um ao lado do outro
sns.boxplot([sync, asyncr])
plt.xticks([0, 1], ["sync", "asyncr"])
plt.title("Modelos de trabalho")
plt.xlabel("Work type")
plt.ylabel("Hours")
plt.show()


#OUTLIERS usando o gráfico boxplot (código com possível erro)
stock = pd.DataFrame({'open': sync}) 
stock.to_csv('stock_data.csv', index=False)
iris = pd.read_csv('sync.csv')
print(iris.head())

sns.boxplot(stock['open'])
plt.show()

open_prices = stock['open']
x = open_prices.mean()
ponto_corte = open_prices.std(ddof=1) * 3
inf = x - ponto_corte
sup = x + ponto_corte

outliers = open_prices[(open_prices < inf) | (open_prices > sup)]
print(f"outliers: {outliers}") #identificar outliers

