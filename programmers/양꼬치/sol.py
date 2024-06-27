# 양꼬치 10 인분 -> 음료 무료
# 양꼬치 1인분 12,000원, 음료 1개 2,000원

def solution(n, k):
    ns = n * 12000
    ks = k * 2000
    nk = (n // 10) * 2000
    result = ns + ks - nk
    return result

print(solution(10, 3))
print(solution(64, 6))



# 강사님 식
def solution(n, k):
    food_price = n * 12000
    if n >= 10:
        service = n // 10
        drink_price = (k - service) * 2000
    else:
        drink_price = k *2000
    
    return food_price + drink_price

print(solution(10, 3))
print(solution(64, 6))


# 다른 풀이
def solution(n, k):
    answer = n * 12000 + 2000 * (k - n//10)
    return answer
    
print(solution(10, 3))
print(solution(64, 6))