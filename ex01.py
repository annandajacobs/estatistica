import numpy as np
from statistics import multimode

sync = np.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6])

asyncr = np.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2])

#media
x1 = sync.mean()
x2 = asyncr.mean()

print(f"Média x1: {x1}")
print(f"Média x2: {x2}\n")

#mediana
me1 = np.median(sync)
me2 = np.median(asyncr)

print(f"Mediana me1: {me1}")
print(f"Mediana me2: {me2}\n")

#percentil
q1s = np.percentile(sync, 25)
q3s = np.percentile(sync, 75)
q1a = np.percentile(asyncr, 25)
q3a = np.percentile(asyncr, 75)

print(f"primeiro quartil sync: {q1s}")
print(f"terceiro quartil sync: {q3s}")
print(f"primeiro quartil asyncr: {q1a}")
print(f"terceiro quartil asyncr: {q3a}\n")

#moda
moda1 = multimode(sync)
moda2 = multimode(asyncr)

print(f"Moda sync: {moda1}")
print(f"Moda asyncr: {moda2}\n")

#amplitude
r1 = sync.ptp()
r2 = asyncr.ptp()

print(f"Amplitude sync: {r1}")
print(f"Amplitude asyncr: {r2}\n")

#amplitude interquartil
iqr1 = q3s - q1s
iqr2 = q3a - q1a

print(f"IQR sync: {iqr1}")
print(f"IQR asyncr: {iqr2}\n")
