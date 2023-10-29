from collections import Counter

n, k = map(int, input().split())
tamanhos = [int(x) for x in input().split()]

uns = Counter(tamanhos)[1]
dois = Counter(tamanhos)[2]

balanceamento = 0

while k > 0:
    if uns >= 2:
        uns -= 2
        if uns % 2 == 0:
            uns -= 1
        else:
            dois -= 1
    elif dois >= 3:
        dois -= 3
    else:
        uns -= 1
        dois -= 2
        balanceamento += 1

    k -= 1

print(balanceamento)
        