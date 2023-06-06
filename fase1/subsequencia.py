from collections import deque

input()
fila1 = deque([int(x) for x in input().split()])
fila2 = deque([int(x) for x in input().split()])

sub = True
while fila2:
    n = fila2.popleft()
    m = fila1.popleft()
    while m != n and fila1:
        m = fila1.popleft()

    if n != m or not fila1 and fila2:
        sub = False
        break

if sub:
    print('S')
else:
    print('N')