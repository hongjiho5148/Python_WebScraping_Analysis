# 제작한 모듈에서 함수들을 불러옴
import math_operations as mo

circle = mo.get_circle_area(5)
print(f"원의 넓이: {round(circle, 2)}")

rect = mo.get_rect_area(10, 5)
print(f"직사각형 넓이: {rect}")

fact = mo.get_fact(5)
print(f"팩토리얼 5! = {fact}")

gcd = mo.get_gcd(48, 18)
print(f"최대공약수(48, 18) = {gcd}")