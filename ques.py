
from collections import Counter

def solve(s, sub):
    total= Counter([s[i : i+len(sub)] for i in range(len(s))])
    return total[sub]
s=input("string: ")
sub=input("sub string: ")
print(solve(s, sub)) 
