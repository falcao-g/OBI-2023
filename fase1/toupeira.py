import sys

s, t = map(int, sys.stdin.readline().split())

caminhos = {i: set() for i in range(1, s+1)}

for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    caminhos[x].add(y)
    caminhos[y].add(x)

testes = int(sys.stdin.readline())
possiveis = 0

for _ in range(testes):
    caminho = [int(n) for n in sys.stdin.readline().split()]
    del caminho[0]
    possivel = True
    for indice, salao in enumerate(caminho):
        if indice == len(caminho) - 1:
            break
        elif caminho[indice+1] in caminhos[salao]:
            continue
        else:
            possivel = False
            break
    if possivel:
        possiveis += 1

print(possiveis)
