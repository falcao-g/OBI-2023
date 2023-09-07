from collections import deque

tam1 = int(input())
palavra1 = [x for x in input()]
tam2 = int(input())
palavra2 = [x for x in input()]

fila1 = deque(palavra1)
fila2 = deque(palavra2)

total = 0

if tam1 > tam2:
    while fila2:
        letra = fila1.popleft()
        letra2 = fila2.popleft()

        if letra == letra2:
            total += 1
            continue
        break
else: 
    while fila1:
        letra = fila1.popleft()
        letra2 = fila2.popleft()

        if letra == letra2:
            total += 1
            continue
        break

print(total)