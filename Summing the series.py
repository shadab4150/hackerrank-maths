""""
https://www.hackerrank.com/challenges/summing-the-n-series/problem
"""
"""
You are given a sequence whose n(th) term is:

 Tn = n^2 - (n - 1)^2
You have to evaluate the series

 Sn = T1  + T2  + T3........Tn
Find Sn mod (10^9 + 7).

""""
""""
simple explanation: expand: n^2 - (n-1)^2 = n^2 -n^2 +2n-1 = 2n - 1 

Tn= 2n - 1 

sum of n terms of Tn: 2(n(n+1))/2 - n = n^2

just return n^2 for n terms of Tn
"""
# python_3  Time complexity O(1)

n=int(input())

for i in range(n):
    arr=int(input())
    print((arr**2)%((10**9)+7))
    

    
