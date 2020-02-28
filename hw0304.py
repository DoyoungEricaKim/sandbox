import random

com_num = random.randint(100, 999)
count = 0


def compare(a, b):  # 두 수의 크기 비교
    if a == b:
        return 2
    elif a > b:
        return 0
    else:
        return 1


def end_result():   # 몇 번만에 맞췄는지 결과 알림이
    if count == 1:
        print("한번에 맞추셨군요! 로또를 한번 사보시는건 어떤가요?")
    elif count <= 3:
        print(str(count) + "번 만에 맞추셨군요! 대단해요!")
    elif count <= 10:
        print(str(count) + "번 만에 맞추셨습니다. 수고하셨습니다.")
    else:
        print(str(count) + "번 만에 맞추시다니, 찍기에 소질이 없으시군요!")


print("안녕.\n난 100부터 999 중 숫자 하나를 골랐어요.")
guess = int(input("뭔지 쓰고 엔터 키를 누르세요."))
count += 1  # guess를 하나 받을 때 마다 count를 하나씩 올려줌.

result = compare(com_num, guess)

while result != 2:
    count += 1
    if result == 0:
        guess = int(input("Up"))
    else:
        guess = int(input("Down"))

    result = compare(com_num, guess)

end_result()

input("\n\n마치려면 엔터 키를 누르세요.")
