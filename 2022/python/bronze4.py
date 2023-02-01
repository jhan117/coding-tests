# 1297
# TV 크기
# Geometry
# Pythagoras
# Math

D, H, W = map(int, input().split())
# (width + height) * ratio = diagonal line
# ratio = diagonal line / (width + height)
r = (D**2 / (H**2 + W**2))**0.5
print(int(H * r), int(W * r))

# 1330
# 두 수 비교하기
# Implementation
# Arithmetic
# Math

a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")

# 1712
# 손익분기점
# Arithmetic
# Math

a, b, c = map(int, input().split())

if b >= c:
    print(-1)
# using math
# c * x > a + b * x
# cx - bx > a
# (c - b)x > a
# x > a / (c - b)
# x = a / (c - b) + 1
else:
    print(int(a / (c - b) + 1))

# 2480
# 주사위 세개
# Arithmetic
# Math

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a != b != c and a != c:
    if a > b:
        big = a
        if big < c:
            big = c
    else:
        big = b
        if big < c:
            big = c

    print(big * 100)
# or use max function
# max (a, b, c) * 100
else:
    if a == b or b == c:
        same = b
    elif a == c:
        same = a
    print(1000 + same * 100)

# 2525
# 오븐 시계
# Arithmetic
# Math

a, b = map(int, input().split())
c = int(input())

cooked = (a * 60 + b) + c

if cooked // 60 < 24:
    print(cooked // 60, cooked % 60)
else:
    print(cooked // 60 - 24, cooked % 60)

# 2530
# 인공지능 시계
# Arithmetic
# Math

a, b, c = map(int, input().split())
d = int(input())

# 25 / 24 = 24...1
# 25 = 1h
# 25 % 24 = 1
h = (a + ((b + (c + d) // 60) // 60)) % 24
m = (b + (c + d) // 60) % 60
s = (c + d) % 60
print(h, m, s)

# 2588
# 곱셈
# Arithmetic
# Math

Num1 = int(input())
Num2 = input()

print(Num1 * int(Num2[2]))
print(Num1 * int(Num2[1]))
print(Num1 * int(Num2[0]))
# or
i = 2
while i >= 0:
    print(Num1 * int(Num2[i]))
    i -= 1
# or
for i in range(2, -1, -1):
    print(Num1 * int(Num2[i]))

print(Num1 * int(Num2))

# 2752
# 세수 정렬
# Sorting

a, b, c = map(int, input().split())
min = min(a, b, c)
max = max(a, b, c)

if min != a and max != a:
    print(min, a, max)
elif min != b and max != b:
    print(min, b, max)
else:
    print(min, c, max)

# or
n = list(map(int, input().split()))
n.sort()
print(n[0], n[1], n[2])

# 2753
# 윤년
# Arithmetic
# Math

y = int(input())

if y % 4 == 0:
    if y % 100 != 0:
        print(1)
    elif y % 400 == 0:
        print(1)
else:
    print(0)

# 3004
# 체스판 조각
# Math

n = int(input())

if n % 2 == 0:
    print((1 + n // 2) ** 2)
else:
    print((1 + n // 2) * (2 + n // 2))

# 4299
# AFC 윔블던
# Arithmetic
# Math

a, b = map(int, input().split())

if a + b < 0 or a - b < 0:
    print(-1)
elif (a - b) % 2 == 0:
    c = (a + b) // 2
    d = a - c
    print(max(c, d), min(c, d))
else:
    print(-1)

# 5532
# 방학 숙제
# Arithmetic
# Math

import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

s = max(math.ceil(a / c), math.ceil(b / d))
print(l - s)

# 5543
# 상근날드
# Arithmetic
# Math

top = int(input())
middle = int(input())
bottom = int(input())
coke = int(input())
soda = int(input())

print(min(top, middle, bottom) + min(coke, soda) - 50)

# 5575
# 타임 카드
# Implementation
# Arithmetic
# Math

humans = {}
humans["a"] = list(map(int, input().split()))
humans["b"] = list(map(int, input().split()))
humans["c"] = list(map(int, input().split()))

for x in humans:
    y = humans.get(x)
    time = (y[3] * 3600 + y[4] * 60 + y[5]) - (y[0] * 3600 + y[1] * 60 + y[2])

    h = time // 3600
    m = (time - h * 3600) // 60
    s = (time - h * 3600) % 60

    print(h, m, s)

# 5596
# 시험 점수
# Implementation
# Arithmetic
# Math

i, m, s, e = map(int, input().split())
i1, m1, s1, e1 = map(int, input().split())

S = i + m + s + e
T = i1 + m1 + s1 + e1

if S == T:
    print(S)
else:
    print(max(S, T))

# 5893
# 17배
# Implementation
# Arbitrary precision
# Math

n = int(input(), 2)
n *= 17
print(format(n, 'b'))

# 5928
# Contest Timing
# Implementation
# Arithmetic
# Math

d, h, m = map(int, input().split())

endTime = d * 1440 + h * 60 + m
startTime = 11 * (1440 + 60 + 1)

if endTime < startTime:
    print(-1)
else:
    print(endTime - startTime)

# 6763
# Speed fines are not fine!
# Implementation

limit = int(input())
speed = int(input())

over = speed - limit

if over < 1:
    print("Congratulations, you are within the speed limit!")
elif 0 < over < 21:
    print("You are speeding and your fine is $100.")
elif 20 < over < 31:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")

# 6764
# Sounds fishy!
# Implementation

dr1 = int(input())
dr2 = int(input())
dr3 = int(input())
dr4 = int(input())

if dr1 < dr2:
    if dr2 < dr3:
        if dr3 < dr4:
            print("Fish Rising")
        else:
            print("No Fish")
    else:
        print("No Fish")
elif dr1 > dr2:
    if dr2 > dr3:
        if dr3 > dr4:
            print("Fish Diving")
        else:
            print("No Fish")
    else:
        print("No Fish")

elif dr1 == dr2:
    if dr2 == dr3:
        if dr3 == dr4:
            print("Fish At Constant Depth")
        else:
            print("No Fish")
    else:
        print("No Fish")
else:
    print("No Fish")

# OR
if dr1 < dr2 and dr2 < dr3 and dr3 < dr4:
    print("Fish Rising")

# 6778
# Which Alien?
# Implementation

a = int(input())
e = int(input())

if a > 2 and e < 5:
    print("TroyMartian")
if a < 7 and e > 1:
    print("VladSaturnian")
if a < 3 and e < 4:
    print("GraemeMercurian")
