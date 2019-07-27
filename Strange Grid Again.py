"""
https://www.hackerrank.com/challenges/strange-grid/problem
""""

""""
A strange grid has been recovered from an old book. It has 5 columns and infinite number of rows. 
The bottom row is considered as the first row. First few rows of the grid are like this:

..............

..............

20 22 24 26 28

11 13 15 17 19

10 12 14 16 18

 1  3  5  7  9

 0  2  4  6  8
The grid grows upwards forever!

Your task is to find the integer in C th column in R th row of the grid.

""""



#python 3 Time Complexity O(1)

r,c=[int(x) for x in input().split()]

def strangegrid(r,c):
    
    arr=[]
    
    if r%2==1:

        r=(r//2)
        
        for j in range(0,10,2):
                
            arr.append((r*10)+j)
        
                
    elif r%2==0:
        
        r=(r//2)-1
        
        for j in range(0,10,2):
            
            arr.append((r*10)+j+1)
    
    return print(arr[c-1])
       
strangegrid(r,c)
