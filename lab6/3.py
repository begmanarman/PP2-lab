import os

def check(a):
    if os.path.exists(a):
        x = list(os.listdir(a))
        print(x)
    else:
        print("does not exist")

check(r"/Users/armanbegman/Desktop/pp")