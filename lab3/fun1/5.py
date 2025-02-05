from itertools import permutations
def permit(s) :
    perm = permutations(s)
    for i in perm :
        print(i)


string =input("str :")
permit(string)

string =list(map(str,input("str :").split()))
string.reverse()
print(string)
