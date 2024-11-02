def catsandmouse(gatoAp,gatoBp,ratop):
    if abs(gatoAp-ratop)<abs(gatoBp-ratop):
        return 'Cat A'
    elif abs(gatoAp-ratop)>abs(gatoBp-ratop):
        return 'Cat B'
    else:
        return 'Mouse C'
    
q = int(input())

for _ in range(q):
    x,y,z = map(int, input().split())
    print(catsandmouse(x,y,z))