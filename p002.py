# 1부터 n까지 연속한 정수의 합을 구하는 알고리즘 만들기
# 1부터 10까지의 수를 모두 더하면 55
# 1부터 100까지의 수를 모두 더하면 5050



# 계산 복잡도 O(n)
def function(a):
    sum=0
    for i in range(1, a+1):
        sum+=i

    return sum

print(function(10))
print(function(100))




# 계산 복잡도 O(1)
def function2(a):
    return a * (a+1)//2



print(function2(10))
print(function2(100))


# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for 반복문으로 만들자


# 계산 복잡도 O(n)
def function3(n):
    sum=0

    for i in range(1, n+1):

        sum+=i*i

    return sum

print(function3(10))


# 계산 복잡도 O(1)
def function4(n):
    return n*(n+1)*(2*n+1)//6


print(function4(10))