# 최댓값 찾기
# 주어진 숫자 n개 중 가장 큰 숫자를 찾는 알고리즘 만들기

li = [17, 92, 18, 33, 58, 7, 33, 42]


def function():
    max_num = li[0]
    for i in range(1, len(li)):
        if max_num < li[i]:
            max_num = li[i]

    return max_num


print(function())


# 리스트에 숫자가 n개 있을 때 가장 큰 값이 있는 위치 번호를 돌려주는 알고리즘

def function1():
    max_num = 0
    index = 0
    for i in range(0, len(li)):
        if max_num < li[i]:
            max_num = li[i]
            index = i

    return index


print(function1())


# 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램

def function2(minli):
    min_num = minli[0]
    for i in range(1, len(li)):
        if min_num > minli[i]:
            min_num = minli[i]
    return min_num

print(function2(li))