1.)

n = int(input())
arr = list(map(int, input().split()))

print(sum(arr))

2.)

n = int(input())
arr = list(map(int, input().split()))

print(max(arr))

3.)

n = int(input())
arr = list(map(int, input().split()))

count = 0
for i in arr:
    if i % 2 == 0:
        count += 1

print(count)

4.)

n = int(input())
arr = list(map(int, input().split()))

for i in arr[::-1]:
    print(i, end=" ")

5.)

 n = int(input())
arr = list(map(int, input().split()))
target = int(input())

if target in arr:
    print("FOUND")
else:
    print("NOT FOUND")

6.)

n = int(input())
arr = list(map(int, input().split()))

total = 0
for i in arr:
    if i % 2 != 0:
        total += i

print(total)

7.)

n = int(input())
arr = list(map(int, input().split()))

unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print(*unique)

8.)

n = int(input())
arr = list(map(int, input().split()))

unique = list(set(arr))

if len(unique) < 2:
    print("NO SECOND LARGEST")
else:
    unique.sort(reverse=True)
    print(unique[1])
