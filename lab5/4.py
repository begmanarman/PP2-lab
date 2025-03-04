import re
string  = list(input("string; ").split())
pattrern = r'\b[A-Z][a-z]+\b'
for i in string:
    if re.match(pattrern,i):
        print(f"'{i}' ok ")

