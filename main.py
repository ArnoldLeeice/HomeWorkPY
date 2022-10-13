n = float(input())
n = str(n)
total = 0
b = n.replace("0", "")
c = b.replace(".", "")
res = int(c)
while res > 0:
    a = res % 10
    total += a
    res = res // 10
print(total)




from math import *
n = int(input())
res = []
for i in range(1, n+1):
    i = factorial(i)
    a = res.append(i)
print(res)





n = int(input())
total = 0
for i in range(n):
    m = int(input())
    res = (1 + 1 / m)**m
    total += res
print(round(total, 2))
