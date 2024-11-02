def coquinhaGelada(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        n += 1
    return n//3 + coquinhaGelada(n%3 + n//3)


for _ in range(10):
    n = int(input())
    if n == 0:
        break
    else:
        print(coquinhaGelada(n))