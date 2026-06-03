1.)

length = int(input())
breadth = int(input())
a = 2 * (length+breadth)
b = (length*breadth)
print(a)
print(b)

3.)
p = int(input())
r = int(input())
y = int(input())

interest = (p * r * y)/100
amount = p + interest
discount = (2 * interest) / 100
final_settlement =amount - discount

print(f"{interest: .2f}")
print(f"{amount: .2f}")
print(f"{discount: .2f}")
print(f"{final_settlement: .2f}")

4.)

a = int(input())
b = int(input())

print(a//b)
print(a%b)

5.)

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2

print(f"{mid_x:.1f} {mid_y:.1f}")

6.)

w = int(input())
x = int(input())
y = int(input())

revenue = w * x
cost = (w * y) + 100

profit = revenue - cost

print(profit)

7.)

w = int(input())
x = int(input())
y = int(input())

revenue = w * x
cost = (w * y) + 100

profit = revenue - cost

print(profit)

8.)

num = int(input())
sum_digits = (num // 10) + (num % 10)
print(sum_digits)


