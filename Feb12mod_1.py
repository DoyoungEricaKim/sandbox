# -*- coding: utf8 -*-

def sum(a, b):
    return a + b


def safe_sum(a, b):
    if type(a) != type(b):
        print("서로 다른 자료형입니다")
        return
    else:
        result = sum(a, b)
    return result


if __name__ == "__main__":
    print(safe_sum('a', 1))
    print(safe_sum(2, 3))
    print(sum(3, 4))
