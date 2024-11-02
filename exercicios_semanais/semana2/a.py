def isalternate(string):
    alternate = True
    for l in range(len(string)-1):
        if string[l] == string[l+1]:
            alternate = False
    return alternate

def biggestalternate(string):
    letters = []
    for l in string:
        if l not in letters:
            letters.append(l)
    
    comb = []

    for i in range(len(letters)):
        for j in range(i+1, len(letters)):
            duo = [letters[i],letters[j]]
            comb.append(duo)

    bigger = 0
    for duo in comb:
        alt = ''
        for l in string:
            if l in duo:
                alt += l
        if isalternate(alt) and len(alt) > bigger:
            bigger = len(alt)
    
    return bigger

lenstring = int(input())
string = input()
print(biggestalternate(string))
