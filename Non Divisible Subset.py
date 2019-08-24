"""
https://www.hackerrank.com/challenges/non-divisible-subset/problem
"""
"""
Short Problem Definition:
Given a set S of n distinct integers, print the size of a maximal subset S’ of S. 
Where the sum of any 2 numbers in S’ are not evenly divisible by k.
"""

# Python 3 Time Complexity O(n+k)

from collections import Counter

n,k=[int(x) for x in input().split()]
arr=list(map(int,input().split()))

def max_subset(arr,k):

    dog=[x%k for x in arr]
    count=Counter(dog)
    total=[]

    if k%2==1:

        for i in range(1,(k//2)+1):
            total.append(max(count[i],count[k-i]))

        if count[0]>0:
            total.append(1)

    else:

        for i in range(1,k//2):
            total.append(max(count[i],count[k-i]))

        if count[0]>0:
            total.append(1)

        if count[k//2]>0:
            total.append(1)
    
    return sum(total)

print(max_subset(arr,k))
    
