frecs = {'A':2.7e9, 'C':48e6}
longs = {'B':3e-9, 'D':4e-3}
ciclos = [24e6, 48e6, 15e6, 0.3e6, 100e6]
tiempos = {}

for comp, frec in frecs.items():
    temp = []
    for cic in ciclos :
        temp.append(cic/frec)
    tiempos[comp] = temp

for comp, long in longs.items():
    temp = []
    for cic in ciclos :
        temp.append(cic*long)
    tiempos[comp] = temp

print(tiempos)