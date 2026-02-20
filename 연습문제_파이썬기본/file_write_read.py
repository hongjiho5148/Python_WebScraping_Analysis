# 1. 파일에 저장할 내용 입력받기
lines = []
print("파일에 저장할 내용 (3줄 입력):")
for _ in range(3):
    lines.append(input())

# 2. 파일 쓰기
with open("test.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

# 3. 파일 읽기 
print("\n파일에서 읽어온 내용:")
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)