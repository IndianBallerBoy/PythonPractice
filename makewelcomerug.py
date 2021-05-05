# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input().split(' ')

length = int(s[0])
width = int(s[1])

i = 0
minus3 = int((width - 3)/2)


for i in range(0, (length-1)//2):
    
    print(('-'*minus3) + ('.|.'*(i+1)) + ('.|.'*(i)) + ('-'*minus3))
    minus3 = minus3-3
    x = i

print(((width - 7)//2)*'-' + 'WELCOME' + ((width - 7)//2)*'-')
minus3 = minus3+3
for i in range(0, (length-1)//2):
    
    print(('-'*minus3) + ('.|.'*(x)) + ('.|.'*(x+1)) + ('-'*minus3))
    minus3 = minus3+3
    x = x-1