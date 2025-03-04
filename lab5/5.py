import re
 
 
strings = list(input("strings:").split(" "))
 
pattern = r'^a.*b$'
 
 
for s in strings:
    if re.match(pattern, s):
        print(f"'{s}' соответствует паттерну.")
    else:
        print(f"'{s}' не соответствует паттерну.")