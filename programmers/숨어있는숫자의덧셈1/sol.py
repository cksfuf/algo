# 1번
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit(): # isdigit()은 숫자열이 비어있으면 False를 반환
            answer += int(i)
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))


# 2번
def solution(my_string):
    answer = 0
    for i in my_string:
        if ord('1') <= ord(i) <= ord('9'):
            answer += int(i) 
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))