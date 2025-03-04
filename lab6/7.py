

with open("builtin-functions.md/directory.txt","r") as x, open("/Users/armanbegman/Desktop/work/labs/builtin-functions.md/another.txt","w") as y:
    y.write(x.read())