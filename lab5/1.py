import re

arman = "abbbb a ab"
pattern = r'ab*'
a=re.findall(pattern,arman)
print(a)

