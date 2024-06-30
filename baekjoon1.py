# 백준 1000번
n, k = map(int, input().split())
print(n + k)

# 백준 1001번
n, k = map(int, input().split())
print(n - k)

# 백준 10998번
n, k = map(int, input().split())
print(n * k)

# 백준 10926번
data = input()
print(data + "??!")

# 백준 10430번
a, b, c = map(int, input().split())
print((a + b)%c)
print(((a%c) + (b%c))%c)
print(((a*b)%c))
print(((a%c)*(b%c))%c)

# 백준 2588번
n = int(input())
k = input()

print(n * int(k[-1]))
print(n * int(k[1]))
print(n * int(k[0]))
print(n * int(k))

# 백준 11382번
n, m, k = map(int, input().split())
print(n + m + k)

# 백준 10171번
print("\\    /\\")
print(" )  ( \')")
print("(  /  )")
print(" \\(__)|")

# 백준 10172번
print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")

# 백준 1330번
a, b = map(int, input().split())

if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")


# 백준 9498번
n = int(input())

if n >= 90:
    print("A")
elif n >= 80:
    print("B")
elif n >= 70:
    print("C")
elif n >= 60:
    print("D")
else:
    print("F")


# 백준 2753번
n = int(input())

if (n % 4) == 0 and (n % 100) != 0:
    print(1)
elif (n % 400) == 0:
    print(1)
else:
    print(0)

# 백준 14681번
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y > 0:
    print(2)
else:
    print(3)

# 백준 2884번
h, m = map(int, input().split())

if m >= 45:
    print(h, m - 45)
else:
    if h == 0:
        print(23, 60 - (45 - m))
    else:
        print(h-1, 60 - (45 - m))

# 백준 2525번
h, m  = map(int, input().split())
n = int(input())
a = (m + n) // 60
b = (m + n) % 60

if m + n < 60:
    print(h, m + n)
else:
    if h + a >= 24:
        print((h + a) % 24, b)
    else:
        print(h + a, b)

# 백준 2480번
a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + (a * 1000))
elif b == c:
    print(1000 + (b * 100))
elif a == b or a == c:
    print(1000 + (a * 100))
else:
    print(100 * max(a, b, c))

# 백준 2739번
n = int(input())

for i in range(1, 9 + 1):
    print(f"{n} * {i} = {n * i}")

# 백준 10950번
n = int(input())

for i in range(n):
    n, k = map(int, input().split())
    print(n + k)

# 백준 8393번
n = int(input())
sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)

# 백준 25304번
x = int(input())
n = int(input())
sum = 0

for i in range(n):
    a, b = map(int, input().split())
    sum += (a * b)

if sum == x:
    print("Yes")
else:
    print("No")

# 백준 25314번
n = int(input())
sum = ""
for i in range(n // 4):
    sum += "long "

print(sum + "int")

# 백준 15552번
import sys

input = sys.stdin.readline
n = int(input())

for i in range(n):
    n, k = map(int, input().split())
    print(n + k)

# 백준 11021번
n = int(input())

for i in range(1, n + 1):
    n, k = map(int, input().split())
    print(f"Case #{i}: {n + k}")

# 백준 11022번
n = int(input())

for i in range(1, n + 1):
    n, k = map(int, input().split())
    print(f"Case #{i}: {n} + {k} = {n + k}")

# 백준 2438번
n = int(input())
sum = "*"

for i in range(n):
    print(sum)
    sum += "*"

n = int(input())
for i in (1, n + 1):
    print("*" * i)

# 백준 2439번
n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i) + ("*" * i))

# 백준 10952번
while 1:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    else:
        print(n + k)

# 백준 10951번
while 1:
    try:
        n,k = map(int, input().split())
        print(n + k)
    except:
        break

# 백준 10807번
n = int(input())
data = list(map(int, input().split()))
k = int(input())
print(data.count(k))

# 백준 10871번
n, x = map(int, input().split())
data = list(map(int, input().split()))
a = []
for i in data:
    if i < x:
        a.append(i)
   
print(*a)

# 백준 10818번
n = int(input())
data = list(map(int, input().split()))
data.sort()
print(data[0], data[-1])

print(f"{data[0]} {data[-1]}")

# 백준 2562번
a = []
for i in range(9):
    n = int(input())
    a.append(n)

print(max(a))
print(a.index(max(a)) + 1)

# 백준 10810번
n, m = map(int, input().split())
data = [0 for i in range(1, n + 1)]

for _ in range(1, m + 1):
    i, j, k = map(int, input().split())
    for a in range(i, j + 1):
        data[a-1] = k

print(*data)

# 백준 10813번
n, m = map(int, input().split())
data = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    data[i-1], data[j-1] = data[j-1], data[i-1]

print(*data)

# 백준 5597번

# 백준 3052번

# 백준 10811번

# 백준 1546번
n = int(input())
data = list(map(int, input().split()))

m = max(data)
outcome = [(i/m)*100 for i in data]

print(sum(outcome)/n)

# 백준 27866번
s = input()
print(s[int(input()) - 1])

# 백준 2743번
print(len(input())) 

# 백준 9086번
n = int(input())
for i in range(n):
    s = input()
    print(s[0] + s[-1])

# 백준 11720번
import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input()))

print(sum(s))

# 백준 2675번
n = int(input())
for i in range(n):
    r, s = input().split()
    for i in s:
        print(i * int(r), end="")
    print()

# 백준 10809번
s = input()
data = "abcdefghijklmnopqrstuvwxyz"
for _ in data:
    if _ in s:
        print(s.index(_), end=" ")
    else:
        print(-1, end=" ")

# 백준 1152번
data = input().split()
print(len(data))

# 백준 2908번
n, k = input().split()
n = int("".join(reversed(n)))
k = int("".join(reversed(k)))

if n > k:
    print(n)
else:
    print(k)

# 백준 5622번
data = ["ABC", "DEF", "GHI", "JKL", "MNO", "QRS", "TUV", "WXYZ"]

# 백준 11718번

while 1:
    try:
        s = input()
        print(s)
    except:
        break

# 백준 3003번
data = [1, 1, 2, 2, 2, 8]

n = list(map(int, input().split()))

s = [data[i] - n[i] for i in range(6)]
print(*s)


    















    

