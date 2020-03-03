# baseball game

import random

answer = str(random.randint(100, 999))
count = 0


def baseball(a, b):
    strike = 0
    ball = 0
    for i in range(0, len(answer)):
        for j in range(0, len(guess)):
            if answer[i] == guess[j]:  # 숫자 같음
                if i == j:  # 자리도 같으면 strike
                    strike += 1
                else:       # 자리는 다르면 ball
                    ball += 1
    print(str(strike) + " Strike, " + str(ball) + " ball")


count += 1
print(answer)
guess = input("# " + str(count) + ": Your guess? ")

if answer == guess:
    pass
else:
    baseball(answer, guess)
    while True:
        count += 1
        guess = input("# " + str(count) + ": Your guess? ")
        if answer == guess:
            break
        else:
            baseball(answer, guess)
print("Homerun!!!!")