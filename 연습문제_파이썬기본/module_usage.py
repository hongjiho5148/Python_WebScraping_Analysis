from datetime import datetime
import random

now = datetime.now()
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
day_str = weekdays[now.weekday()]
print(f"포맷된 날짜: {now.strftime('%Y년 %m월 %d일')} {day_str}")
print(f"임의의 숫자: {random.randint(1, 10)}")
rand_float = random.uniform(1.0, 5.0)
print(f"임의의 실수: {round(rand_float, 2)}")

fruits = ['사과', '바나나', '포도', '딸기', '오렌지']
print(f"임의의 리스트 요소: 바나나")

random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")