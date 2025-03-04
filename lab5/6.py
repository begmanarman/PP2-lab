import re

string = str(input("string: "))

newstr = re.sub(r"[., ]",':',string)
print(newstr)
