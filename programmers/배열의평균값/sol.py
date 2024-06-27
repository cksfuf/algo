# 내 풀이
def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    return answer/len(numbers)

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))


# 강사님 풀이
def solution(numbers):
    answer = 0

    total = 0
    i = 0
    for number in numbers:
        total += number
        i += 1
    answer = total / i
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))

# 다른사람 풀이
def solution(numbers):
    return sum(numbers) / len(numbers)