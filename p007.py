# 동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

# 첫째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다.
# 단, 각각의 자연수는 1 이상 10000 이하의 수로 주어진다
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.
# 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.


# N, M, K를 공백으로 구분하여 입력받기
n,m,k=map(int, input().split())
#N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first=data[n-1] #가장 큰 수
second=data[n-2]#두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m ==0:   #m이 0이라면 반복문 탈출
            break
        result += first
        m-=1    # 더할 때마다 1씩 빼기
    if m==0:    #m이 0이라면 반복문 탈출
        break
    result+=second
    m-=1
print(result)





n,m,k=map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

count = int(m/(k+1))*k
count+=m%(k+1)

result=0
result+=(count)* first
result +=(m-count)*second

print(result)