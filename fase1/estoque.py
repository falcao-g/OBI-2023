m, n = map(int, input().split())
estoque = []

for i in range(m):
    estoque.append([int(x) for x in input().split()])

qtd_vendas = int(input())
vendas_realizadas = 0

for j in range(qtd_vendas):
    x, y = map(int, input().split())
    atual = estoque[x-1][y-1]
    if atual > 0:
        vendas_realizadas += 1
        estoque[x-1][y-1] -= 1

print(vendas_realizadas)