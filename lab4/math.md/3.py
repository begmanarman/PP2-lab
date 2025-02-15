import math
def area(n,m):
    r = math.tan(math.pi / n)
    s= n*(m**2)/(4*r)
    return s
n = int(input("n "))
m = int(input("m"))
print(area(n,m))