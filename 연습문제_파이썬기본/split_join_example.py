text = "Python is awesome programming language"

words = text.split()
hyphen_text = "-".join(words)
upper_words = [word.upper() for word in words]
upper_text = " ".join(upper_words)

# 결과 출력
print(f"원본 문자열: {text}")
print(f"분리된 단어들: {words}")
print(f"하이픈으로 연결: {hyphen_text}")
print(f"대문자로 변환 후 공백으로 연결: {upper_text}")