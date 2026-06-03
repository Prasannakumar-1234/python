1.)

balance = int(input())
if balance > 0:
    print("positive")
elif balnace < 0:
    print("negative")
else:
    print("zero balance")

2.)

token = int(input())
if token % 2 == 0:
     print("even token")
else:
    print("odd token")

3.)

marks = int(input())
if marks >= 35:
    print("pass")
else:
    print("fail")

4.)


A, B = map(int, input().split())

if A > B:
    print("A is costlier")
elif B > A:
    print("B is costlier")
else:
    print("equal prices")

5.)

a, b and c = map(int, input().split())

if a > b and a > c:
    print("player a")
elif b > a and b > c:
    print("player b")
elif c > a and c > b:
    print("player c")
else:
    print("tie")


6.)

ch = input()

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("vowel")
else:
    print("consonant")

7.)

y = int(input())

if (y % 400 == 0) or(y % 4 == 0 and y % 100 != 0):
    print("leap year")
else:
    print("not a leap year")

8.)

age = int(input())
if age > 13:
     print("child")
elif age >= 13 and age <= 19:
    print("Teen")
elif age >= 20 and age <=59:
    print("adult")
else:
    print("senior")

9.)

A, B, op = input().split()

A = int(A)
B = int(B)

if op == '+':
    print(A + B)
elif op == '-':
    print(A - B)
elif op == '*':
    print(A * B)
elif op == '/':
    print(A / B)
else:
    print("invalid operator")

    
10.)

A, B, C= map(int,input().split())

if (A + B > C) and (B + C > A) and (A + C > B):
    print("valid triangle")
else:
    print("invalid triangle")

11.)

m = int(input())

if 90 <= m <= 100:
    print("A")
elif 75 <= m <= 89:
    print("B")
elif 60 <= m <= 74:
    print("C")
elif 35 <= m <= 59:
    print("D")
else:
    print("F")

    
