n = int(input())
gostade = [int(x) for x in input().split()]
safadeza = False

for i in range(n):
    if gostade[i] == gostade[gostade[gostade[gostade[i] - 1] - 1] - 1]:
        safadeza = True
        break

if safadeza:
    print('YES')
else:
    print('NO')