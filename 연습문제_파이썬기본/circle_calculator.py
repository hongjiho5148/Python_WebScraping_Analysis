import math
def cal():
    r = float(input("원의 반지름을 입력하세요:"))
    n1 = math.pi * (r ** 2)
    n2 = 2 * math.pi * r
    print(f"반지름이 {r}인 원의 넓이: {n1:.2f}")
    print(f"반지름이 {r}인 원의 둘레: {n2:.2f}")
cal()
