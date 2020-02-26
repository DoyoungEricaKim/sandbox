# hw0226
import random
import time

print("반갑습니다. 최첨단 인공지능 대화로봇을 지향만합니다.")
answer = ["자! 해보세요!", "됐네요, 이 사람아", "뭐라고? 다시 생각해보세요.", "모르니 두려운 것입니다.",
          "칠푼인가요?? 제 정신이 아니군요!", "당신이라면 할 수 있어요!", "해도 그만, 안 해도 그만, 아니겠어요?",
          "맞아요, 당신은 올바른 선택을 했어요.", "숙제가 참 쉽죠", "누가 챗봇소리를 내었는가"]
val = ""

while True:
    print("아무거나 물어보세요~")
    val = input()
    val = val.casefold()    # 입력된 값을 소문자로 변경
    val = val.strip()       # 입력된 값에서 공백 제거

    if val == "quit":       # 첫번째 while문에서 입력이 quit일 경우 종료
        input("\n엔터치면 마칩니다.")
        break
    elif val == "":         # 입력이 없을 경우
        print("에이~ 그러지 말고 아무말이나 해봐요")
    else:
        choice = random.randint(1, 10)  # 1~10 사이의 랜덤 값 구하기
        print("제 대답은요...", end='')  # print 후 개행 없애기
        time.sleep(1)                   # 1초 정지
        print(".", end='')
        time.sleep(1)
        print(".", end='')
        time.sleep(1)
        print(answer[choice-1])         # list의 index를 활용하여 랜덤한 답변 출력

