""""
https://www.hackerrank.com/challenges/connecting-towns/problem
""""
""""
Gandalf is travelling from Rohan to Rivendell to meet Frodo but there is no direct route from Rohan (T1) to Rivendell (Tn).

But there are towns T2,T3,T4...Tn-1 such that there are N1 routes from Town T1 to T2, 
and in general, Ni routes from Ti to Ti+1 for i=1 to n-1 and 0 routes for any other Ti to Tj for j ≠ i+1

Find the total number of routes Gandalf can take to reach Rivendell from Rohan.

Note 

Gandalf has to pass all the towns Ti for i=1 to n-1 in numerical order to reach Tn. 

For each Ti , Ti+1 there are only Ni distinct routes Gandalf can take.

Input Format 

The first line contains an integer T, T test-cases follow. 
Each test-case has 2 lines. The first line contains an integer N (the number of towns). 
The second line contains N - 1 space separated integers where the ith integer denotes the number of routes, Ni, from the town Ti to Ti+1

Output Format 

Total number of routes from T1 to Tn modulo 1234567 

""""""

# python 3


for i in range(int(input())):
    T=int(input())
    N=list(map(int,input().split()))
    routes=1
    for i in N:
        routes=(routes*i)%1234567
    print(routes)







