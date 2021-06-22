n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2]

#가장큰수가 더해지는 횟수 계싼
count = int(m / (k +1)) * k
count += m % (k+1)

result = 0
result += count * first #가장큰수 더하기
result += (m - count) * second #두번째로 큰 수 더하기

print(result)
