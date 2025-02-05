def sett(nums):
    x=[]
    for i in nums:
        if i not in x:
            x.append(i)
    return x

nums = list(map(int,input("enter").split()))
print(sett(nums))