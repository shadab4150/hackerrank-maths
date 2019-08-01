""""
A modified Kaprekar number is a positive whole number with a special property. 
If you square it, then split the number into two integers and sum those integers, you have the same value you started with.
"""
"""
https://www.hackerrank.com/challenges/kaprekar-numbers/problem
"""
#python # Time Complexity O(n)

j=int(input())
num=int(input())
arr=[]

for i in  range(j,num+1):
    
    
    k=str(i*i)
    if i==1:
        arr.append(i)
    if len(k)%2==0:
        k1=k[:len(k)//2]
        k2=k[len(k)//2:]
        if (int(k1)+int(k2))==i:
            arr.append(i)
    if len(k)%2==1 and i>1:
        m='0'
        k=m+k
        
        k1=k[:len(k)//2]
        k2=k[len(k)//2:]
        
        if (int(k1)+int(k2))==i:
            arr.append(i)
    
            
        
if len(arr)==0:
    print("INVALID RANGE")
else:
    print(" ".join(str(x) for x in arr))
