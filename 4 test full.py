1.)

N = int(input())
if N % 2 == 0:
    print("Even")
else:
    print("Odd")
    
2.)

marks = int(input())
if marks >= 35:
    print("Pass")
else:
    print("Fail")
    
3.)

N = int(input())
if N > 0:
    print("Positive")
elif N < 0:
    print("Negative")
else:
    print("Zero")
    
4.)

A, B = map(int, input().split())
if A > B:
    print(A)
else:
    print(B)
    
5.)

age = int(input())
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
    
6.)

year = int(input())
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
    
7.)

N = int(input())
if N % 5 == 0:
    print("Divisible")
else:
    print("Not Divisible")
    
8.)

temp = int(input())
if temp > 30:
    print("Hot")
else:
    print("Cold")
    
9.)

ch = input().lower()
if ch in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")
    
10.)

A, B, C = map(int, input().split())
if A <= B and A <= C:
    print(A)
elif B <= A and B <= C:
    print(B)
else:
    print(C)
    
11.)

marks = int(input())
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 35:
    print("Grade C")
else:
    print("Fail")
    
12.)

signal = input()
if signal == "Red":
    print("Stop")
elif signal == "Yellow":
    print("Wait")
elif signal == "Green":
    print("Go")
    
13.)

CP, SP = map(int, input().split())
if SP > CP:
    print("Profit")
elif SP < CP:
    print("Loss")
else:
    print("No Profit No Loss")
    
14.)

N = int(input())
if N % 3 == 0 and N % 5 == 0:
    print("Yes")
else:
    print("No")
    
15.)
BMI = float(input())
if BMI < 18.5:
    print("Underweight")
elif BMI <= 24.9:
    print("Normal")
else:
    print("Overweight")
















    
