# 1번 입력된 정수 n의 자릿수 더하기

# 1. 10으로 나누어 몫이 0이 될때까지 반복
def solution(n):
    answer = 0
    while n > 0:
        # a: 몫, b: 나머지
        a, b = divmod(n, 10)
        n = a
        answer += b
    return answer
print(solution(1234))
print(solution(930211))


# 2. 형변환 후 풀기
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer
print(solution(1234))
print(solution(930211))