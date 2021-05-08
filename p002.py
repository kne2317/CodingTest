# 1부터 n까지 연속한 정수의 합을 구하는 알고리즘 만들기
# 1부터 10까지의 수를 모두 더하면 55
# 1부터 100까지의 수를 모두 더하면 5050

def function(a):
    sum=0
    for i in range(1, a+1):
        sum+=i

    return sum

print(function(10))
print(function(100))

def function2(a):
    return a * (a+1)//2



print(function2(10))
print(function2(100))