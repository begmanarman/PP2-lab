def palindrom(num):
    
    for i in range(len(num)//2):
        if num[i] != num[len(num)-1-i]:
            return False
        return True
            
    
    

num=list(map(int,input("enter: ").split()))
print(palindrom(num))