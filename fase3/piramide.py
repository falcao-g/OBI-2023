def main():
    pesos = [int(x) for x in input().split()]
    pesos.sort()
    resto = sum(pesos) % 3
    divisao = sum(pesos) // 3

    if resto != 0:
        print("N")
        return
    
    if not divisao in pesos:
        print("N")
        return
    
    pesos.remove(divisao)

    for index, value in enumerate(pesos):
        if value > divisao:
            print('N')
            break

    if sum(pesos) == divisao * 2:
        print('S')
    else:
        print('N')

main()