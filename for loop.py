14.)
n = int(input())
for i in range(1,n + 1):
    for j in range(1,i + 1):
        print(j,end=" ")
    print()
12.)   
n = int(input())
if n > 1:
    for i  in range(2,n):
        if n%i == 0:
            print("not prime")
            break
        else:
            print("prime")
    else:
        print("not prime")
11.)
n = int(input())
for i in range(1,n+1):
    if n%i == 0:
        print(i,end=" ")

4.)
n = int(input())
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    
3.)
n = int(input())
k = 0
for i in range(1,n+1):
    k = k + i
    print(k,end= " ")
    
7.)s
n = int(input())
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n //10
print(reverse)
