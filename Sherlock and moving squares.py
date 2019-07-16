"""""
https://www.hackerrank.com/challenges/sherlock-and-moving-tiles/problem

""""""
#python 3

import math
l, s1, s2 =[int(x) for x in input().split()]
for i in range(int(input())):
    a=int(input())
    time=math.sqrt(2)*(l-math.sqrt(a))/abs(s2-s1)
    print(time)
