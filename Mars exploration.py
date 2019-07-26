"""
https://www.hackerrank.com/challenges/mars-exploration/problem
"""

# python 3 Time complexity O(1)



s=input()
Tcount=0
for i in range(0,len(s),3):
    print(s[i:i+3])
    count=0
    if s[i]!='S':
        count+=1
    if s[i+1]!='O':
        count+=1
    if s[i+2]!='S':
        count+=1
    Tcount+=count
    print("Msg Part:"+str((i//3)+1)+" |Total Error Count:"+str(count))
print("Total Errors:"+str(Tcount))
