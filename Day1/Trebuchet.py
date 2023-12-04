def isdigit(c):
    if '0' <= c <= '9':
        return int(c)
    return -1

res = 0
with open('inp.txt','r') as fd:
    txt = fd.readlines()
for line in txt:
    first = -1
    last = -1
    for c in line:
        if isdigit(c) != -1:
            if first == -1:
                first = isdigit(c)
            last = isdigit(c)
    if first != -1 and last != -1:
        res += first * 10 + last
    
print(res)