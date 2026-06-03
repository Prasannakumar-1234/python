1.)

n=int(input())
for i in range(n):
    for j in range(n):
        print("*" if i==0 or i==n-1 or j==0 or j==n-1 else " ",end=" ")
    print()

2.)

n=int(input())
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()

3.)

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

4.)

n=int(input())
for i in range(1,n+1):
    print("*"*i+" "*(2*(n-i))+"*"*i)
for i in range(n,0,-1):
    print("*"*i+" "*(2*(n-i))+"*"*i)

5.)

n=int(input())
for i in range(n):
    c=1
    for j in range(i+1):
        print(c,end=" ")
        c=c*(i-j)//(j+1)
    print()

7.)

n=int(input())
for i in range(n):
    for j in range(2*n-1):
        if i==n-1 or j==n-i-1 or j==n+i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

8.)

n=int(input())
for i in range(3):
    for j in range(n):
        print("*" if (i+j)%4==0 or (i==1 and j%4==2) else " ",end="")
    print()

9.)

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print(chr(65+j),end=" ")
    print()

10.)

n=int(input())
for i in range(n):
    for j in range(n):
        print("*" if i==j or i+j==n-1 else " ",end="")
    print()

    
