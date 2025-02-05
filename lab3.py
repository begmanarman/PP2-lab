def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]


#numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
#abprime_numbers = filter_prime(numbers)
#print("Prime numbers:", prime_numbers)

#from itertools import permutations
#def permit(s) :
    perm = permutations(s)
    for i in perm :
        print(i)


#string =input("str :")
#permit(string)

#string =list(map(str,input("str :").split()))
#string.reverse()
#print(string)



#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def x(num) :
    for i in range(len(num)-1) :
        if num[i] ==3 and num[i+1]==3:
            return True
    return False

#arr =list(map(int,input("arr :").split()))
#print(x(arr))

#Write a function that takes in a list of integers and returns True if it contains 007 in order
def c(nums):
    agent = [] 

    for num in nums:
        if num == 0 or num == 7:
            agent.append(num)  


    if agent[:3] == [0, 0, 7]:
        return True
    return False


#x = list(map(int, input("arr: ").split()))
#print(c(x))

#Write a function that computes the volume of a sphere given its radius.
def volume(r):
    vol =(4/3)*(r**3)
    print(vol)

#print(volume(3))

#Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

def sett(nums):
    x=[]
    for i in nums:
        if i not in x:
            x.append(i)
    return x

#nums = list(map(int,input("enter").split()))
#print(sett(nums))

#palindrome
def palindrom(num):
    
    for i in range(len(num)//2):
        if num[i] != num[len(num)-1-i]:
            return False
        return True
            
    
    

#num=list(map(int,input("enter: ").split()))
#print(palindrom(num))

def histogram(num):
    for i in num:
        print("*" * i)
       
      

#num =list(map(int,input("enter:").split()))
#histogram(num)

#task 13
name =input("Hello ! What is your name ")


        
        

        
    

    
  