# MyMagic8Ball

import random
import time

# 기존의 여러 ans 값을 하나의 list에 저장
ans = ["자! 해보세요!", "됐네요, 이 사람아", "뭐라고? 다시 생각해보세요.", "모르니 두려운 것입니다.",
       "칠푼인가요?? 제 정신이 아니군요!", "당신이라면 할 수 있어요!", "해도 그만, 안 해도 그만, 아니겠어요?",
       "맞아요, 당신은 올바른 선택을 했어요."]

print("MyMagic8Ball에 오신 것을 환영합니다.")
val = ""  # val 초기화

while val != 'q':
    question = input("조언을 구하고 싶으면 질문을 입력하고 엔터 키를 누르세요.\n")

    for n in range(4):
        print("고민 중...")
        time.sleep(1)

    choice = random.randint(1, 8)
    answer = ans[choice - 1]    # ans의 index이용하여 answer값 주기

    print(answer)

    val = input("\n\n마치려면 q를, 다시 하려면 엔터를 누르세요.")
