#python booleans
print(10 > 1)
print(10 == 2)
print(10 < 1)

a = 200
b = 33

if b > a:
  print("yes")
else:
  print("no")


print(bool("Hello"))
print(bool(15))
print(bool())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = "vwvwv"
print(isinstance(x, str))



# Операторы Python
print(10 + 5)

x = 5

print(x > 3 and x < 10)


print(2 & 6)

#python list
list = ["apple", "banana", "cherry"]
print(list[1])

list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[:4])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[2:])


a =[ "arman", "samat"]
a.append("sake")

print(a)
a.remove("arman")
a.pop(1)

#python tuples


my_name=("arman, begmanov, abdusattar")

print(my_name)

print(my_name[1])

print(len(my_name))

#python sets

arman={"sake, samat, shyngus,1 ,true,0, False"}

print(arman)

print(len(arman))


print("sake" in arman)

print("sake" not in arman)

arman.add("jake")

ggg={"nurik, askar"}

arman.update(ggg)

arman.remove("sake")

set3=arman.union(ggg)

set4= arman| ggg

#python dictionaries

dict1={"sake" : "friend",
      }

a=dict1.get("sake")

s=dict1.keys()

print(s)

dict1["sake"]= "2006"

dict1["jake"] = "2017"

dict1.pop("sake")

#python if else

x=2
y=4
if x<=y :
  print("Yes")
elif a!=0:
  print("no")
else :
  print("1")



#whille loops
i = 1
while i < 6:
  print(i)
  i += 1


