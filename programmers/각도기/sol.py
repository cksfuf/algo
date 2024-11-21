def solution(angle):
    if angle == 180:
        return 4
    elif angle > 90:
        return 3
    elif angle == 90:
        return 2
    else:
        return 1

# 4: 평각, 3: 둔각, 2: 직각, 1: 예각

# 더 짧게 가능
def solution(angle):
    if angle<=90:
        return 1 if angle<90 else 2
    else:
        return 3 if angle<180 else 4