n = 7
for i in range(n):
    for j in range(2*n-1):
        if(j==n-i-1 or j==n+i-1 or(i==n//2 and n-i-1<j<n+i-1)):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()        





d = 7
a = 5

for i in range(d):
    for j in range(a):
        if j == 0 or (j == a - 1 and i != 0 and i != d - 1) or (i == 0 or i == d - 1) and j < a - 1:
            print("D", end="")
        else:
            print(" ", end="")
    print()  



n = 11  
for i in range(n):
    for j in range(n):
        if j == 0 or i + j == n // 2 or i - j == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print() 



ch = 65
n  = 5
for i in range(1,n+1):
    for j in range(ch,ch+i):
        print(chr(j),end = " ")
    print()    



ch = 65
n  = 5
for i in range(1,n+1):
    for j in range(ch,ch+i):
        print(chr(j),end = " ")
    print()    
    
ch = 65
n  = 5
for i in range(5,0,-1):
    for j in range(ch,ch+i):
        print(chr(j),end = " ")
    print()        
