text_content = "파이썬 프로그래밍 언어 배우기 쉬운 강력한 파이썬 프로그래밍 언어 파이썬"

with open("sample.txt", "w", encoding="utf-8") as f:
    f.write(text_content)

word_count = {}

with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    words = content.split()
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

print("단어 빈도 분석 결과:")
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words:
    print(f"{word}: {count}번")