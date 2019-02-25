import numpy as np
import scipy.stats as st

tiempos = np.array([
    [83, 20, 56, 121],
    [1938, 949, 1453, 2342],
    [844, 939, 932, 638],
    [994, 593, 734, 1029],
    [95, 19, 24, 68]
])
print("Datos")
print(tiempos)

print("Promedio")
print(np.mean(tiempos, axis=0))

print("Media armónica")
print(st.hmean(tiempos))

print("Media geométrica")
print(st.gmean(tiempos))

data_to_norm = np.c_[tiempos[:, 0], tiempos[:, 3]]
ref = tiempos[:, 1]
norm_data = data_to_norm / ref.reshape((5, 1))

print("A y D normalizados respecto a B")
print(norm_data)

print("Promedio A D normalizados")
print(np.mean(norm_data, axis=0))

print("Media armónica A D normalizados")
print(st.hmean(norm_data))

print("Media geométrica A D normalizados")
print(st.gmean(norm_data))


