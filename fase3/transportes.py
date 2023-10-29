import heapq
n, m, k = map(int, input().split())
preco = int(input())
distancia = [float('inf') for i in range(n+1)]
processado = [False for i in range(n+1)]
vizinhos = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    vizinhos[a].append((c, b))
    vizinhos[b].append((c, a))

origem, destino = map(int, input().split())

def Djikstra(S):
    distancia[S] = 0
    fila = [(0, S)]

    while fila:
        davez = -1

        while fila:
            dist, atual = heapq.heappop(fila)

            if not processado[atual]:
                davez = atual
                break

        if davez == -1:
            break

        processado[davez] = True

        for dist, atual in vizinhos[davez]:
            if distancia[atual] > distancia[davez] + dist:
                distancia[atual] = distancia[davez] + dist
                heapq.heappush(fila, (distancia[atual], atual))

Djikstra(origem)

if distancia[destino] == float('inf'):
    print(-1)
else:
    print(preco)