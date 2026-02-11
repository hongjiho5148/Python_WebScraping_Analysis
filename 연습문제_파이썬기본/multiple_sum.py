s = []
for i in range(1,101):
    if i % 3 == 0:
        s.append(i)
print(f"1부터 100까지 3의 배수: {s}")
print(f"3의 배수의 합: {sum(s)}")
print(f"3의 배수의 개수: {len(s)}개")