saldo = int(input())
contas = [int(input()) for _ in range(3)]
contas.sort()
pagas = 0

for conta in contas:
    if conta <= saldo:
        pagas += 1
        saldo -= conta

print(pagas)