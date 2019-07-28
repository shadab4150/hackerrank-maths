"""
https://www.hackerrank.com/challenges/restaurant/problem
"""


""""
Martha is interviewing at Subway. 
One of the rounds of the interview requires her to cut a bread of size (L x B) into smaller identical pieces. 
Such that each piece is a square having maximum possible side length with no left over piece of bread.
"""
#python 3 Time complexity O(1)

import math
n=int(input())

for _ in range(n):
    l,b=[int(x) for x in input().split()]
    Max_squares=(l//(math.gcd(l,b)))*(b//(math.gcd(l,b)))
    print(Max_squares)
