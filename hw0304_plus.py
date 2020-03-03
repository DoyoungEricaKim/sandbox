
import random


def pick_quiz():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = nums[random.randint(0, len(nums) - 1)]
    nums.remove(a)
    b = nums[random.randint(0, len(nums) - 1)]
    nums.remove(b)
    c = nums[random.randint(0, len(nums) - 1)]
    quiz = str(a) + str(b) + str(c)
    print(quiz)
    return quiz


def validate(num):
    if "0" in num:
        print("Error: Only Three-digit-number without zero is allowed.")
        return False
    else:
        return True


def determine(quiz, guess):
    strike = 0
    ball = 0
    if validate(guess):
        for i in range(0, len(quiz)):
            for j in range(0, len(guess)):
                if quiz[i] == guess[j]:  # 숫자 같음
                    if i == j:  # 자리도 같으면 strike
                        strike += 1
                    else:  # 자리는 다르면 ball
                        ball += 1
        print(str(strike) + " Strike, " + str(ball) + " ball")


def playball(quiz):
    count = 0
    count += 1

    print("quiz:" + quiz)
    guess = input("# " + str(count) + ": Your guess? ")
    if quiz == guess:
        pass
    else:
        determine(quiz, guess)
        while True:
            count += 1
            guess = input("# " + str(count) + ": Your guess? ")
            if quiz == guess:
                break
            else:
                determine(quiz, guess)
    print("Homerun!!!!")


if __name__ == '__main__':
    playball(pick_quiz())