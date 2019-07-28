""""
https://www.hackerrank.com/challenges/halloween-party/problem
"""
"""
Alex is attending a Halloween party with his girlfriend, Silvia. 
At the party, Silvia spots the corner of an infinite chocolate bar (two dimensional, infinitely long in width and length).

If the chocolate can be served only as 1 x 1 sized pieces and Alex can cut the chocolate bar exactly K times. 
What is the maximum number of chocolate pieces Alex can cut and give Silvia?
"""
#python 3 Time complexity O(1)

n=int(input())
for i in range(n):
    k=int(input())
    if k%2==0:
        print((k//2)**2)
    else:
        print((k//2)*((k//2)+1))
