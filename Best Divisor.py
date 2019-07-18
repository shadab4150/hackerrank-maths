""""
https://www.hackerrank.com/challenges/best-divisor/problem
"""
"""""
Kristen loves playing with and comparing numbers. 
She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. 
If the sum of digits is equal for both numbers, then she thinks the smaller number is better. 
For example, Kristen thinks that 13 is better than 31 and that 12 is better than 11 .

Given an integer, N , can you find the divisor of N that Kristin will consider to be the best?
"""""
"""""
constraints 1<n<10^5
""""""


#python 3

n=int(input())
arr=[]
for i in range(1,n+1):
    if n%i==0:
        arr.append(i)
arr2=[int(x) for x in arr  if x<=9 ]
arr3=[int(x) for x in arr  if x>9 ]

def sum_digit(num):
    tot=0
    while(num>0):
        dig=num%10
        tot=tot+dig
        num=num//10
    return tot


k=max(arr2)
arr4=[]
for i in range(len(arr3)):
    
    man=sum_digit(arr3[i])
    if man>k:
        k=man
        arr4.append(arr3[i])
 
    

if len(arr4)==0:
    print(max(arr2))
else:
    print(max(max(arr4),max(arr2)))

#python one liner time comp O(n)

n=int(input())
print(max((d for d in range(1, n+1) if n%d == 0), key=lambda x: sum(map(int, str(x)))))
