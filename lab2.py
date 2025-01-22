#python booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


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
