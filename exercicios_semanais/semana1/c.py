h,m,s = input().split(':')

for i in range(len(s)):
    if i == 2 and s[i] == 'A':
        if h == '12':
            h = '00'
        
    if i == 2 and s[i] == 'P' and h != '12':
        h = int(h)
        h+=12

print(f'{h}:{m}:{s[:-2]}')