"""
https://www.hackerrank.com/challenges/sherlock-and-divisors/problem
"""
"""
Watson gives an integer N  to Sherlock and asks him: 
What is the number of divisors of N that are divisible by 2?.
"""
# Time Complexity O(N)

n=int(input())
for i in range(n):
    num=int(input())
    count=0
    for i in range(1,(num//2)+1):
        if num%i==0 and i%2==0:
            
            count+=1
    if num%2==0:
        count+=1
    print(count)


# Time Complexity  O(n^(1/2))

import math

def divisors(n):
    count = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0 and i%2==0:
            # i is even
            count+=1
        if n%(n//i)==0 and (n//i)%2==0:
            # n//i is even and n's factor
            count+=1
        if i*i==n and i%2==0:
            # if i is sqrt reduce by 1
            count-=1
    return count


n=int(input())
for i in range(n):
    num=int(input())
    print(divisors(num))
