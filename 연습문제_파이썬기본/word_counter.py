sentence = input("문장을 입력하세요: ")

processed_sentence = " ".join(sentence.split())
word_count = len(sentence.split())

print(f"공백 제거: {processed_sentence}")
print(f"단어 개수: {word_count}개")