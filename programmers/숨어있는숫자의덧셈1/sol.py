# 1번
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit(): # isdigit()은 숫자열이 비어있으면 False를 반환
            answer += int(i)
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))```

# 주어진 n에는 숫자와 문자가 합쳐진 문자형 데이터
# 숫자만 합하기 위해 isdigit method 활용
    # isdigit은 숫자열이 아니라면 False 즉, 0을 반환
# n에 들어온 데이터 중 문자는 0 값을, 숫자는 숫자형으로 변환되어 answer 공간에 저장되어 더해짐.
# 결과값 도출.

# 2번
def solution(my_string):
    answer = 0
    for i in my_string:
        if ord('1') <= ord(i) <= ord('9'):
            answer += int(i) 
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))