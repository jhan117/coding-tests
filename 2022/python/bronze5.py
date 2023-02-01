# 1000
# A + B
# Arithmetic
# Implementation
# Math

a, b = input().split()
print(int(a) + int(b))

# 1001
# A - B
# Arithmetic
# Implementation
# Math

a, b = input().split()
print(int(a) - int(b))

# 1271
# 엄청난 부자 2
# Arbitrary precision
# Arithmetic
# Math

n, m = input().split()
n = int(n)
m = int(m)
print(n // m)
print(n % m)

# 1550
# 16진수
# Implementation
# Math

n = int(input(), 16)
print(n)

# 2338
# 긴 자리 계산
# Arbitrary precision
# Arithmetic
# Math

a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)

# 2475
# 검증 수
# Arithmetic
# Implementation
# Math

a, b, c, d, e = input().split()
n = (int(a) ** 2 + int(b) ** 2 + int(c) ** 2 + int(d) ** 2 + int(e) ** 2) % 10
print(n)

# 2557
# Hello World
# Implementation

print("Hello World!")

# 2558
# A+B - 2
# Arithmetic
# Implementation
# Math

# 입력 잘못 봐서 시도 몇 번 함 ㅎㅎ
a = int(input())
b = int(input())
print(a+b)

# 2845
# 파티가 끝나고 난 뒤
# Arithmetic
# Implementation
# Math

l, p = input().split()
a, b, c, d, e = input().split()
n = int(l) * int(p)
print(int(a) - n, int(b) - n, int(c) - n, int(d) - n, int(e) - n)

# 2914
# 저작권
# Arithmetic
# Implementation
# Math

A, I = input().split()
n = int(A) * (int(I)-1) + 1
print(n)

# 3003
# 킹, 퀸, 룩, 비숍, 나이트, 폰
# Arithmetic
# Implementation
# Math

K, Q, L, B, N, P = input().split()
print(1 - int(K), 1 - int(Q), 2 - int(L), 2 - int(B), 2 - int(N), 8 - int(P))

# 3046
# R2
# Arithmetic
# Implementation
# Math

R1, S = input().split()
R2 = 2 * int(S) - int(R1)
print(R2)

# 5337
# Welcome
# Implementation

print(".  .   .")
print("|  | _ | _. _ ._ _  _")
print("|/\|(/.|(_.(_)[ | )(/.")

# 5338
# Microsoft Logo
# Implementation

print("       _.-;;-._")
print("'-..-'|   ||   |")
print("'-..-'|_.-;;-._|")
print("'-..-'|   ||   |")
print("'-..-'|_.-''-._|")
# or
print("""       _.-;;-._
'-..-'|   ||   |
'-..-'|_.-;;-._|
'-..-'|   ||   |
'-..-'|_.-''-._|""")
# or
a = """       _.-;;-._
'-..-'|   ||   |
'-..-'|_.-;;-._|
'-..-'|   ||   |
'-..-'|_.-''-._|"""
print(a)


# 5339
# 콜센터
# Implementation

# backslash -> Use a raw string : r"\"
print(r"     /~\ ")
print("    ( oo|")
print("    _\=/_")
print(r"   /  _  \ ")
print(r"  //|/.\|\\")
print(" ||  \ /  ||")
print("============")
print("|          |")
print("|          |")
print("|          |")
# or
print(r"""     /~\
    ( oo|
    _\=/_
   /  _  \
  //|/.\|\\
 ||  \ /  ||
============
|          |
|          |
|          |""")

# 5522
# 카드 게임
# Arithmetic
# Math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(a + b + c + d + e)

# 5554
# 심부름 가는 길
# Arithmetic
# Implementation
# Math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

s = a + b + c + d
x = s // 60
y = s % 60

print(x)
print(y)

# 6749
# Next in line
# Arithmetic
# Math

y = int(input())
m = int(input())

print(m + (m - y))


# 7287
# 등록
# Implementation

print(18)
print("jhan117")

# 8370
# Plane
# Arithmetic
# Math

n1, k1, n2, k2 = input().split()

s = int(n1) * int(k1) + int(n2) * int(k2)
print(s)
