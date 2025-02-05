def c(nums):
    agent = [] 

    for num in nums:
        if num == 0 or num == 7:
            agent.append(num)  


    if agent[:3] == [0, 0, 7]:
        return True
    return False


x = list(map(int, input("arr: ").split()))
print(c(x))