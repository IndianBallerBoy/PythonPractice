# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n,m=tuple(map(int, input().split()))
ns=tuple(map(int, input().split()))
h=set(map(int, input().split()))
s=set(map(int, input().split()))
happiness = 0
for x in ns:
    if x in h:
        happiness+=1
    elif x in s:
        happiness-=1
       

    
    
print(happiness)




'''example input:
3 2
1 5 3
3 1
5 7

output:
1

finds if numbers of A are in big array and adds happiness
finds if numbers of B are in big array and removes one happiness'''


