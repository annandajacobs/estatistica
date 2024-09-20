import numpy as np
import statistics
import scipy

sync = np.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6])

asyncr = np.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2])


# p = scipy.stats.shapiro(sync)
# q = scipy.stats.shapiro(asyncr)

# if p.pvalue < 0.05:
#     print("Rejeitar H0")
# else:
#     print("Não rejeitar H0")

# if q.pvalue < 0.05:
#     print("Rejeitar H0")
# else:
#     print("Não rejeitar H0")   

lista = []

lista.append(scipy.stats.kurtosis(sync))
lista.append(scipy.stats.kurtosis(asyncr))

for i in lista:
    if i == 0:
        print("Simétrica")
    elif i > 0:
        print("Cauda a direita")
    else:
        print("Cauda a esquerda")