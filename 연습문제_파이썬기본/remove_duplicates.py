numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique_numbers = list(set(numbers))
unique_numbers.sort()

print(f"원본 리스트: {numbers}")
print(f"중복 제거 후: {unique_numbers}")