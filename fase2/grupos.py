# essa solução resolve parcialmente o problema, dando 39/100 pontos

import sys

estudantes, ngostam, nodeiam = map(int, sys.stdin.readline().split())

gostam = {i: set() for i in range(1, estudantes+1)}
for _ in range(ngostam):
    x, y = map(int, sys.stdin.readline().split())
    gostam[x].add(y)
    gostam[y].add(x)

odeiam = {i: set() for i in range(1, estudantes+1)}
for _ in range(nodeiam):
    x, y = map(int, sys.stdin.readline().split())
    odeiam[x].add(y)
    odeiam[y].add(x)

errados = 0
for i in range(int(estudantes / 3)):
    u, v, w = map(int, sys.stdin.readline().split())

    infracoes = len(gostam[u]) + len(gostam[v]) + len(gostam[w])

    if v in gostam[u]:
        infracoes -= 2
    if w in gostam[u]:
        infracoes -= 2
    if v in gostam[w]:
        infracoes -= 2
    
    for i in gostam[u]:
        gostam[i].discard(u)
    
    for i in gostam[v]:
        gostam[i].discard(v)

    for i in gostam[w]:
        gostam[i].discard(w)

    errados += infracoes

    if v in odeiam[u]:
        errados += 1
    if w in odeiam[u]:
        errados += 1
    if v in odeiam[w]:
        errados += 1
    

print(errados)