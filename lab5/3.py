import re
string  = list(input("string; ").split())
pattrern = r'\b[A-Za-z]+_[a-z]+\b'
for i in string:
    if re.match(pattrern,i):
        print(f"'{i}' ok ")