def define(n):
    for i in range(n):
        if i%12==0:
            yield i

n = int(input("n:"))
for i in define(n):
    print(i)
    