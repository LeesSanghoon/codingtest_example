
#각 자리 숫자로만 이루어진 문자열 S가 주어졌을때 왼쪽부터 오른쪽으로 하나씩 모든숫자를 확인하며
#숫자 사이에 *혹은 + 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰수를 구하는 프로그램
#단 모든 연산은 사칙연산을 무시하고 왼쪽에서 부터 순서대로 이러진다고 가정

s = input()

result = int(s[0])

for i in range (1, len(s)) :
  num = int(s[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)
