#다양한 수로 이러우진 배열이 있을때 주어진 수들을 M번더하여 가장 큰 수를 만드는 법칙
#단, 배열의 특정한 인덱스에 해당하는 수가 K번을 초과하여 더해질 수 없음.
#단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른것으로 간주
#입력예시
#5 8 3
#2 4 5 4 6
#출력예시 : 46

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
