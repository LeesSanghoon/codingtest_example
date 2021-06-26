#어떠한 수 N이 1이 될 때 까지 다음의 두과정중 하나를 반복적으로
#선택하여 수행하려고 함. 단 두번째 연산은 N이 K로 나누어
#떨어질때만 가능합니다.
#1.N에서 1을 뺍니다
#2.N을 K로 나눕니다.

n, k = map(int,input().split())

result = 0

while True:
  #N이 K로 나누어 떨어지는수가 될때 까지 빼기
  target = (n//k) * k
  result += (n-target)
  n = target
  if n<k:
    break
  result += 1
  n //= k

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
