def cal():
    w = int(input("가로 길이를 입력하세요: "))
    l = int(input("세로 길이를 입력하세요: "))
    n1 = w * l
    n2 = 2 * (w + l)
    print(f"직사각형의 넓이: {n1}")
    print(f"직사각형의 둘레: {n2}")

cal()