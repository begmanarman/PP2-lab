import os
import string

with open("builtin-functions.md/directory.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
