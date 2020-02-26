# -*- coding: utf8 -*-

# hello.py를 가져와 그 내용을 포함하는 과정에서 hello.py의 본문이 interpreter에 의해 수행된다.
import Feb12hello

new_msg = Feb12hello.msg + "!!!" * 10

if __name__ == "__main__":
    print(new_msg)