1.)

 n = int(input())
if n < 10:
    print("slow")
elif n >= 10 and n <= 49:
    print("moderate")
else:
    print("fast")

2.)

 n = int(input())
if n >= 0 and n<= 10:
    print("critical")
elif n >= 11 and n <= 30:
    print("low battery")
else:
    print("battery ok")

3.)

n = int(input())
if n%100 == 0:
    print("Transaction allowed")
else:
    print("invalid amount")

4.)

n = int(input())

if n < 15:
    print("cold")
elif n >= 15 and n <= 30:
    print("normal")
else:
    print("hot")

5.)

age = int(input())

if age < 18:
    print("not allowed")
else:
    print("allowed")

6.)

n = int(input())

if n >= 999:
    print("free delivery")
else:
    print("delivery charges apply")

7.)

n = input()

if n.isalpha():
    print("alphabet")
elif n.isdigit():
    print('number")
else:
    print("special charater")

8.)

a = int(input()
b = int(input()

if a > b:
        print("team a win ")
elif a == b:
    print("match draw")
else:
    print("team b win")

9.)

n  = int(input())
if n >= 5:
    print("bonus eligible")
else:
    print(" not eligible")

10.)

n = int(input())

if n < 6:
    print("weak password")
else:
    print("strong password")


11.)

n = input()
if n == red:
    print("stop")
elif n == yellow:
    print("ready")
elif n == green:
    print("go")
else:
    print("invalid signa")


12.)

n  = int(input())

if n >=1 and n <=100:
    print("small")
elif n >=101 and n <= 1000:
    print("medium")
else:
    print("large")

13.)

n = int(input())

if n >= 1 and n <= 2:
    print("small table")
elif n >= 3 and n <= 6:
    print("family table")
else:
    print("party hall")

14.)

n  = int(input())

if n == 100:
    print("tank full")
elif n >= 50 and n <=99:
    print("tank stable")
elif n < 50:
    print("refill needed")

15.)

n = input()
if n == "school" or n == "college":
    print("eligible")
else:
    print("not eligible")

16.)

n = int(input())
if n >= 6 and n <= 11:
    print("breakfast")
elif n >= 12 and n <= 16:
    print("lunch")
elif n >= 17 and n <= 22:
    print("dinner")
else:
    print("closed")
    
