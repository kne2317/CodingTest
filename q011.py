# 팩토리얼 구하기
# 1부터 n까지 연속한 정수의 곱을 구하는 알고리즘

def solution(n):
    answer=1
    for i in range(1,n+1):
        answer*=i
    return answer

print(solution(1))
print(solution(5))
print(solution(10))


#재귀함수
def solution2(n):
    if n<=1:
        return 1
    return n* solution2(n-1)

print(solution2(1))
print(solution2(5))
print(solution2(10))


def solution3(n):
    if n<=1:
        return 1
    return n + solution3(n-1)

print(solution3(1))
print(solution3(5))
print(solution3(10))

