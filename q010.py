# 동명이인 찾기
# n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘

def solution(name_list):
    result=set()
    name_list.sort()
    for i in range(0, len(name_list)-1):
        for j in range(i+1, len(name_list)):
            if name_list[i]==name_list[j]:
                result.add(name_list[i])
    return result
name=["Tom","mike","Tom","jerry"]
print(solution(name))



def solution2(name_list):
    for i in range(0, len(name_list)-1):
        for j in range(i+1, len(name_list)):
            print(name_list[i]+"-"+name_list[j])
    return 0

name2=["Tom","mike","jerry"]
solution2(name2)