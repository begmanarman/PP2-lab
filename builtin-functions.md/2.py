string = "Arman Begman"
upper = 0
tow = 0
for i in string:
    if i >='A' and i <='Z':
        upper +=1
        continue
    tow+=1

print(upper)
print(tow)