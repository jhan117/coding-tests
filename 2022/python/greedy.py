# 큰 수의 법칙
# 단순 풀이
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 반복되는 수열 이용
'''
[입력 예시]
5 8 3
2 4 5 4 6
-> 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46

수열
{6 + 6 + 6 + 5}, {6 + 6 + 6 + 5}

가장 큰 수가 들어간 횟수
= 수열 반복 횟수 * 연속으로 더할 수 있는 횟수
= (숫자가 더해질 수 있는 총 길이 // 수열의 길이) * 연속으로 더할 수 있는 횟수
= (숫자가 더해질 수 있는 총 길이 // 연속으로 더할 수 있는 횟수 + 1) * 연속으로 더할 수 있는 횟수
= m // (k + 1) * k

if 수열 반복 횟수에 나머지가 있는 경우,
즉, m이 홀수인 경우에는 나머지만큼 각각 횟수가 더해지므로
+= m % (k + 1)

즉, first number count = (m // (k + 1) * k) + (m % (k + 1))

'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = m // (k + 1) * k + m % (k + 1)
'''OR
count = m // (k + 1) * k
count += m % (k + 1)
'''

result = 0
result += count * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)

# 숫자 카드 게임
# min() 함수 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# 2중 반복문 구조 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001

    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)
