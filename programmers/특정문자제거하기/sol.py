# 1. replace() 활용
def solution(my_string, letter):
    answer = ''
    answer = my_string.replace(letter, '')
    return answer

print(solution('abcdef', 'f'))
print(solution('BCBdbe', 'B'))

# 2. 
def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer += i
    return answer

print(solution('abcdef', 'f'))
print(solution('BCBdbe', 'B'))