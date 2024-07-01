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
# 정수 데이터를 문자형태로 전환하여 1234 데이터를 '1', '2', '3', '4', '5' 로 바꿔줌.
# 리스트 형태로 바뀌어 자리가 정해지면 빈 공간 answer에 하나씩 다시 숫자형으로 저장
# 저장하며 더해주면 합 완성.