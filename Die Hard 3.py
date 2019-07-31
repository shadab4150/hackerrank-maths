"""
https://www.hackerrank.com/challenges/die-hard-3/problem
"""


import math

def JugFill(a,b,c):
    if c<max(a,b) and c%math.gcd(a,b)==0:
        return "YES"
    else:
        return "NO"
    

n=int(input())

for i in range(n):
    
    a,b,c=[int(x) for x in input().split()]
    
    # Am+Bn=C    gcd(m,n) % d == 0
    
    print(JugFill(a,b,c))
