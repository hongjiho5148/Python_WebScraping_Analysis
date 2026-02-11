score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
status = "성인" if age >= 20 else "미성년자"
print(f"나이: {age}, 상태: {status}")

numbers = [12, 42, 8, 23, 5]
max_value = numbers[0]
for num in numbers:
    max_value = num if num > max_value else max_value

print(f"숫자들의 최대값: {max_value}")

mixed_numbers = [-3, 5, -1, 12, 8, -7, 23]
positive_numbers = [num for num in mixed_numbers if num > 0]

print(f"양수들: {positive_numbers}")