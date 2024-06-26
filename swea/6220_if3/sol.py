import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    char = input()

    if char.islower():
        print(f'#{tc} 는 소문자 입니다.')
    else:
        print(f'#{tc} 는 대문자 입니다.')