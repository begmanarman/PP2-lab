
def squere(n,m):
    for i in range(n,m):
         yield i**2

n = int(input("a:"))
m = int(input("b:"))
for i in squere(n,m):
    print(i)