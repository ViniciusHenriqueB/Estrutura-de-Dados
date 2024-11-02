s,t = map(int, input().split())
appletree,orangetree = map(int, input().split())
qapples,qoranges = map(int, input().split())
dapples = [int(x) for x in input().split()]
doranges = [int(x) for x in input().split()]

apples = 0
oranges = 0

for apple in dapples:
    position = apple + appletree
    if position>=s and position<=t:
        apples+=1
for orange in doranges:
    position = orange + orangetree
    if position>=s and position<=t:
        oranges+=1

print(apples)
print(oranges)

