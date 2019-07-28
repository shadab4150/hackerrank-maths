"""""
https://www.hackerrank.com/challenges/encryption/problem
""""
#python 3 Time Complexity O(n)


import math
s=input()
l=math.sqrt(len(s))
row=int(math.floor(l))
col=int(math.ceil(l))
arr=[]
for i in range(0,len(s),col):
    arr.append(s[i:i+col])
j=0
i=0 
arr1=[]  
while j<len(arr[i]):
    arr2=[]
    
    for i in range(len(arr)):
        arr2.append(arr[i][j])
        
    arr1.append(arr2)
    j+=1
man=len(arr[-1])
j=man
i=0
while j<len(arr[i]):
    arr3=[]
    for i in range(len(arr)-1):
        arr3.append(arr[i][j])
    arr1.append(arr3)
    j+=1 
arr4=[]      
for i in arr1:
    arr4.append("".join(i))
print(" ".join(arr4))
