import os
import sys

# 1. 시스템 및 작업 환경 정보 (os, sys)
print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"Python 버전: {sys.version}")
print(f"운영체제: {os.name}")

# 환경 변수 PATH 중 앞부분 일부만 출력
path_env = os.environ.get('PATH', '')
print(f"환경 변수 PATH 일부: {path_env[:50]}...")

# 2. 파일 경로 다루기 (os.path)
full_path = "/Users/username/documents/report.txt"

# 경로 분리 (디렉토리와 파일명)
dirname = os.path.dirname(full_path)
filename = os.path.basename(full_path)
# 파일명과 확장자 분리
name, ext = os.path.splitext(filename)

print("파일 경로 정보:")
print(f"- 디렉토리: {dirname}")
print(f"- 파일명: {filename}")
print(f"- 확장자: {ext}")

# 파일 존재 여부 확인
print(f"파일 존재 여부: {os.path.exists(full_path)}")