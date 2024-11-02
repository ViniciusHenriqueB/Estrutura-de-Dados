q = int(input())
lista = [int(x) for x in input().split()]

p = 0
n = 0
z = 0

for e in lista:
    if e > 0:
        p+=1
    elif e < 0:
        n+=1
    else:
        z+=1

print(f'{p/q:.6f}')
print(f'{n/q:.6f}')
print(f'{z/q:.6f}')