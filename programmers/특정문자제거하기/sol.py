# 1. replace() 활용
def solution(my_string, letter):
    answer = ''
    answer = my_string.replace(letter, '')
    return answer

print(solution('abcdef', 'f'))
print(solution('BCBdbe', 'B'))

# 하나의 문자열 데이터 수정하는 method인 replace를 활용
# 수집된 n이라는 문자열에서 j라는 문자를 공백으로 처리하는 코드 작성.
# 빈공간 acswer에 수정하는 데이터 할당
# 할당된 answer 추출하는 함수 작성.


# 2. 
def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer += i
    return answer
print(solution('abcdef', 'f'))
print(solution('BCBdbe', 'B'))