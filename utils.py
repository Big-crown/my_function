# 한 줄 짜리 주석
"""
따옴표 세 개 사용하면 그 범위 안에 모든 주석임.
"""
"""
코드 작성 일자 : 2024년 6월 12일 스터디
코드 작성자 : 김대관
코드 이름 : utils.py
코드 목적 : 유용한 함수를 따로 저장하여 두고 나중에 불러와 사용하기 위함
"""


def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)

def gugudan(x):
    for i in range(9):
        print((i+1)*x)
