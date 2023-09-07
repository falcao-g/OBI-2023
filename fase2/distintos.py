# essa solução resolve parcialmente o problema, dando 41/100 pontos

import sys
from collections import deque

candidatos = deque()
diferentes = set()

tam = int(input())
metade = tam / 2
for _ in range(tam):
    candidatos.append(int(sys.stdin.readline()))

maior = 1
atual = 1

while candidatos:
    atual = 1
    pai = candidatos.popleft()
    outros = candidatos.copy()
    if not outros:
        break
    outro = outros.popleft()
    diferentes.add(pai)
    while outro not in diferentes:
        diferentes.add(outro)
        atual += 1
        if not outros:
            break
        outro = outros.popleft()
    outros.clear()
    diferentes.clear()
    maior = max(maior, atual)

    if maior >= metade:
        break

maior = max(maior, atual)
print(maior)