# 1009
''' 시간 초과
for i in range(t):
    a, b = map(int, input().split())
    l = a ** b % 10
    if l == 0:
        l = 10
    print(l)
'''
'''
밑수의 일의 자리 규칙 사용하기
1. 규칙이 1개인 경우 [0, 1, 5, 6]
2. 규칙이 2개인 경우 [4, 9]
3. 규칙이 4개인 경우 [2, 3, 7, 8]
'''
# t = int(input())
# for i in range(t):
#     a, b = map(int, input().split())
#     base = a % 10

#     if base == 0:               # 규칙 1-1
#         print(10)
#     elif base in [1, 5, 6]:     # 규칙 1-2
#         print(base)
#     elif base in [4, 9]:        # 규칙 2
#         if b % 2 == 1:
#             print(base)
#         else:
#             print(base ** 2 % 10)
#     else:                       # 규칙 3
#         b %= 4
#         if b == 0:
#             print(base ** 4 % 10)
#         else:
#             print(base ** b % 10)

# 1085
# x, y, w, h = map(int, input().split())
# print(min(x - 0, w - x, y - 0, h - y))

# 1212
# n = int(input(), 8)
# print(format(n, 'b'))

# 1247
''' 시간 초과
for i in range(3):
    n = int(input())
    s = 0
    for i in range(n):
        integer = int(input())
        s += integer
    if s < 0:
        print('-')
    elif s > 0:
        print('+')
    else:
        print(0)
'''
'''
빠른 입력
sys.stdin.readline()
for을 같이 쓸 수 있네
'''
# from sys import stdin
# for i in range(3):
#     n = int(stdin.readline())
#     integer = [int(stdin.readline()) for i in range(n)]
#     if sum(integer) < 0:
#         print('-')
#     elif sum(integer) > 0:
#         print('+')
#     else:
#         print(0)

# 1267
'''
(time / 30 + 10) * (time + 1)
(time / 60 + 15) * (time + 1)
'''
# Y = M = 0
# n = int(input())
# time = list(map(int, input().split()))
# for i in time:              # range로 안 해도 된다.
#     Y += i // 30 * 10 + 10  # list 보다는 이게 때로는 코드 단축이 된다...
#     M += i // 60 * 15 + 15
# if Y < M:
#     print("Y", Y)
# elif Y > M:
#     print("M", M)
# else:
#     print("Y M", Y)

# 1284
# while True:
#     n = input()
#     if n == '0':
#         break
#     width = 1 + len(n)
#     for i in n:
#         if i == '1':
#             width += 2
#         elif i == '0':
#             width += 4
#         else:
#             width += 3
#     print(width)

# 1547
# ball = [1, 2, 3]
# M = int(input())
# for i in range(M):
#     X, Y = map(int, input().split())
#     x = ball.index(X)
#     y = ball.index(Y)
#     ball[x], ball[y] = ball[y], ball[x]
# print(ball[0])

# 1598
'''좌표로 접근
원점 = (0, 0)
절댓값 = abs()
'''
# a, b = map(int, input().split())
# a -= 1
# b -= 1
# print(abs(a // 4 - b // 4) + abs(a % 4 - b % 4))

# 1703

# 1837
P, K = map(int, input().split())
