def sort(n):
    even =[]
    for i in range(n):
        
        if (i +1)%2==0:
            even.append(i+1)
    
    return even
n =int(input("n:"))
print(",".join(map(str,sort(n))))
