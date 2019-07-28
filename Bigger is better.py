"""
https://www.hackerrank.com/challenges/bigger-is-greater/problem
"""


# Classic style using recursion take long time and memory for long string

from itertools import permutations

def find(x,y):
    
    k=sorted(list(permutations(sorted(x),int(y))))
    arr=[]
    for i in range(len(k)):
        #print("".join(str(x) for x in k[i]))
        arr.append("".join(k[i]))
    kat=sorted(list(set(arr)))
    man=kat.index(x)
    
    if man==len(arr)-1  or len(kat)==1:
        print("no answer")
    else:
        print(kat[man+1])
    return 1
    
n=int(input())
for i in range(n):
    x=input()
    y=len(x)
    find(x,y)
    

# Best style less time consuming for length of strings

def next(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True

n=int(input())

for i in range(n):
    # input string
    x=list(input())
    
    if next(x): # If True string x has been altered to next string
        print("".join(x))
    else:
        print("no answer")
    
