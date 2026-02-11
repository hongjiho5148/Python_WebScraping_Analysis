list1 = [2, 4, 6, 8, 10]
all_even1 = all(num % 2 == 0 for num in list1)
any_greater1 = any(num > 10 for num in list1)

print(f"숫자 리스트: {list1}")
print(f"모든 수가 짝수인가? {all_even1}")
print(f"하나라도 10보다 큰 수가 있는가? {any_greater1}")

print()

list2 = [1, 3, 5, 7, 12]
all_even2 = all(num % 2 == 0 for num in list2)
any_greater2 = any(num > 10 for num in list2)

print(f"숫자 리스트2: {list2}")
print(f"모든 수가 짝수인가? {all_even2}")
print(f"하나라도 10보다 큰 수가 있는가? {any_greater2}")