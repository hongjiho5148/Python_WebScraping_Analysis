point = (10, 20)
x, y = point
print(f"좌표: x={x}, y={y}")

nums = [1, 2, 3]
a, b, c = nums
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

def sum_all(*args):
    return sum(args)

result = sum_all(10, 20, 30)
print(f"가변 인수의 합: {result}")

def print_info(**kwargs):
    info_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
    print(f"키워드 인수들: {info_str}")

print_info(name="김철수", age=25, city="서울")