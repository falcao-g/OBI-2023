import heapq

n, m = map(int, input().split())
carros = [int(x) for x in input().split()]
carros.sort()

mecanicos = [int(x) for x in input().split()]
mecanicos.sort()

mecanicos_esperas = {x: [] for x in range(len(mecanicos))}

heapq.heapify(carros)

for i in range(len(mecanicos) -1 , -1, -1):
    carro = heapq.heappop(carros)
    mecanicos_esperas[i].append(carro * mecanicos[i])
    if not carros:
        break

mecanico_atual = len(mecanicos) - 1

while carros:
    carro = heapq.heappop(carros)
    mecanico = mecanicos[mecanico_atual]
    mecanicos_esperas[mecanico_atual].append(mecanicos_esperas[mecanico_atual][-1] + carro * mecanicos[i])
    mecanico_atual -= 1
    if mecanico_atual < 0:
        mecanico_atual = len(mecanicos) - 1
        
if n > 1:
    print(sum([sum(x[:-1]) for x in mecanicos_esperas.values()]))
else:
    print(sum([sum(x) for x in mecanicos_esperas.values()]))