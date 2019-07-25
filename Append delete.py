"""
https://www.hackerrank.com/challenges/append-and-delete/problem
"""

"""
You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:

Append a lowercase English alphabetic letter to the end of the string.
Delete the last character in the string. Performing this operation on an empty string results in an empty string.
""""
# python 3

def appenddelete(s1,s2,n):    
    count=0
    for i in range(len(s2)):
        if s1[i]==s2[i]:
            count+=1
        else:
            break
    if s1==s2:
        min=0
    else:
        min=(len(s1)-count)+(len(s2)-count)
    if n>=min:
        print("Yes")
    else:
        print("No")
        
    return 1  

def appenddelete1(s1,s2,n):    
    count=0
    for i in range(len(s2)):
        if s1[i]==s2[i]:
            count+=1
        else:
            break
    if s1==s2:
        min=0
    else:
        min=(len(s1)-count)+(len(s2)-count)
    if len(s1)>n>=min or n>(len(s1)+len(s2)):
        print("Yes")
    else:
        print("No")
        
    return 1  

s=input()
t=input()
n=int(input())



if len(s)>=len(t):
    appenddelete(s,t,n)
else:
    appenddelete1(t,s,n)
    
